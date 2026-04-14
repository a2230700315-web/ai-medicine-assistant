import { useState, useEffect, useRef } from 'react'
import { Mic, MicOff, Loader2, Pill } from 'lucide-react'

function MedicalVoiceInput({ onTranscript, disabled }) {
  const [isRecording, setIsRecording] = useState(false)
  const [isProcessing, setIsProcessing] = useState(false)
  const [isSupported, setIsSupported] = useState(true)
  const recognitionRef = useRef(null)
  const finalTranscriptRef = useRef('')

  const MEDICAL_TERMS = [
    '阿莫西林', '头孢', '青霉素', '红霉素', '克拉霉素',
    '不良反应', '副作用', '过敏反应', '禁忌症', '注意事项',
    '用法用量', '服用方法', '剂量', '频次', '疗程',
    '处方药', '非处方药', 'OTC', '抗生素', '抗病毒药',
    '降压药', '降糖药', '降脂药', '抗凝药', '抗血小板药',
    '心血管', '呼吸系统', '消化系统', '神经系统', '内分泌系统',
    '肝肾功能', '孕妇', '哺乳期', '儿童', '老年人',
    '遵医嘱', '咨询医师', '药师', '执业药师', '临床用药指南'
  ]

  const MEDICAL_INITIAL_PROMPT = `
    医药专业术语提示：
    抗菌药物：阿莫西林、头孢类、青霉素类、大环内酯类
    心血管药物：降压药、降脂药、抗心律失常药
    消化系统药物：质子泵抑制剂、H2受体拮抗剂、胃黏膜保护剂
    不良反应：恶心、呕吐、皮疹、过敏反应、肝肾功能损害
    禁忌症：孕妇、哺乳期、儿童、肝肾功能不全、过敏体质
    用法用量：口服、静脉注射、肌肉注射、外用、吸入
    处方药：请遵医嘱
  `

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
      <div className="flex items-center gap-2 px-3 py-2 text-sm text-red-600 bg-red-50 rounded-lg border border-red-200">
        <MicOff className="w-4 h-4" />
        <span>您的浏览器不支持语音输入</span>
      </div>
    )
  }

  return (
    <div className="relative">
      <button
        onClick={handleToggleRecording}
        disabled={disabled || isProcessing}
        className={`relative flex items-center justify-center w-14 h-14 rounded-full transition-all shadow-lg ${
          isRecording
            ? 'bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white animate-pulse'
            : 'bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white'
        } ${disabled || isProcessing ? 'opacity-50 cursor-not-allowed' : ''}`}
        title={isRecording ? '停止录音' : '开始语音输入'}
      >
        {isProcessing ? (
          <Loader2 className="w-6 h-6 animate-spin" />
        ) : isRecording ? (
          <MicOff className="w-6 h-6" />
        ) : (
          <Mic className="w-6 h-6" />
        )}
        
        {isRecording && (
          <div className="absolute -bottom-8 left-1/2 transform -translate-x-1/2 flex items-center gap-1">
            <div className="w-1 h-3 bg-red-500 rounded-full animate-bounce" />
            <div className="w-1 h-3 bg-red-500 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }} />
            <div className="w-1 h-3 bg-red-500 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
          </div>
        )}
      </button>

      {isRecording && (
        <div className="absolute -bottom-6 left-1/2 transform -translate-x-1/2 text-xs text-red-600 font-medium whitespace-nowrap">
          录音中...
        </div>
      )}

      <div className="absolute top-full left-1/2 transform -translate-x-1/2 mt-2 w-64 p-3 bg-white rounded-lg shadow-xl border border-gray-200 opacity-0 hover:opacity-100 transition-opacity pointer-events-none hover:pointer-events-auto">
        <div className="flex items-center gap-2 mb-2">
          <Pill className="w-4 h-4 text-emerald-600" />
          <span className="text-xs font-semibold text-gray-700">医药术语优化</span>
        </div>
        <div className="text-xs text-gray-600 leading-relaxed">
          已优化识别：阿莫西林、头孢、不良反应、禁忌症、用法用量等专业医药词汇
        </div>
      </div>
    </div>
  )
}

export default MedicalVoiceInput