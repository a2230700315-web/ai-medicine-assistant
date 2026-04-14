import { useState } from 'react'
import { Send, MessageSquare, Bot, User } from 'lucide-react'
import VoiceInput from './components/VoiceInput'

function App() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      role: 'assistant',
      content: '您好！我是您的AI助手。您可以点击麦克风按钮开始语音输入，我会将您的语音转换为文字并回复。'
    }
  ])
  const [input, setInput] = useState('')
  const [isVoiceInput, setIsVoiceInput] = useState(false)

  const handleTranscript = (text, isInterim, isFinal) => {
    setInput(text)
    setIsVoiceInput(!isFinal)
    
    if (isFinal && text.trim()) {
      handleSendMessage(text)
    }
  }

  const handleSendMessage = (messageText = input) => {
    if (!messageText.trim()) return

    const userMessage = {
      id: Date.now(),
      role: 'user',
      content: messageText
    }

    setMessages(prev => [...prev, userMessage])
    setInput('')
    setIsVoiceInput(false)

    setTimeout(() => {
      const assistantMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: `我收到了您的消息："${messageText}"。这是一个语音输入演示，实际应用中可以连接到豆包API进行智能对话。`
      }
      setMessages(prev => [...prev, assistantMessage])
    }, 1000)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 p-4 md:p-8">
      <div className="max-w-4xl mx-auto">
        <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
          <div className="bg-gradient-to-r from-blue-600 to-indigo-600 p-6">
            <div className="flex items-center gap-3">
              <div className="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center">
                <MessageSquare className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold text-white">语音输入演示</h1>
                <p className="text-blue-100 text-sm">使用浏览器原生语音识别功能</p>
              </div>
            </div>
          </div>

          <div className="h-[500px] overflow-y-auto p-6 space-y-4 bg-gray-50">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`flex items-start gap-3 ${
                  message.role === 'user' ? 'flex-row-reverse' : ''
                }`}
              >
                <div className={`w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 ${
                  message.role === 'user'
                    ? 'bg-gradient-to-r from-blue-500 to-indigo-600'
                    : 'bg-gradient-to-r from-green-500 to-emerald-600'
                }`}>
                  {message.role === 'user' ? (
                    <User className="w-5 h-5 text-white" />
                  ) : (
                    <Bot className="w-5 h-5 text-white" />
                  )}
                </div>
                <div
                  className={`max-w-[80%] p-4 rounded-2xl ${
                    message.role === 'user'
                      ? 'bg-gradient-to-r from-blue-500 to-indigo-600 text-white'
                      : 'bg-white border border-gray-200 text-gray-800 shadow-sm'
                  }`}
                >
                  <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
                </div>
              </div>
            ))}
          </div>

          <div className="p-6 bg-white border-t border-gray-200">
            <div className="flex gap-3">
              <div className="flex-1 relative">
                <input
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                  placeholder={isVoiceInput ? '正在识别语音...' : '输入您的回复...'}
                  disabled={isVoiceInput}
                  className={`w-full px-4 py-3 pr-12 border rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all ${
                    isVoiceInput
                      ? 'border-blue-300 bg-blue-50 text-blue-900'
                      : 'border-gray-300'
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
                disabled={false}
              />
              
              <button
                onClick={() => handleSendMessage()}
                disabled={!input.trim() || isVoiceInput}
                className="px-6 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-xl hover:from-blue-600 hover:to-indigo-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
              >
                <Send className="w-4 h-4" />
                发送
              </button>
            </div>
            
            <div className="mt-4 p-4 bg-blue-50 rounded-xl">
              <h3 className="font-semibold text-blue-900 mb-2">使用说明</h3>
              <ul className="text-sm text-blue-800 space-y-1">
                <li>• 点击蓝色麦克风按钮开始录音</li>
                <li>• 说话时会实时显示识别结果</li>
                <li>• 再次点击按钮停止录音并提交</li>
                <li>• 支持中文语音识别</li>
                <li>• 需要浏览器支持 Web Speech API（推荐使用 Chrome）</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App