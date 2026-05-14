import { useCallback } from 'react'
import { Mic, MicOff, Loader2 } from 'lucide-react'
import useVoiceChat from '../hooks/useVoiceChat'

function VoiceHoldButton({ onTranscript, disabled }) {
  const {
    isRecording,
    isProcessing: isVoiceProcessing,
    isSupported: isVoiceSupported,
    startRecording,
    stopRecording
  } = useVoiceChat()

  const handleClick = useCallback(() => {
    if (disabled || isVoiceProcessing) return
    if (isRecording) {
      stopRecording(onTranscript, false)
    } else {
      startRecording(onTranscript)
    }
  }, [disabled, isVoiceProcessing, isRecording, startRecording, stopRecording, onTranscript])

  if (!isVoiceSupported) {
    return (
      <div className="flex items-center gap-2 px-3 py-2 text-sm text-gray-500 bg-gray-100 rounded-lg">
        <MicOff className="w-4 h-4" />
        <span>不支持语音</span>
      </div>
    )
  }

  return (
    <button
      onClick={handleClick}
      disabled={disabled || isVoiceProcessing}
      style={{ WebkitUserSelect: 'none', userSelect: 'none', WebkitTouchCallout: 'none' }}
      className={`relative flex items-center justify-center w-12 h-12 rounded-full transition-all ${
        isRecording
          ? 'bg-red-500 text-white animate-pulse'
          : 'bg-gradient-to-r from-blue-500 to-indigo-600 hover:from-blue-600 hover:to-indigo-700 text-white'
      } ${disabled || isVoiceProcessing ? 'opacity-50 cursor-not-allowed' : ''}`}
      title={isRecording ? '点击停止录音' : '点击开始录音'}
    >
      {isVoiceProcessing ? (
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

export default VoiceHoldButton
