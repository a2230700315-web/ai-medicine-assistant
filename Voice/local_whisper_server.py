import os
import io
import base64
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from faster_whisper import WhisperModel
import torch
import numpy as np
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

MODEL_SIZE = os.getenv("WHISPER_MODEL_SIZE", "small")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
LANGUAGE = os.getenv("WHISPER_LANGUAGE", "zh")

logger.info(f"正在加载Whisper模型，大小: {MODEL_SIZE}, 设备: {DEVICE}")
model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type="float16")

@app.route("/")
def home():
    return jsonify({
        "message": "本地Whisper语音识别API服务",
        "status": "running",
        "model": MODEL_SIZE,
        "device": DEVICE,
        "language": LANGUAGE
    })

@app.route("/api/voice/transcribe", methods=["POST"])
def transcribe_audio():
    try:
        if "audio" not in request.files:
            return jsonify({"error": "缺少音频文件", "status": "error"}), 400
        
        audio_file = request.files["audio"]
        
        if audio_file.filename == "":
            return jsonify({"error": "音频文件名为空", "status": "error"}), 400
        
        logger.info(f"收到音频文件: {audio_file.filename}")
        
        audio_data = audio_file.read()
        
        audio_array, sample_rate = convert_audio_to_array(audio_data)
        
        logger.info(f"开始语音识别，音频长度: {len(audio_array)/sample_rate:.2f}秒")
        
        segments, info = model.transcribe(
            audio_array,
            language=LANGUAGE,
            beam_size=5,
            vad_filter=True,
            word_timestamps=True
        )
        
        text = " ".join([segment.text for segment in segments])
        
        logger.info(f"识别完成，文本长度: {len(text)}字符")
        
        return jsonify({
            "text": text,
            "status": "success",
            "language": LANGUAGE,
            "duration": len(audio_array) / sample_rate,
            "segments": [{"start": seg.start, "end": seg.end, "text": seg.text} for seg in segments]
        })
        
    except Exception as e:
        logger.error(f"语音识别失败: {str(e)}")
        return jsonify({"error": str(e), "status": "error"}), 500

@app.route("/api/voice/transcribe_base64", methods=["POST"])
def transcribe_base64():
    try:
        data = request.get_json()
        
        if not data or "audio_data" not in data:
            return jsonify({"error": "缺少音频数据", "status": "error"}), 400
        
        audio_base64 = data["audio_data"]
        
        if "," in audio_base64:
            audio_base64 = audio_base64.split(",")[1]
        
        audio_data = base64.b64decode(audio_base64)
        
        audio_array, sample_rate = convert_audio_to_array(audio_data)
        
        logger.info(f"开始语音识别，音频长度: {len(audio_array)/sample_rate:.2f}秒")
        
        segments, info = model.transcribe(
            audio_array,
            language=LANGUAGE,
            beam_size=5,
            vad_filter=True,
            word_timestamps=True
        )
        
        text = " ".join([segment.text for segment in segments])
        
        logger.info(f"识别完成，文本长度: {len(text)}字符")
        
        return jsonify({
            "text": text,
            "status": "success",
            "language": LANGUAGE,
            "duration": len(audio_array) / sample_rate,
            "segments": [{"start": seg.start, "end": seg.end, "text": seg.text} for seg in segments]
        })
        
    except Exception as e:
        logger.error(f"语音识别失败: {str(e)}")
        return jsonify({"error": str(e), "status": "error"}), 500

@app.route("/api/voice/status", methods=["GET"])
def get_status():
    return jsonify({
        "model": MODEL_SIZE,
        "device": DEVICE,
        "language": LANGUAGE,
        "cuda_available": torch.cuda.is_available(),
        "status": "ready"
    })

def convert_audio_to_array(audio_data):
    try:
        import soundfile as sf
        audio_array, sample_rate = sf.read(io.BytesIO(audio_data))
        
        if len(audio_array.shape) > 1:
            audio_array = audio_array.mean(axis=1)
        
        if audio_array.dtype != np.float32:
            audio_array = audio_array.astype(np.float32)
        
        return audio_array, sample_rate
    except ImportError:
        logger.warning("soundfile未安装，使用简单音频处理")
        return simple_audio_processing(audio_data)

def simple_audio_processing(audio_data):
    sample_rate = 16000
    audio_array = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
    return audio_array, sample_rate

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    logger.info(f"启动本地Whisper语音识别服务，端口: {port}")
    app.run(host="0.0.0.0", port=port, debug=False)