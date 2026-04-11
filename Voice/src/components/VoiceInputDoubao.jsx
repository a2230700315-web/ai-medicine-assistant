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