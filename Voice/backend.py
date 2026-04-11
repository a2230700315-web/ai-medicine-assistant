from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import httpx
import uuid
import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

VOLC_APP_KEY = os.getenv("VOLC_APP_KEY")
VOLC_ACCESS_KEY = os.getenv("VOLC_ACCESS_KEY")
VOLC_RESOURCE_ID = os.getenv("VOLC_RESOURCE_ID", "volc.lark.minutes")

@app.get("/")
async def root():
    return {"message": "豆包语音识别API服务", "status": "running"}

@app.post("/api/voice/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    语音转文字接口
    """
    try:
        if not VOLC_APP_KEY or not VOLC_ACCESS_KEY:
            return {"error": "请配置VOLC_APP_KEY和VOLC_ACCESS_KEY环境变量", "status": "error"}
        
        file_content = await file.read()
        file_size = len(file_content)
        
        if file_size == 0:
            return {"error": "音频文件为空", "status": "error"}
        
        file_url = f"data:audio/wav;base64,{file_content.decode('utf-8')}"
        
        submit_url = "https://openspeech.bytedance.com/api/v3/auc/lark/submit"
        headers = {
            "X-Api-App-Key": VOLC_APP_KEY,
            "X-Api-Access-Key": VOLC_ACCESS_KEY,
            "X-Api-Resource-Id": VOLC_RESOURCE_ID,
            "X-Api-Request-Id": str(uuid.uuid4()),
            "X-Api-Sequence": "-1",
            "Content-Type": "application/json"
        }
        
        payload = {
            "Input": {
                "Offline": {
                    "FileURL": file_url,
                    "FileType": "audio"
                }
            },
            "Params": {
                "AllActivate": True,
                "SourceLang": "zh_cn",
                "AudioTranscriptionEnable": True,
                "AudioTranscriptionParams": {
                    "SpeakerIdentification": False,
                    "NumberOfSpeaker": 0,
                    "NeedWordTimeSeries": False
                }
            }
        }
        
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(submit_url, headers=headers, json=payload)
            result = response.json()
            
            if result.get("X-Api-Status-Code") != "20000000":
                return {"error": f"提交任务失败: {result}", "status": "error"}
            
            task_id = result["Data"]["TaskID"]
            
            query_url = "https://openspeech.bytedance.com/api/v3/auc/lark/query"
            max_attempts = 60
            
            for attempt in range(max_attempts):
                import asyncio
                await asyncio.sleep(1)
                
                headers["X-Api-Request-Id"] = task_id
                query_payload = {"TaskID": task_id}
                
                response = await client.post(query_url, headers=headers, json=query_payload)
                result = response.json()
                
                status = result["Data"]["Status"]
                
                if status == "success":
                    transcription_url = result["Data"]["Result"]["AudioTranscriptionFile"]
                    transcription_response = await client.get(transcription_url)
                    transcription_data = transcription_response.json()
                    
                    text = " ".join([item.get("content", "") for item in transcription_data])
                    
                    return {"text": text, "status": "success", "task_id": task_id}
                    
                elif status == "failed":
                    error_msg = result['Data'].get('ErrMessage', '未知错误')
                    return {"error": f"识别失败: {error_msg}", "status": "failed"}
                
            return {"error": "识别超时", "status": "timeout"}
            
    except Exception as e:
        return {"error": str(e), "status": "error"}

@app.get("/api/voice/status")
async def get_status():
    """
    获取API配置状态
    """
    return {
        "app_key_configured": bool(VOLC_APP_KEY),
        "access_key_configured": bool(VOLC_ACCESS_KEY),
        "resource_id": VOLC_RESOURCE_ID,
        "status": "ready" if VOLC_APP_KEY and VOLC_ACCESS_KEY else "not_configured"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)