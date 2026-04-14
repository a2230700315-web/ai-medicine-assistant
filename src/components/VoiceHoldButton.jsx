import { useState, useRef, useCallback, useEffect } from 'react'
import { Mic, MicOff, Loader2 } from 'lucide-react'
import useVoiceChat from '../hooks/useVoiceChat'
import VoiceRecordingOverlay from './VoiceRecordingOverlay'

function VoiceHoldButton({ onTranscript, disabled }) {
  const {
    isRecording,
    isProcessing: isVoiceProcessing,
    isSupported: isVoiceSupported,
    startRecording,
    stopRecording
  } = useVoiceChat()

  const [isHolding, setIsHolding] = useState(false)
  const [isCancelling, setIsCancelling] = useState(false)
  const [slideDistance, setSlideDistance] = useState(0)
  const [startY, setStartY] = useState(0)
  const [currentY, setCurrentY] = useState(0)
  
  const buttonRef = useRef(null)
  const maxSlideDistance = 100

  const handleStartRecording = useCallback(async (onTranscript) => {
    setIsHolding(true)
    setIsCancelling(false)
    setSlideDistance(0)
    
    try {
      await startRecording(onTranscript)
    } catch (error) {
      console.error('开始录音失败:', error)
      setIsHolding(false)
    }
  }, [startRecording])

  const handleStopRecording = useCallback((onTranscript, shouldSend = true) => {
    if (shouldSend) {
      stopRecording(onTranscript)
    } else {
      // 取消录音，停止录音但不发送结果
      if (isRecording) {
        stopRecording(() => {}) // 传入空回调，不处理结果
      }
    }
    
    setIsHolding(false)
    setIsCancelling(false)
    setSlideDistance(0)
  }, [stopRecording, isRecording])

  const handleMouseDown = useCallback((event) => {
    if (disabled || isVoiceProcessing) return
    
    setStartY(event.clientY)
    setCurrentY(event.clientY)
    handleStartRecording()
  }, [disabled, isVoiceProcessing, handleStartRecording])

  const handleTouchStart = useCallback((event) => {
    if (disabled || isVoiceProcessing) return
    
    const touch = event.touches[0]
    setStartY(touch.clientY)
    setCurrentY(touch.clientY)
    handleStartRecording()
  }, [disabled, isVoiceProcessing, handleStartRecording])

  const handleMouseMove = useCallback((event) => {
    if (!isHolding) return
    
    const deltaY = startY - event.clientY
    setCurrentY(event.clientY)
    setSlideDistance(Math.max(0, deltaY))
    setIsCancelling(deltaY > maxSlideDistance * 0.3)
  }, [isHolding, startY, maxSlideDistance])

  const handleTouchMove = useCallback((event) => {
    if (!isHolding) return
    
    const touch = event.touches[0]
    const deltaY = startY - touch.clientY
    setCurrentY(touch.clientY)
    setSlideDistance(Math.max(0, deltaY))
    setIsCancelling(deltaY > maxSlideDistance * 0.3)
  }, [isHolding, startY, maxSlideDistance])

  const handleMouseUp = useCallback(() => {
    if (!isHolding) return
    
    const shouldSend = slideDistance <= maxSlideDistance * 0.3
    handleStopRecording(onTranscript, shouldSend)
  }, [isHolding, slideDistance, maxSlideDistance, handleStopRecording, onTranscript])

  const handleTouchEnd = useCallback(() => {
    if (!isHolding) return
    
    const shouldSend = slideDistance <= maxSlideDistance * 0.3
    handleStopRecording(onTranscript, shouldSend)
  }, [isHolding, slideDistance, maxSlideDistance, handleStopRecording, onTranscript])

  // 添加全局事件监听器
  useEffect(() => {
    if (isHolding) {
      document.addEventListener('mousemove', handleMouseMove)
      document.addEventListener('mouseup', handleMouseUp)
      document.addEventListener('touchmove', handleTouchMove, { passive: false })
      document.addEventListener('touchend', handleTouchEnd)
    }

    return () => {
      document.removeEventListener('mousemove', handleMouseMove)
      document.removeEventListener('mouseup', handleMouseUp)
      document.removeEventListener('touchmove', handleTouchMove)
      document.removeEventListener('touchend', handleTouchEnd)
    }
  }, [isHolding, handleMouseMove, handleMouseUp, handleTouchMove, handleTouchEnd])

  // 防止默认行为
  const preventDefault = useCallback((event) => {
    event.preventDefault()
  }, [])

  if (!isVoiceSupported) {
    return (
      <div className="flex items-center gap-2 px-3 py-2 text-sm text-gray-500 bg-gray-100 rounded-lg">
        <MicOff className="w-4 h-4" />
        <span>您的浏览器不支持语音输入</span>
      </div>
    )
  }

  return (
    <>
      <button
        ref={buttonRef}
        onMouseDown={handleMouseDown}
        onTouchStart={handleTouchStart}
        onContextMenu={preventDefault}
        disabled={disabled || isVoiceProcessing}
        className={`relative flex items-center justify-center w-12 h-12 rounded-full transition-all ${
          isHolding && !isCancelling
            ? 'bg-red-500 hover:bg-red-600 text-white animate-pulse'
            : 'bg-gradient-to-r from-blue-500 to-indigo-600 hover:from-blue-600 hover:to-indigo-700 text-white'
        } ${disabled || isVoiceProcessing ? 'opacity-50 cursor-not-allowed' : ''}`}
        title="按住说话，上滑取消"
      >
        {isVoiceProcessing ? (
          <Loader2 className="w-5 h-5 animate-spin" />
        ) : isHolding && isCancelling ? (
          <MicOff className="w-5 h-5" />
        ) : (
          <Mic className="w-5 h-5" />
        )}
        
        {isHolding && (
          <span className="absolute -bottom-6 left-1/2 transform -translate-x-1/2 text-xs text-red-500 font-medium whitespace-nowrap">
            录音中...
          </span>
        )}
      </button>

      <VoiceRecordingOverlay
        isVisible={isHolding}
        isRecording={isRecording}
        isCancelling={isCancelling}
        slideDistance={slideDistance}
        maxSlideDistance={maxSlideDistance}
      />
    </>
  )
}

export default VoiceHoldButton