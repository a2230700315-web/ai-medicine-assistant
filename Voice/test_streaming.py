import websocket
import json
import threading
import time
import uuid

VOLC_APP_ID = "8636573250"
VOLC_ACCESS_KEY = "TBd8NadSYc_OK17mLnnQk0NN8WflbZWJ"
VOLC_RESOURCE_ID = "volc.seedasr.sauc.duration"

print("=" * 50)
print("豆包流式语音识别大模型API测试")
print("=" * 50)
print(f"VOLC_APP_ID: {VOLC_APP_ID}")
print(f"VOLC_ACCESS_KEY: {VOLC_ACCESS_KEY[:10]}...")
print(f"VOLC_RESOURCE_ID: {VOLC_RESOURCE_ID}")
print("=" * 50)

def on_message(ws, message):
    print(f"收到消息: {message}")

def on_error(ws, error):
    print(f"错误: {error}")

def on_close(ws, close_status_code, close_msg):
    print("连接关闭")

def on_open(ws):
    print("连接成功！")
    
    start_request = {
        "user": {
            "uid": "test_user_001"
        },
        "audio": {
            "format": "pcm",
            "rate": 16000,
            "bits": 16,
            "channel": 1,
            "language": "zh-CN"
        },
        "request": {
            "model_name": "bigmodel",
            "enable_itn": True,
            "enable_ddc": False,
            "enable_punc": True
        }
    }
    
    print(f"发送配置请求: {json.dumps(start_request, ensure_ascii=False)}")
    ws.send(json.dumps(start_request, ensure_ascii=False))
    
    time.sleep(3)
    
    finish_request = {
        "event": 2
    }
    
    print(f"发送结束请求")
    ws.send(json.dumps(finish_request, ensure_ascii=False))

if __name__ == "__main__":
    try:
        ws_url = "wss://openspeech.bytedance.com/api/v3/sauc/bigmodel"
        headers = {
            "X-Api-App-Key": VOLC_APP_ID,
            "X-Api-Access-Key": VOLC_ACCESS_KEY,
            "X-Api-Resource-Id": VOLC_RESOURCE_ID,
            "X-Api-Connect-Id": str(uuid.uuid4())
        }
        
        print(f"正在连接到: {ws_url}")
        print(f"请求头: {json.dumps(headers, indent=2, ensure_ascii=False)}")
        
        ws = websocket.WebSocketApp(
            ws_url,
            header=headers,
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close
        )
        
        ws.run_forever()
        
    except Exception as e:
        print(f"连接失败: {str(e)}")
        print("可能的原因:")
        print("1. 网络连接问题")
        print("2. API密钥配置错误")
        print("3. 需要安装websocket库: pip install websocket-client")

print("\n" + "=" * 50)