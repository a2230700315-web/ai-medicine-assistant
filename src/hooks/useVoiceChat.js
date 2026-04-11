import { useState, useRef, useCallback } from 'react'

const useVoiceChat = () => {
  const [isRecording, setIsRecording] = useState(false)
  const [isProcessing, setIsProcessing] = useState(false)
  const [isSupported, setIsSupported] = useState(true) // 添加浏览器支持状态
  const recognitionRef = useRef(null)
  const mediaRecorderRef = useRef(null)
  const audioChunksRef = useRef([])
  const finalTranscriptRef = useRef('')
  const currentTranscriptRef = useRef('') // 新增：用于存储当前识别的文本

  // 首先定义所有被引用的函数
  const startBackendRecording = useCallback(async (onTranscript) => {
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
        await transcribeWithBackend(audioBlob, onTranscript)
        audioChunksRef.current = []
      }
      
      mediaRecorderRef.current = mediaRecorder
      mediaRecorder.start()
      setIsRecording(true)
    } catch (error) {
      console.error('录音失败:', error)
      alert('无法访问麦克风，请检查权限设置')
    }
  }, [])

  const stopBackendRecording = useCallback(() => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop()
      mediaRecorderRef.current.stream.getTracks().forEach(track => track.stop())
      setIsRecording(false)
      setIsProcessing(true)
    }
  }, [isRecording])

  const transcribeAudio = useCallback(async (audioBlob) => {
    try {
      const formData = new FormData()
      formData.append('file', audioBlob, 'recording.wav')
      
      const response = await fetch('/api/voice/transcribe', {
        method: 'POST',
        body: formData
      })
      
      const result = await response.json()
      
      if (result.status === 'success') {
        return result.text
      } else {
        throw new Error(result.error || '识别失败')
      }
    } catch (error) {
      console.error('语音识别失败:', error)
      throw error
    }
  }, [])

  const transcribeWithBackend = useCallback(async (audioBlob, onTranscript) => {
    try {
      const text = await transcribeAudio(audioBlob)
      if (onTranscript && typeof onTranscript === 'function') {
        onTranscript(text, false, true)
      }
    } catch (error) {
      alert('语音识别失败: ' + error.message)
    } finally {
      setIsProcessing(false)
    }
  }, [transcribeAudio])

  const stopBrowserRecording = useCallback((onTranscript) => {
    if (recognitionRef.current && isRecording) {
      recognitionRef.current.stop()
      setIsProcessing(true)
      
      setTimeout(() => {
        setIsProcessing(false)
        
        // 使用当前识别的文本，确保有内容
        const lastResult = currentTranscriptRef.current || finalTranscriptRef.current || ''
        console.log('停止录音，最终结果:', lastResult)
        
        if (onTranscript && typeof onTranscript === 'function' && lastResult) {
          console.log('停止录音，调用onTranscript:', lastResult)
          onTranscript(lastResult, false, true)
        }
        
        // 重置状态
        currentTranscriptRef.current = ''
        finalTranscriptRef.current = ''
      }, 500)
    }
  }, [isRecording])

  // 最后定义主函数
  const startRecording = useCallback((onTranscript) => {
    console.log('开始语音识别...')
    
    // 检查浏览器支持
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    const isBrowserSupported = !!SpeechRecognition
    
    if (!isBrowserSupported) {
      console.log('浏览器不支持语音识别')
      setIsSupported(false)
      return
    }
    
    if (isBrowserSupported) {
      
      if (!recognitionRef.current) {
        console.log('初始化语音识别器...')
        recognitionRef.current = new SpeechRecognition()
        recognitionRef.current.continuous = true
        recognitionRef.current.interimResults = true
        recognitionRef.current.lang = 'zh-CN'
        
        recognitionRef.current.onresult = (event) => {
          console.log('接收到语音识别结果:', event)
          let interimTranscript = ''
          let currentFinalTranscript = ''
          
          for (let i = event.resultIndex; i < event.results.length; i++) {
            const transcript = event.results[i][0].transcript
            console.log(`识别结果 ${i}: ${transcript} (isFinal: ${event.results[i].isFinal})`)
            if (event.results[i].isFinal) {
              currentFinalTranscript += transcript
            } else {
              interimTranscript += transcript
            }
          }
          
          console.log('临时转录:', interimTranscript)
          console.log('最终转录:', currentFinalTranscript)
          
          // 直接更新当前识别的文本
          if (interimTranscript) {
            currentTranscriptRef.current = interimTranscript
            console.log('更新当前转录:', interimTranscript)
          }
          
          if (currentFinalTranscript) {
            currentTranscriptRef.current = currentFinalTranscript
            finalTranscriptRef.current = currentFinalTranscript
            console.log('更新最终转录:', currentFinalTranscript)
          }
          
          // 立即调用回调，确保实时更新
          if (onTranscript && typeof onTranscript === 'function') {
            // 临时结果总是调用回调
            if (interimTranscript) {
              console.log('调用onTranscript (临时):', interimTranscript)
              onTranscript(interimTranscript, true, false)
            }
            
            // 最终结果也调用回调
            if (currentFinalTranscript) {
              console.log('调用onTranscript (最终):', currentFinalTranscript)
              onTranscript(currentFinalTranscript, false, true)
            }
          }
        }
        
        // 添加更多事件监听器用于调试
        recognitionRef.current.onstart = () => {
          console.log('语音识别开始')
          setIsRecording(true)
          setIsProcessing(false)
          currentTranscriptRef.current = '' // 重置当前转录
        }
        
        recognitionRef.current.onend = () => {
          console.log('语音识别结束')
          setIsRecording(false)
          setIsProcessing(false)
          
          // 语音识别结束时，确保调用最终结果
          if (onTranscript && typeof onTranscript === 'function' && finalTranscriptRef.current) {
            console.log('语音识别结束，调用最终结果:', finalTranscriptRef.current)
            onTranscript(finalTranscriptRef.current, false, true)
          }
        }
        
        recognitionRef.current.onerror = (event) => {
          console.error('语音识别错误:', event.error)
          setIsRecording(false)
          setIsProcessing(false)
        }
      }
      
      if (recognitionRef.current && !isRecording) {
        console.log('启动语音识别...')
        recognitionRef.current.start()
      }
    } else {
      console.log('浏览器不支持语音识别，尝试后端录音')
      startBackendRecording(onTranscript)
    }
  }, [isRecording, startBackendRecording])

  const stopRecording = useCallback((onTranscript) => {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      stopBrowserRecording(onTranscript)
    } else {
      stopBackendRecording()
    }
  }, [stopBrowserRecording, stopBackendRecording])

  return {
    isRecording,
    isProcessing,
    isSupported,
    startRecording,
    stopRecording
  }
}

export default useVoiceChat