import { useState, useEffect, useRef } from 'react'
import { Mic, MicOff, Loader2 } from 'lucide-react'

function VoiceInput({ onTranscript, disabled }) {
  const [isRecording, setIsRecording] = useState(false)
  const [isProcessing, setIsProcessing] = useState(false)
  const [isSupported, setIsSupported] = useState(true)
  const recognitionRef = useRef(null)
  const finalTranscriptRef = useRef('')

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
      
      if (!SpeechRecognition) {
        setIsSupported(false)
        return
      }

      const recognition = new SpeechRecognition()
      recognition.continuous = true
      recognition.interimResults = true
      recognition.lang = 'zh-CN'

      recognition.onstart = () => {
        setIsRecording(true)
        setIsProcessing(false)
      }

      recognition.onend = () => {
        setIsRecording(false)
        setIsProcessing(false)
      }

      recognition.onerror = (event) => {
        console.error('语音识别错误:', event.error)
        setIsRecording(false)
        setIsProcessing(false)
      }

      recognition.onresult = (event) => {
        let interimTranscript = ''
        let currentFinalTranscript = ''

        for (let i = event.resultIndex; i < event.results.length; i++) {
          const transcript = event.results[i][0].transcript
          if (event.results[i].isFinal) {
            currentFinalTranscript += transcript
          } else {
            interimTranscript += transcript
          }
        }

        if (currentFinalTranscript) {
          finalTranscriptRef.current += currentFinalTranscript
          onTranscript(finalTranscriptRef.current, false)
        } else if (interimTranscript) {
          onTranscript(finalTranscriptRef.current + interimTranscript, true)
        }
      }

      recognitionRef.current = recognition

      return () => {
        if (recognitionRef.current) {
          recognitionRef.current.stop()
        }
      }
    }
  }, [onTranscript])

  const handleStartRecording = () => {
    if (recognitionRef.current && !isRecording) {
      finalTranscriptRef.current = ''
      recognitionRef.current.start()
    }
  }

  const handleStopRecording = () => {
    if (recognitionRef.current && isRecording) {
      recognitionRef.current.stop()
      setIsProcessing(true)
      
      setTimeout(() => {
        setIsProcessing(false)
        onTranscript(finalTranscriptRef.current, false, true)
        finalTranscriptRef.current = ''
      }, 500)
    }
  }

  const handleToggleRecording = () => {
    if (isRecording) {
      handleStopRecording()
    } else {
      handleStartRecording()
    }
  }

  if (!isSupported) {
    return (
      <div className="flex items-center gap-2 px-3 py-2 text-sm text-gray-500 bg-gray-100 rounded-lg">
        <MicOff className="w-4 h-4" />
        <span>您的浏览器不支持语音输入</span>
      </div>
    )
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

export default VoiceInput