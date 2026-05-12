import { useState, useRef, useCallback } from 'react'

const useVoiceChat = () => {
  const [isRecording, setIsRecording] = useState(false)
  const [isProcessing, setIsProcessing] = useState(false)
  const [isSupported] = useState(() => !!(navigator.mediaDevices?.getUserMedia))

  const mediaRecorderRef = useRef(null)
  const audioChunksRef = useRef([])
  const cancelledRef = useRef(false)

  const startRecording = useCallback(async (onTranscript) => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })

      // Prefer webm/opus (Chrome/Firefox), fall back to default
      const mimeType = MediaRecorder.isTypeSupported('audio/webm;codecs=opus')
        ? 'audio/webm;codecs=opus'
        : MediaRecorder.isTypeSupported('audio/webm')
        ? 'audio/webm'
        : ''

      const mediaRecorder = mimeType
        ? new MediaRecorder(stream, { mimeType })
        : new MediaRecorder(stream)

      audioChunksRef.current = []
      cancelledRef.current = false

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data)
        }
      }

      mediaRecorder.onstop = async () => {
        stream.getTracks().forEach(track => track.stop())

        if (cancelledRef.current) {
          setIsProcessing(false)
          return
        }

        const audioBlob = new Blob(audioChunksRef.current, {
          type: mediaRecorder.mimeType || 'audio/webm'
        })
        audioChunksRef.current = []

        try {
          const formData = new FormData()
          const ext = (mediaRecorder.mimeType || '').includes('webm') ? 'webm' : 'wav'
          formData.append('file', audioBlob, `recording.${ext}`)

          const response = await fetch('/api/voice/transcribe', {
            method: 'POST',
            body: formData
          })

          const result = await response.json()

          if (result.status === 'success' && result.text) {
            onTranscript?.(result.text, false, true)
          } else {
            throw new Error(result.error || '识别失败')
          }
        } catch (error) {
          console.error('语音识别失败:', error)
          alert('语音识别失败，请重试或改用文字输入')
        } finally {
          setIsProcessing(false)
        }
      }

      mediaRecorderRef.current = mediaRecorder
      mediaRecorder.start(100)
      setIsRecording(true)
    } catch (error) {
      console.error('录音失败:', error)
      alert('无法访问麦克风，请检查权限设置')
    }
  }, [])

  const stopRecording = useCallback((onTranscript, cancelled = false) => {
    if (mediaRecorderRef.current && isRecording) {
      cancelledRef.current = cancelled
      mediaRecorderRef.current.stop()
      setIsRecording(false)
      if (!cancelled) setIsProcessing(true)
    }
  }, [isRecording])

  return {
    isRecording,
    isProcessing,
    isSupported,
    startRecording,
    stopRecording
  }
}

export default useVoiceChat
