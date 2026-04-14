# 语音输入功能集成指南

## 概述

本文档说明如何将语音输入功能集成到现有的医药助教项目中。当前实现使用浏览器原生的 Web Speech API 进行语音识别，可以轻松扩展为调用豆包语音识别 API。

## 当前实现

### 技术方案

- **语音识别**: 使用浏览器原生的 Web Speech API
- **支持语言**: 中文 (zh-CN)
- **实时识别**: 支持实时显示识别结果
- **浏览器兼容**: Chrome/Edge 完全支持，Firefox/Safari 部分支持

### 核心组件

#### VoiceInput 组件

位置: `Voice/src/components/VoiceInput.jsx`

主要功能:
- 开始/停止录音
- 实时语音识别
- 识别结果回调
- 录音状态可视化

## 集成到现有项目

### 方法一：直接复制组件

1. 将 `Voice/src/components/VoiceInput.jsx` 复制到项目的 `src/components/` 目录

2. 在需要使用语音输入的组件中引入:

```jsx
import VoiceInput from './components/VoiceInput'
```

3. 在 ChatInterface 组件中集成:

```jsx
function ChatInterface({ onReview, practiceCase, examMode = false }) {
  // ... 现有代码 ...
  
  const [input, setInput] = useState('')
  const [isVoiceInput, setIsVoiceInput] = useState(false)
  
  const handleTranscript = (text, isInterim, isFinal) => {
    setInput(text)
    setIsVoiceInput(!isFinal)
    
    if (isFinal && text.trim()) {
      handleSendMessage(text)
    }
  }
  
  // ... 现有代码 ...
  
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
      {/* ... 现有代码 ... */}
      
      <div className="flex gap-3">
        <div className="flex-1 relative">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
            placeholder={isVoiceInput ? '正在识别语音...' : '输入您的回复...'}
            disabled={isLoading || isVoiceInput}
            className={`flex-1 px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 transition-all ${
              isVoiceInput ? 'border-blue-300 bg-blue-50' : 'border-gray-300'
            }`}
          />
          {isVoiceInput && (
            <div className="absolute right-3 top-1/2 transform -translate-y-1/2">
              <div className="flex gap-1">
                <div className="w-1 h-4 bg-blue-500 rounded-full animate-bounce" />
                <div className="w-1 h-4 bg-blue-500 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }} />
                <div className="w-1 h-4 bg-blue-500 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
              </div>
            </div>
          )}
        </div>
        
        <VoiceInput 
          onTranscript={handleTranscript}
          disabled={isLoading}
        />
        
        <button
          onClick={handleSendMessage}
          disabled={!input.trim() || isLoading || isVoiceInput}
          className="px-6 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-lg hover:from-blue-600 hover:to-indigo-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
        >
          <Send className="w-4 h-4" />
          发送
        </button>
      </div>
    </div>
  )
}
```

### 方法二：使用独立演示页面

如果不想修改现有代码，可以直接使用 `Voice/demo.html` 作为独立的语音输入演示页面。

## 升级到豆包语音识别 API

### 准备工作

1. 获取豆包 API 凭证:
   - APP ID
   - Access Token
   - Resource ID

2. 参考文档: https://www.volcengine.com/docs/6561/1798094

### 实现步骤

#### 1. 创建后端 API 端点

在 `backend.py` 中添加语音识别端点:

```python
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import httpx
import json
import os
from dotenv import load_dotenv

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
VOLC_RESOURCE_ID = "volc.lark.minutes"

@app.post("/api/voice/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    语音转文字接口
    """
    try:
        # 1. 上传音频文件到对象存储（需要实现）
        file_url = await upload_audio_to_tos(file)
        
        # 2. 提交识别任务
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
        
        async with httpx.AsyncClient() as client:
            response = await client.post(submit_url, headers=headers, json=payload)
            result = response.json()
            
            if result.get("X-Api-Status-Code") != "20000000":
                raise Exception(f"提交任务失败: {result}")
            
            task_id = result["Data"]["TaskID"]
            
            # 3. 轮询查询结果
            query_url = "https://openspeech.bytedance.com/api/v3/auc/lark/query"
            max_attempts = 60  # 最多等待60秒
            
            for attempt in range(max_attempts):
                await asyncio.sleep(1)
                
                headers["X-Api-Request-Id"] = task_id
                query_payload = {"TaskID": task_id}
                
                response = await client.post(query_url, headers=headers, json=query_payload)
                result = response.json()
                
                status = result["Data"]["Status"]
                
                if status == "success":
                    # 4. 获取识别结果
                    transcription_url = result["Data"]["Result"]["AudioTranscriptionFile"]
                    transcription_response = await client.get(transcription_url)
                    transcription_data = transcription_response.json()
                    
                    # 提取文本
                    text = " ".join([item["content"] for item in transcription_data])
                    
                    return {"text": text, "status": "success"}
                    
                elif status == "failed":
                    raise Exception(f"识别失败: {result['Data'].get('ErrMessage', '未知错误')}")
                
            raise Exception("识别超时")
            
    except Exception as e:
        return {"error": str(e), "status": "error"}

async def upload_audio_to_tos(file: UploadFile):
    """
    上传音频文件到火山引擎对象存储
    需要根据实际情况实现
    """
    # 这里需要实现上传到 TOS 的逻辑
    # 返回可访问的文件 URL
    pass
```

