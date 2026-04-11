import asyncio
import websockets
import json
import logging
import threading
import time
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VoskWebSocketServer:
    def __init__(self, host="0.0.0.0", port=8765):
        self.host = host
        self.port = port
        self.clients = set()
        self.server = None
        self.is_running = False
        self.broadcast_thread = None
        self.result_queue = []
        self.queue_lock = threading.Lock()
        self.audio_processor = None
        self.test_mode = False
    
    async def handle_client(self, websocket, path):
        self.clients.add(websocket)
        client_id = id(websocket)
        logger.info(f"客户端 {client_id} 已连接，当前连接数: {len(self.clients)}")
        
        try:
            await websocket.send(json.dumps({
                "type": "connected",
                "message": "Vosk实时语音识别服务已连接",
                "mode": "test" if self.test_mode else "vosk",
                "timestamp": datetime.now().strftime("%H:%M:%S.%f")[:-3]
            }, ensure_ascii=False))
            
            async for message in websocket:
                try:
                    data = json.loads(message)
                    
                    if data.get("action") == "start":
                        logger.info(f"客户端 {client_id} 请求开始识别")
                        success = self.start_recognition()
                        await websocket.send(json.dumps({
                            "type": "status",
                            "action": "start",
                            "success": success,
                            "message": "识别已启动" if success else "识别启动失败",
                            "mode": "test" if self.test_mode else "vosk",
                            "timestamp": datetime.now().strftime("%H:%M:%S.%f")[:-3]
                        }, ensure_ascii=False))
                    
                    elif data.get("action") == "stop":
                        logger.info(f"客户端 {client_id} 请求停止识别")
                        self.stop_recognition()
                        await websocket.send(json.dumps({
                            "type": "status",
                            "action": "stop",
                            "success": True,
                            "message": "识别已停止",
                            "timestamp": datetime.now().strftime("%H:%M:%S.%f")[:-3]
                        }, ensure_ascii=False))
                    
                    elif data.get("action") == "status":
                        memory_mb = 0
                        if hasattr(self.audio_processor, 'get_memory_usage'):
                            memory_mb = self.audio_processor.get_memory_usage()
                        
                        await websocket.send(json.dumps({
                            "type": "status",
                            "is_running": self.is_running and self.audio_processor and self.audio_processor.is_running,
                            "memory_mb": round(memory_mb, 2),
                            "clients_count": len(self.clients),
                            "mode": "test" if self.test_mode else "vosk",
                            "timestamp": datetime.now().strftime("%H:%M:%S.%f")[:-3]
                        }, ensure_ascii=False))
                
                except json.JSONDecodeError as e:
                    logger.error(f"JSON解析错误: {e}")
                except Exception as e:
                    logger.error(f"处理客户端消息失败: {e}")
        
        except websockets.exceptions.ConnectionClosed:
            logger.info(f"客户端 {client_id} 连接已关闭")
        except Exception as e:
            logger.error(f"客户端处理错误: {e}")
        finally:
            self.clients.discard(websocket)
            logger.info(f"客户端 {client_id} 已断开，当前连接数: {len(self.clients)}")
    
    def broadcast_results(self):
        while self.is_running:
            try:
                with self.queue_lock:
                    if self.result_queue:
                        results = self.result_queue.copy()
                        self.result_queue.clear()
                    else:
                        results = []
                
                if results and self.clients:
                    for result in results:
                        message = json.dumps(result, ensure_ascii=False)
                        disconnected_clients = set()
                        
                        for client in self.clients:
                            try:
                                asyncio.run_coroutine_threadsafe(
                                    client.send(message),
                                    self.server.loop
                                )
                            except Exception as e:
                                logger.error(f"发送消息失败: {e}")
                                disconnected_clients.add(client)
                        
                        for client in disconnected_clients:
                            self.clients.discard(client)
                
                time.sleep(0.01)
            
            except Exception as e:
                logger.error(f"广播结果失败: {e}")
    
    def add_result(self, result):
        with self.queue_lock:
            self.result_queue.append(result)
    
    def start_recognition(self):
        if self.audio_processor and self.audio_processor.is_running:
            logger.warning("识别已在运行")
            return True
        
        if self.audio_processor:
            return self.audio_processor.start()
        return False
    
    def stop_recognition(self):
        if self.audio_processor:
            self.audio_processor.stop()
    
    async def start_server(self):
        logger.info(f"启动Vosk WebSocket服务器: {self.host}:{self.port}")
        
        self.is_running = True
        self.broadcast_thread = threading.Thread(target=self.broadcast_results, daemon=True)
        self.broadcast_thread.start()
        
        self.server = await websockets.serve(
            self.handle_client,
            self.host,
            self.port,
            ping_interval=20,
            ping_timeout=60
        )
        
        logger.info("Vosk WebSocket服务器已启动")
        
        await self.server.wait_closed()
    
    def stop_server(self):
        self.is_running = False
        self.stop_recognition()
        logger.info("Vosk WebSocket服务器已停止")

async def main():
    server = VoskWebSocketServer()
    
    try:
        from audio_processor import AudioProcessor
        server.audio_processor = AudioProcessor("vosk-model-small-cn")
        logger.info("使用Vosk音频处理器")
    except Exception as e:
        logger.warning(f"无法加载Vosk音频处理器: {e}")
        logger.info("切换到测试模式")
        
        from test_audio_processor import TestAudioProcessor
        server.audio_processor = TestAudioProcessor()
        server.audio_processor.set_ws_server(server)
        server.test_mode = True
        logger.info("使用测试音频处理器")
    
    try:
        await server.start_server()
    except KeyboardInterrupt:
        logger.info("接收到停止信号")
    finally:
        server.stop_server()

if __name__ == "__main__":
    asyncio.run(main())