import sounddevice as sd
import numpy as np
import queue
import logging
import json
from vosk import Model, KaldiRecognizer
import threading
import time
from datetime import datetime
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AudioProcessor:
    def __init__(self, model_path="vosk-model-small-cn"):
        self.model_path = model_path
        self.model = None
        self.recognizer = None
        self.audio_queue = queue.Queue()
        self.is_running = False
        self.recognition_thread = None
        self.sample_rate = 16000
        self.chunk_duration = 0.1  # 100ms chunks
        self.silence_threshold = 0.01
        self.min_speech_duration = 0.3  # 300ms minimum speech
        self.current_speech_start = None
        self.speech_buffer = []
        self.total_speech_duration = 0.0
        
    def load_model(self):
        try:
            logger.info(f"正在加载Vosk模型: {self.model_path}")
            self.model = Model(self.model_path)
            self.recognizer = KaldiRecognizer(self.model, self.sample_rate)
            logger.info("Vosk模型加载成功")
            return True
        except Exception as e:
            logger.error(f"Vosk模型加载失败: {e}")
            return False
    
    def start(self):
        if self.is_running:
            logger.warning("音频处理器已在运行")
            return False
        
        if not self.load_model():
            logger.error("模型加载失败，无法启动音频处理器")
            return False
        
        self.is_running = True
        self.speech_buffer = []
        self.total_speech_duration = 0.0
        self.current_speech_start = None
        
        logger.info(f"开始音频捕获，采样率: {self.sample_rate}Hz")
        
        try:
            self.stream = sd.InputStream(
                samplerate=self.sample_rate,
                channels=1,
                dtype='float32',
                blocksize=int(self.sample_rate * self.chunk_duration),
                callback=self.audio_callback
            )
            self.stream.start()
            logger.info("音频流启动成功")
            return True
        except Exception as e:
            logger.error(f"音频流启动失败: {e}")
            if "Permission" in str(e) or "denied" in str(e).lower():
                print("请检查麦克风权限")
                logger.error("请检查麦克风权限")
            elif "device" in str(e).lower():
                print("请检查音频设备连接")
                logger.error("请检查音频设备连接")
            self.is_running = False
            return False
    
    def audio_callback(self, indata, frames, time_info, status):
        if status.InputOverflow:
            logger.warning("音频输入溢出")
            return
        
        if not self.is_running:
            return
        
        audio_float32 = indata.flatten()
        audio_level = np.abs(audio_float32).mean()
        
        self.speech_buffer.extend(audio_float32)
        
        if audio_level > self.silence_threshold:
            if self.current_speech_start is None:
                self.current_speech_start = time.time()
                logger.info("检测到语音开始")
        else:
            if self.current_speech_start is not None:
                speech_duration = time.time() - self.current_speech_start
                
                if speech_duration >= self.min_speech_duration:
                    self.total_speech_duration += speech_duration
                    
                    if len(self.speech_buffer) > 0:
                        audio_data = np.concatenate(self.speech_buffer)
                        self.process_speech(audio_data)
                    
                    self.current_speech_start = None
                    self.speech_buffer = []
                    logger.info(f"语音结束，持续时间: {speech_duration:.2f}秒")
    
    def process_speech(self, audio_data):
        try:
            if self.recognizer:
                rec = self.recognizer
                rec.AcceptWaveform(audio_data)
                
                while rec.Result():
                    result = rec.Result()
                    rec.Reset()
                    
                    if result and result.strip():
                        self.output_result(result)
                        
                partial_result = rec.PartialResult()
                if partial_result and partial_result.strip():
                    self.output_partial_result(partial_result)
                    
        except Exception as e:
            logger.error(f"语音识别处理失败: {e}")
    
    def output_result(self, text):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        result = {
            "type": "final",
            "text": text,
            "timestamp": timestamp,
            "duration": self.total_speech_duration
        }
        print(f"识别结果: {json.dumps(result, ensure_ascii=False)}")
        self.total_speech_duration = 0.0
    
    def output_partial_result(self, text):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        result = {
            "type": "partial",
            "text": text,
            "timestamp": timestamp
        }
        print(f"部分识别: {json.dumps(result, ensure_ascii=False)}")
    
    def stop(self):
        if not self.is_running:
            return
        
        self.is_running = False
        
        if hasattr(self, 'stream') and self.stream:
            try:
                self.stream.stop()
                self.stream.close()
                logger.info("音频流已停止")
            except Exception as e:
                logger.error(f"停止音频流失败: {e}")
        
        self.speech_buffer = []
        self.current_speech_start = None
        self.total_speech_duration = 0.0
    
    def get_memory_usage(self):
        import psutil
        process = psutil.Process()
        memory_info = process.memory_info()
        return memory_info.rss / 1024 / 1024  # MB

def main():
    processor = AudioProcessor("vosk-model-small-cn")
    
    if not processor.start():
        logger.error("音频处理器启动失败")
        return
    
    logger.info("音频处理器运行中，按Ctrl+C停止...")
    
    try:
        while True:
            time.sleep(1)
            
            if processor.is_running:
                memory_mb = processor.get_memory_usage()
                if memory_mb > 100:
                    logger.warning(f"内存使用过高: {memory_mb:.1f}MB")
    
    except KeyboardInterrupt:
        logger.info("接收到停止信号")
    finally:
        processor.stop()
        logger.info("音频处理器已停止")

if __name__ == "__main__":
    main()