#### 2. 修改前端 VoiceInput 组件

创建 `VoiceInputDoubao.jsx`:

```jsx
import { useState, useRef } from 'react'
import { Mic, MicOff, Loader2 } from 'lucide-react'

function VoiceInputDoubao({ onTranscript, disabled }) {
  const [isRecording, setIsRecording] = useState(false)
  const [isProcessing, setIsProcessing] = useState(false)
  const mediaRecorderRef = useRef(null)
  const audioChunksRef = useRef([])

  const handleStartRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      const mediaRecorder = new MediaRecorder(stream)
      
      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data)
        }
      }
      
      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/wav' })
        await transcribeAudio(audioBlob)
        audioChunksRef.current = []
      }
      
      mediaRecorderRef.current = mediaRecorder
      mediaRecorder.start()
      setIsRecording(true)
    } catch (error) {
      console.error('录音失败:', error)
      alert('无法访问麦克风，请检查权限设置')
    }
  }

  const handleStopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop()
      mediaRecorderRef.current.stream.getTracks().forEach(track => track.stop())
      setIsRecording(false)
      setIsProcessing(true)
    }
  }

  const transcribeAudio = async (audioBlob) => {
    try {
      const formData = new FormData()
      formData.append('file', audioBlob, 'recording.wav')
      
      const response = await fetch('/api/voice/transcribe', {
        method: 'POST',
        body: formData
      })
      
      const result = await response.json()
      
      if (result.status === 'success') {
        onTranscript(result.text, false, true)
      } else {
        throw new Error(result.error || '识别失败')
      }
    } catch (error) {
      console.error('语音识别失败:', error)
      alert('语音识别失败: ' + error.message)
    } finally {
      setIsProcessing(false)
    }
  }

  const handleToggleRecording = () => {
    if (isRecording) {
      handleStopRecording()
    } else {
      handleStartRecording()
    }
  }

  return (
    <button
      onClick={handleToggleRecording}
      disabled={disabled || isProcessing}
      className={`relative flex items-center justify-center w-12 h-12 rounded-full transition-all ${
        isRecording
          ? 'bg-red-500 hover:bg-red-600 text-white animate-pulse'
          : 'bg-blue-500 hover:bg-blue-600 text-white'
      } ${disabled || isProcessing ? 'opacity-50 cursor-not-allowed' : ''}`}
      title={isRecording ? '停止录音' : '开始录音'}
    >
      {isProcessing ? (
        <Loader2 className="w-5 h-5 animate-spin" />
      ) : isRecording ? (
        <MicOff className="w-5 h-5" />
      ) : (
        <Mic className="w-5 h-5" />
      )}
      
      {isRecording && (
        <span className="absolute -bottom-6 left-1/2 transform -translate-x-1/2 text-xs text-red-500 font-medium whitespace-nowrap">
          录音中...
        </span>
      )}
    </button>
  )
}

export default VoiceInputDoubao
```

#### 3. 更新环境变量

在 `.env` 文件中添加:

```env
VOLC_APP_KEY=your_app_key_here
VOLC_ACCESS_KEY=your_access_key_here
```

## 测试

### 测试浏览器原生语音识别

1. 打开 `Voice/demo.html`
2. 点击麦克风按钮
3. 允许麦克风权限
4. 开始说话
5. 查看实时识别结果

### 测试豆包语音识别

1. 配置好 API 凭证
2. 启动后端服务: `python backend.py`
3. 在 ChatInterface 中使用 VoiceInputDoubao 组件
4. 测试录音和识别功能

## 注意事项

1. **浏览器兼容性**: Web Speech API 在 Chrome/Edge 中表现最佳
2. **麦克风权限**: 首次使用需要用户授权
3. **网络连接**: 语音识别需要网络连接
4. **识别准确度**: 受环境噪音、语音清晰度影响
5. **API 限制**: 豆包 API 有调用频率和配额限制

## 故障排除

### 浏览器不支持语音识别

- 使用 Chrome 或 Edge 浏览器
- 更新浏览器到最新版本

### 无法访问麦克风

- 检查浏览器权限设置
- 确保系统已授予麦克风权限
- 尝试使用 HTTPS 协议（某些浏览器要求）

### 识别准确度低

- 减少环境噪音
- 清晰、缓慢地说话
- 调整麦克风位置

### 豆包 API 调用失败

- 检查 API 凭证是否正确
- 确认网络连接正常
- 查看后端日志获取详细错误信息
- 检查 API 配额是否充足

## 总结

当前实现提供了完整的语音输入功能，使用浏览器原生 API 即可满足基本需求。如需更高准确度或特殊功能，可以升级到豆包语音识别 API。两种方案都可以无缝集成到现有项目中。