import { useState, useRef, useEffect } from 'react'
import { Send, MessageSquare, User, Bot, RotateCcw, TrendingUp, AlertCircle } from 'lucide-react'
import ReviewModal from './ReviewModal'
import { saveProgress } from '../utils/progressStorage'
import VoiceHoldButton from './VoiceHoldButton'

function ChatInterface({ onReview, practiceCase, examMode = false }) {
  const [messages, setMessages] = useState([
    {
      id: 1,
      role: 'assistant',
      content: '您好，我是今天的模拟顾客。我最近总是感觉肠胃不舒服，想买点益生菌，但是市面上品牌太多了，不知道该怎么选择。您能给我一些建议吗？'
    }
  ])

  useEffect(() => {
    if (practiceCase) {
      const initialMessage = {
        id: Date.now(),
        role: 'assistant',
        content: `您好，我最近身体不太舒服。${practiceCase.现病史}。${practiceCase.目前用药 ? '目前我正在服用' + practiceCase.目前用药 + '。' : ''}您能给我一些建议吗？`
      }
      setMessages([initialMessage])
    }
  }, [practiceCase])

  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [showReview, setShowReview] = useState(false)
  const [reviewData, setReviewData] = useState(null)
  const [trustScore, setTrustScore] = useState(50)
  const [currentStage, setCurrentStage] = useState('initial')
  const messagesEndRef = useRef(null)

  const handleVoiceTranscript = (transcript, isInterim = false, isFinal = false) => {
    console.log('handleVoiceTranscript 被调用:', { transcript, isInterim, isFinal })
    
    if (transcript && transcript.trim()) {
      // 累积文本而不是覆盖
      setInput(prevInput => {
        let newText = transcript
        
        // 如果是临时结果，替换最后一句
        if (isInterim) {
          const sentences = prevInput.split(/[。！？.!?]/).filter(s => s.trim())
          if (sentences.length > 0) {
            // 保留之前的句子，只替换最后一句
            sentences[sentences.length - 1] = transcript
            newText = sentences.join('。') + '。'
          }
        } else if (isFinal) {
          // 最终结果，添加到现有文本后面
          newText = prevInput ? prevInput + ' ' + transcript : transcript
        }
        
        console.log('设置输入框内容:', newText)
        return newText
      })
      
      // 如果是最终结果，自动发送
      if (isFinal) {
        console.log('检测到最终结果，准备发送消息')
        setTimeout(() => {
          handleSendMessage()
        }, 500)
      }
    }
  }

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  // 输入框自动调整高度
  useEffect(() => {
    const textarea = document.querySelector('textarea')
    if (textarea) {
      textarea.style.height = 'auto'
      textarea.style.height = Math.min(textarea.scrollHeight, 200) + 'px'
    }
  }, [input])

  const parseMetadata = (content) => {
    try {
      console.log('解析内容:', content)
      
      if (!content || content.trim() === '') {
        console.log('内容为空，返回默认')
        return {
          content: '（顾客正在思考，请继续沟通...）',
          trustScore: 50,
          currentStage: 'initial'
        }
      }

      let separator = null
      if (content.includes('@@@')) {
        separator = '@@@'
        console.log('使用 @@@ 分隔符')
      } else if (content.includes('[/METADATA]')) {
        separator = '[/METADATA]'
        console.log('使用 [/METADATA] 分隔符（旧格式）')
      }

      if (!separator) {
        console.log('没有找到分隔符，直接显示内容')
        return {
          content: content.trim(),
          trustScore: 50,
          currentStage: 'initial'
        }
      }

      const parts = content.split(separator)
      console.log('分割后的部分:', parts)
      
      if (parts.length >= 2) {
        const dialogueContent = parts[0].trim()
        const jsonData = parts[1].trim()
        
        console.log('对话内容:', dialogueContent)
        console.log('JSON数据:', jsonData)
        
        let parsedMetadata = { trustScore: 50, currentStage: 'initial' }
        
        try {
          parsedMetadata = JSON.parse(jsonData)
          console.log('解析成功:', parsedMetadata)
        } catch (e) {
          console.error('解析JSON失败:', e, jsonData)
        }
        
        const finalContent = dialogueContent || '（顾客正在思考，请继续沟通...）'
        console.log('最终内容:', finalContent)
        console.log('信任度分数:', parsedMetadata.trust_score)
        console.log('销售阶段:', parsedMetadata.current_stage)
        
        return {
          content: finalContent,
          trustScore: parsedMetadata.trust_score || 50,
          currentStage: parsedMetadata.current_stage || 'initial'
        }
      }
      
      console.log('分割部分不足2个，返回原始内容')
      return { 
        content: content.trim(), 
        trustScore: 50, 
        currentStage: 'initial' 
      }
    } catch (e) {
      console.error('解析元数据失败:', e)
      return { 
        content: content.trim() || '（顾客正在思考，请继续沟通...）', 
        trustScore: 50, 
        currentStage: 'initial' 
      }
    }
  }

  const handleSendMessage = async () => {
    if (!input.trim()) return

    const userMessage = {
      id: Date.now(),
      role: 'user',
      content: input
    }

    setMessages(prev => [...prev, userMessage])
    setInput('')
    setIsLoading(true)

    try {
      const assistantMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: '',
        isStreaming: true
      }
      setMessages(prev => [...prev, assistantMessage])

      await fetchStreamResponse([...messages, userMessage], (metadata) => {
        setTrustScore(metadata.trustScore)
        setCurrentStage(metadata.currentStage)
        setMessages(prev => prev.map(msg => 
          msg.id === assistantMessage.id 
            ? { ...msg, content: metadata.content, isStreaming: false }
            : msg
        ))
      })
    } catch (error) {
      console.error('AI响应错误:', error)
      const errorMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: '抱歉，我暂时无法回应。请检查API配置后重试。'
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const fetchStreamResponse = async (conversationHistory, onComplete) => {
    const filteredMessages = conversationHistory.filter(msg => {
      const content = msg.content || ''
      return !content.includes('[错误:') && 
             !content.includes('抱歉，我暂时无法回应')
    })

    const messages = filteredMessages.map(msg => {
      const content = msg.content || ''
      let cleanContent = content
      if (content.includes('@@@')) {
        cleanContent = content.split('@@@')[0].trim()
      } else if (content.includes('[/METADATA]')) {
        cleanContent = content.split('[/METADATA]')[0].trim()
      }
      return {
        role: msg.role === 'user' ? 'user' : 'assistant',
        content: cleanContent
      }
    })

    const requestBody = {
      messages: messages,
      practice_case: practiceCase || {
        姓名: '模拟顾客',
        年龄: 45,
        BMI: 24.5,
        过敏史: '无',
        现病史: '最近总是感觉肠胃不舒服，想买点益生菌',
        目前用药: '',
        饮食习惯: '饮食不规律',
        销售目标: '成功推荐益生菌产品'
      },
      temperature: 0.8,
      max_tokens: 500,
      difficulty: practiceCase?.difficulty || 'medium'
    }

    console.log('发送到后端的请求体:', requestBody)

    const response = await fetch('/api/chat/stream', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody),
      signal: AbortSignal.timeout(45000) // 45秒超时
    })

    // 先读取响应体内容（只能读取一次）
    const responseText = await response.text()
    
    if (!response.ok) {
      console.error('API 请求失败:', response.status, responseText)
      // 尝试解析错误信息
      try {
        const errorData = JSON.parse(responseText)
        throw new Error(`HTTP error! status: ${response.status}: ${errorData.message || errorData.error || JSON.stringify(errorData)}`)
      } catch (jsonError) {
        // 如果无法解析为JSON，使用原始文本
        throw new Error(`HTTP error! status: ${response.status}: ${responseText}`)
      }
    }

    // 尝试解析JSON响应，如果失败则处理为文本响应
    try {
      const responseData = JSON.parse(responseText)
      console.log('接收到JSON响应:', responseData)
      
      // 检查是否有错误信息
      if (responseData.error) {
        console.error('API返回错误:', responseData)
        throw new Error(`API错误: ${responseData.message || responseData.error}`)
      }
      
      if (responseData && responseData.content) {
        const content = responseData.content
        console.log('提取的内容:', content)
        const parsed = parseMetadata(content)
        onComplete(parsed)
      } else {
        console.error('JSON响应格式错误:', responseData)
        throw new Error('API响应格式错误')
      }
    } catch (jsonError) {
      // 如果JSON解析失败，处理为文本响应
      console.log('JSON解析失败，处理为文本响应:', jsonError.message)
      console.log('接收到文本响应:', responseText)
      
      // 检查文本响应是否包含错误信息
      if (responseText.includes('error') || responseText.includes('Error')) {
        console.error('文本响应包含错误:', responseText)
        throw new Error(`API错误: ${responseText}`)
      }
      
      // 处理正常的文本响应
      const parsed = parseMetadata(responseText)
      onComplete(parsed)
    }
  }

  const handleReview = async () => {
    setIsLoading(true)
    try {
      const review = await fetchReview(messages)
      
      // 根据难度计算倍率
      const difficultyMultiplier = {
        'easy': 1.0,
        'medium': 1.2,
        'hard': 1.5
      }
      const multiplier = difficultyMultiplier[practiceCase?.difficulty || 'medium']
      
      // 应用难度倍率
      const adjustedReview = {
        ...review,
        originalTotalScore: review.totalScore,
        totalScore: Math.min(100, Math.round(review.totalScore * multiplier)),
        difficultyMultiplier: multiplier,
        difficulty: practiceCase?.difficulty || 'medium'
      }
      
      setReviewData(adjustedReview)
      setShowReview(true)
      onReview(adjustedReview)
      
      if (practiceCase && practiceCase.id) {
        saveProgress(practiceCase.id, adjustedReview.totalScore, adjustedReview)
      }
    } catch (error) {
      console.error('复盘分析错误:', error)
      alert('复盘分析失败，请检查API配置')
    } finally {
      setIsLoading(false)
    }
  }

  const fetchReview = async (conversationMessages) => {
    const messages = conversationMessages.map(msg => ({
      role: msg.role === 'user' ? 'user' : 'assistant',
      content: msg.content
    }))

    const response = await fetch('/api/chat/review', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        type: 'review',
        messages: messages,
        practice_case: practiceCase
      })
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    return await response.json()
  }

  const handleReset = () => {
    if (practiceCase) {
      const initialMessage = {
        id: Date.now(),
        role: 'assistant',
        content: `您好，我最近身体不太舒服。${practiceCase.现病史}。${practiceCase.目前用药 ? '目前我正在服用' + practiceCase.目前用药 + '。' : ''}您能给我一些建议吗？`
      }
      setMessages([initialMessage])
    } else {
      setMessages([
        {
          id: 1,
          role: 'assistant',
          content: '您好，我是今天的模拟顾客。我最近总是感觉肠胃不舒服，想买点益生菌，但是市面上品牌太多了，不知道该怎么选择。您能给我一些建议吗？'
        }
      ])
    }
    setShowReview(false)
    setReviewData(null)
    setTrustScore(50)
    setCurrentStage('initial')
  }

  const getStageLabel = (stage) => {
    const stageMap = {
      'initial': '初次接触',
      'inquiry': '询问了解',
      'objection': '提出异议',
      'consideration': '考虑评估',
      'decision': '决定购买',
      'rejection': '拒绝购买'
    }
    return stageMap[stage] || stage
  }

  const getTrustColor = (score) => {
    if (score < 30) return 'bg-red-500'
    if (score < 50) return 'bg-orange-500'
    if (score < 70) return 'bg-yellow-500'
    if (score < 90) return 'bg-green-500'
    return 'bg-emerald-500'
  }

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-gradient-to-r from-blue-400 to-cyan-500 rounded-lg flex items-center justify-center">
            <MessageSquare className="w-5 h-5 text-white" />
          </div>
          <h2 className="text-xl font-bold text-gray-800">模拟对话</h2>
        </div>
        <div className="flex gap-2">
          <button
            onClick={handleReset}
            className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
          >
            <RotateCcw className="w-4 h-4" />
            <span className="text-sm">重新开始</span>
          </button>
          <button
            onClick={handleReview}
            disabled={messages.length < 3 || isLoading}
            className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-green-500 to-emerald-600 text-white rounded-lg hover:from-green-600 hover:to-emerald-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <TrendingUp className="w-4 h-4" />
            <span className="text-sm">复盘分析</span>
          </button>
        </div>
      </div>

      <div className="mb-4 p-4 bg-gradient-to-r from-purple-50 to-pink-50 rounded-lg">
        <div className="flex items-center justify-between mb-2">
          <div className="flex items-center gap-2">
            <span className="text-sm font-medium text-gray-700">顾客满意度</span>
            {trustScore < 30 && (
              <AlertCircle className="w-4 h-4 text-red-500 animate-pulse" />
            )}
          </div>
          <span className={`text-2xl font-bold ${trustScore < 30 ? 'text-red-600' : 'text-purple-600'}`}>
            {trustScore}
          </span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-3">
          <div
            className={`h-3 rounded-full transition-all duration-500 ${getTrustColor(trustScore)}`}
            style={{ width: `${trustScore}%` }}
          />
        </div>
        <div className="mt-2 flex items-center justify-between text-xs text-gray-500">
          <span>当前阶段：{getStageLabel(currentStage)}</span>
          {trustScore < 30 && (
            <span className="text-red-500 font-medium">⚠️ 顾客满意度较低</span>
          )}
        </div>
      </div>

      <div className="flex-1 overflow-y-auto space-y-4 mb-4 p-4 bg-gray-50 rounded-lg">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex items-start gap-3 ${
              message.role === 'user' ? 'flex-row-reverse' : ''
            }`}
          >
            <div className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
              message.role === 'user'
                ? 'bg-gradient-to-r from-blue-500 to-indigo-600'
                : 'bg-gradient-to-r from-orange-400 to-red-500'
            }`}>
              {message.role === 'user' ? (
                <User className="w-4 h-4 text-white" />
              ) : (
                <Bot className="w-4 h-4 text-white" />
              )}
            </div>
            <div
              className={`max-w-[80%] p-4 rounded-2xl ${
                message.role === 'user'
                  ? 'bg-gradient-to-r from-blue-500 to-indigo-600 text-white'
                  : 'bg-white border border-gray-200 text-gray-800'
              }`}
            >
              <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
              {message.isStreaming && (
                <div className="flex gap-1 mt-2">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" />
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }} />
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
                </div>
              )}
            </div>
          </div>
        ))}
        {isLoading && !messages.find(m => m.isStreaming) && (
          <div className="flex items-start gap-3">
            <div className="w-8 h-8 rounded-full flex items-center justify-center bg-gradient-to-r from-orange-400 to-red-500">
              <Bot className="w-4 h-4 text-white" />
            </div>
            <div className="bg-white border border-gray-200 p-4 rounded-2xl">
              <div className="flex gap-1">
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" />
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }} />
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {showReview && reviewData && (
        <ReviewModal 
          reviewData={reviewData} 
          onClose={() => setShowReview(false)} 
        />
      )}

      <div className="flex flex-col sm:flex-row gap-3">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && !e.shiftKey && handleSendMessage()}
          placeholder="输入您的回复..."
          disabled={isLoading}
          className="w-full sm:flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all disabled:opacity-50 resize-none min-h-[60px] max-h-[200px] overflow-y-auto"
          style={{ height: 'auto' }}
          ref={(textarea) => {
            if (textarea) {
              textarea.style.height = 'auto'
              textarea.style.height = Math.min(textarea.scrollHeight, 200) + 'px'
            }
          }}
        />
        <VoiceHoldButton
          onTranscript={handleVoiceTranscript}
          disabled={isLoading}
        />
        <button
          onClick={handleSendMessage}
          disabled={!input.trim() || isLoading}
          className="px-6 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-lg hover:from-blue-600 hover:to-indigo-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
        >
          <Send className="w-4 h-4" />
          发送
        </button>
      </div>
    </div>
  )
}

export default ChatInterface
