import sounddevice as sd
import numpy as np
import logging
import json
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestAudioProcessor:
    def __init__(self):
        self.is_running = False
        self.sample_rate = 16000
        self.chunk_duration = 0.1
        self.silence_threshold = 0.01
        self.current_speech_start = None
        self.speech_buffer = []
        self.ws_server = None
    
    def set_ws_server(self, ws_server):
        self.ws_server = ws_server
    
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
                self.current_speech_start = datetime.now()
                logger.info("检测到语音开始")
                self.send_status("speech_start")
        else:
            if self.current_speech_start is not None:
                speech_duration = (datetime.now() - self.current_speech_start).total_seconds()
                
                if speech_duration >= 0.3:
                    if len(self.speech_buffer) > 0:
                        audio_data = np.concatenate(self.speech_buffer)
                        self.process_speech(audio_data, speech_duration)
                    
                    self.current_speech_start = None
                    self.speech_buffer = []
                    logger.info(f"语音结束，持续时间: {speech_duration:.2f}秒")
                    self.send_status("speech_end", {"duration": speech_duration})
    
    def process_speech(self, audio_data, duration):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        result = {
            "type": "test",
            "message": "检测到语音片段",
            "duration": round(duration, 2),
            "timestamp": timestamp,
            "audio_length": len(audio_data)
        }
        
        logger.info(f"处理语音片段: {result}")
        
        if self.ws_server:
            self.ws_server.add_result(result)
    
    def send_status(self, status_type, data=None):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        result = {
            "type": "status",
            "status_type": status_type,
            "timestamp": timestamp
        }
        if data:
            result.update(data)
        
        if self.ws_server:
            self.ws_server.add_result(result)
    
    def start(self):
        if self.is_running:
            logger.warning("音频处理器已在运行")
            return False
        
        self.is_running = True
        self.speech_buffer = []
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
            self.is_running = False
            return False
    
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