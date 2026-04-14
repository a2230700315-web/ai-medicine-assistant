import { useState, useEffect } from 'react'
import { Mic, MicOff } from 'lucide-react'

function VoiceRecordingOverlay({ 
  isVisible, 
  isRecording, 
  isCancelling, 
  slideDistance = 0,
  maxSlideDistance = 100 
}) {
  const [showAnimation, setShowAnimation] = useState(false)

  useEffect(() => {
    if (isVisible) {
      setShowAnimation(true)
    } else {
      const timer = setTimeout(() => setShowAnimation(false), 300)
      return () => clearTimeout(timer)
    }
  }, [isVisible])

  if (!showAnimation) return null

  const slidePercentage = Math.min(slideDistance / maxSlideDistance, 1)
  const isCancelled = slidePercentage > 0.3

  return (
    <div className={`fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 transition-opacity duration-300 ${
      isVisible ? 'opacity-100' : 'opacity-0'
    }`}>
      <div className={`bg-white rounded-2xl p-8 shadow-2xl transform transition-all duration-300 ${
        isVisible ? 'scale-100 opacity-100' : 'scale-95 opacity-0'
      }`}>
        <div className="flex flex-col items-center space-y-4">
          {/* 录音图标 */}
          <div className={`relative w-20 h-20 rounded-full flex items-center justify-center transition-all duration-300 ${
            isCancelled 
              ? 'bg-red-100 text-red-600' 
              : 'bg-blue-100 text-blue-600'
          }`}>
            {isCancelled ? (
              <MicOff className="w-10 h-10" />
            ) : (
              <Mic className="w-10 h-10" />
            )}
            
            {/* 录音波纹动画 */}
            {isRecording && !isCancelled && (
              <>
                <div className="absolute inset-0 rounded-full bg-blue-200 animate-ping opacity-75" />
                <div className="absolute inset-0 rounded-full bg-blue-300 animate-ping opacity-50" style={{ animationDelay: '0.5s' }} />
              </>
            )}
          </div>

          {/* 提示文字 */}
          <div className="text-center">
            <p className={`text-lg font-medium transition-colors duration-300 ${
              isCancelled ? 'text-red-600' : 'text-gray-800'
            }`}>
              {isCancelled ? '松开取消' : '正在录音，上滑取消'}
            </p>
            <p className="text-sm text-gray-500 mt-2">
              滑动距离: {Math.round(slidePercentage * 100)}%
            </p>
          </div>

          {/* 滑动指示器 */}
          <div className="w-32 h-2 bg-gray-200 rounded-full overflow-hidden">
            <div 
              className={`h-full transition-all duration-200 ${
                isCancelled ? 'bg-red-500' : 'bg-blue-500'
              }`}
              style={{ width: `${slidePercentage * 100}%` }}
            />
          </div>

          {/* 取消区域指示 */}
          <div className="flex items-center space-x-2 text-sm text-gray-500">
            <div className="w-4 h-4 border-2 border-gray-300 rounded-full">
              <div className={`w-full h-full rounded-full transition-all ${
                isCancelled ? 'bg-red-500' : 'bg-transparent'
              }`} />
            </div>
            <span>取消区域</span>
          </div>
        </div>
      </div>
    </div>
  )
}

export default VoiceRecordingOverlay