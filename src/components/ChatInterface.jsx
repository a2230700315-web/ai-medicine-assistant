import { useState, useRef, useEffect, lazy, Suspense } from 'react'
import { Send, MessageSquare, User, Bot, RotateCcw, TrendingUp, AlertCircle, ChevronUp, ChevronDown, ArrowLeftRight } from 'lucide-react'
import { saveProgress } from '../utils/progressStorage'
import VoiceHoldButton from './VoiceHoldButton'

const ReviewModal = lazy(() => import('./ReviewModal'))

function ChatInterface({ onReview, practiceCase, examMode = false }) {
  const [roleMode, setRoleMode] = useState('user') // 'user'=用户扮店员 'ai'=AI扮店员
  const [messages, setMessages] = useState([
    {
      id: 1,
      role: 'assistant',
      content: '你好，我想买点东西，你们有什么可以推荐的吗？'
    }
  ])

  useEffect(() => {
    const opening = roleMode === 'ai'
      ? buildAIStaffOpening(practiceCase)
      : practiceCase ? buildOpeningMessage(practiceCase) : '你好，我想买点东西，你们有什么可以推荐的吗？'
    setMessages([{ id: Date.now(), role: 'assistant', content: opening }])
    setTrustScore(50)
    setCurrentStage('initial')
    setPurchaseIntent(25)
    setShowPurchaseSuccess(false)
  }, [practiceCase, roleMode])

  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [showReview, setShowReview] = useState(false)
  const [reviewData, setReviewData] = useState(null)
  const [trustScore, setTrustScore] = useState(50)
  const [currentStage, setCurrentStage] = useState('initial')
  const [purchaseIntent, setPurchaseIntent] = useState(25)
  const [showStatusBar, setShowStatusBar] = useState(true)
  const [showPurchaseSuccess, setShowPurchaseSuccess] = useState(false)
  const messagesEndRef = useRef(null)

  // 根据案例和难度生成真实感强的顾客开场白
  const buildOpeningMessage = (case_) => {
    if (!case_) {
      return '你好，我想买点东西，你们这边有什么可以推荐的吗？'
    }
    const difficulty = case_.difficulty || 'medium'
    const category = case_.category || ''
    const name = case_.name || '顾客'
    const age = case_.age || ''

    // 按分类生成贴近真实场景的开场白
    const openingsByCategory = {
      高血糖: {
        easy: [
          `你好，我最近查体检血糖有点高，医生说要注意，我想来看看有什么适合我吃的。`,
          `你好，我血糖偏高，想配点降糖的药，应该买哪个？`,
        ],
        medium: [
          `你好，我上次去医院，医生说我空腹血糖${case_.现病史?.match(/\d+\.?\d*mmol/)?.[0] || '偏高'}，让我来药店看看有没有辅助调理的。我现在在吃${case_.目前用药 || '药'}，你们有什么可以搭着用的吗？`,
          `师傅，我想问一下，我血糖控制得不太好，吃了${case_.目前用药 || '降糖药'}感觉效果一般，还有没有别的方案？`,
        ],
        hard: [
          `你好，我糖尿病好几年了，现在在吃${case_.目前用药 || '药'}，最近复查餐后血糖还是高，我听说${Math.random() > 0.5 ? '阿卡波糖' : 'DPP-4抑制剂'}效果不错，你们有卖吗？价格怎么样？`,
          `你这里有${case_.销售目标?.match(/[一-龥A-Za-z-]+(?:抑制剂|类|片|胶囊)/)?.[0] || '联合降糖药'}吗？我自己在网上查了一下，感觉可以试试，但我有${case_.过敏史 !== '无' ? case_.过敏史 + '过敏' : '一些担心'}，你帮我看看行不行？`,
        ]
      },
      高血压: {
        easy: [
          `你好，我最近血压有点高，头有时候会晕，来看看有什么药可以吃。`,
          `你好，我想买点降压药，你们这有什么？`,
        ],
        medium: [
          `你好，我血压${case_.现病史?.match(/\d+\/\d+/)?.[0] || '偏高'}，在吃${case_.目前用药 || '降压药'}，最近感觉控制得不太稳，你有没有什么建议？`,
          `师傅，我老公血压高，一直在吃${case_.目前用药 || '药'}，但有时候还是高，你们有没有可以配合着用的？`,
        ],
        hard: [
          `你好，我吃${case_.目前用药 || 'CCB'}有${case_.现病史?.includes('脚肿') ? '脚肿' : Math.random() > 0.5 ? '脚踝有点肿' : '副作用'}，想换或者加个药，我还有${case_.现病史?.includes('冠心病') ? '冠心病' : '其他问题'}，你看怎么搭配比较好？`,
          `我对${case_.过敏史 !== '无' ? case_.过敏史 : 'ACE抑制剂'}过敏，现在要加强降压方案，你帮我看看有什么合适的替代？`,
        ]
      },
      高血脂: {
        easy: [
          `你好，体检说我血脂高，医生让我来买他汀类的药，你们有什么？`,
          `你好，我胆固醇高，想买点调血脂的，哪个好？`,
        ],
        medium: [
          `你好，我在吃${case_.目前用药 || '他汀药'}，最近复查LDL还是${case_.现病史?.match(/\d+\.?\d*/)?.[0] || '偏高'}，医生让加量，但我有点担心副作用，有没有其他方案？`,
          `师傅，我甘油三酯很高，他汀类对它效果好吗？还是要换别的？`,
        ],
        hard: [
          `你好，我吃他汀吃了半年，最近感觉腿有点酸，是不是肌肉的问题？我要不要停药？有没有别的降脂办法？`,
          `我想问一下，鱼油和他汀可以一起吃吗？我甘油三酯和胆固醇都高，想双管齐下。`,
        ]
      },
      高尿酸: {
        easy: [
          `你好，我上次痛风发作，现在好了，医生说要吃药控制尿酸，买什么？`,
          `你好，我尿酸高，关节有时候会疼，有什么可以吃的药？`,
        ],
        medium: [
          `你好，我上次痛风发了，吃了${case_.目前用药 || '消炎药'}好了，但我尿酸还是${case_.现病史?.match(/\d+/)?.[0] || '高'}，要不要长期吃降尿酸的药？`,
          `师傅，我尿酸高，听说要少吃海鲜啤酒，我平时饮食注意了，但还是高，有没有药可以帮忙？`,
        ],
        hard: [
          `你好，我吃别嘌醇之前皮肤出过疹子，现在要降尿酸，有没有其他选择？我尿酸有${case_.现病史?.match(/\d+/)?.[0] || '500'}多了，肾功能也稍微有点问题。`,
          `痛风发作期能不能直接就用降尿酸药？还是要先消炎？你帮我解释一下怎么个顺序。`,
        ]
      },
      消化内科: {
        easy: [
          `你好，我最近胃不舒服，总是反酸，有没有什么胃药推荐？`,
          `你好，我肠胃不好，老是胀气，买什么药比较好？`,
        ],
        medium: [
          `你好，我有胃食管反流，在吃${case_.目前用药 || '奥美拉唑'}，但效果一般，吃完饭还是会烧心，你们有没有更好的方案？`,
          `师傅，我胃镜查出来有慢性胃炎，幽门螺旋杆菌阳性，医生让我来配三联治疗的药，你帮我看看买什么？`,
        ],
        hard: [
          `你好，我长期吃PPI，最近看到说会影响骨质，是真的吗？有没有替代方案？我反流很严重，不吃就难受。`,
          `我妈妈${age ? age + '岁' : '年纪大了'}，消化不好，经常腹胀腹泻，她还有其他基础病在吃好几种药，有没有消化方面的药可以推荐，不会跟她其他药冲突的？`,
        ]
      },
      中医内科: {
        easy: [
          `你好，我最近总是感觉很累，睡不好，想买点中成药调理一下。`,
          `你好，我体质比较差，容易生病，有没有适合我的调理方案？`,
        ],
        medium: [
          `你好，我${case_.现病史 || '最近总是乏力，手脚发凉'}，中医说我是气虚，你们有什么中成药可以调理？`,
          `师傅，我想买点六味地黄丸，但不知道自己适不适合，你帮我看看？`,
        ],
        hard: [
          `你好，我在吃西药${case_.目前用药 || '降压药'}，想同时配点中药调理，会不会有冲突？怎么搭配比较好？`,
          `我已经在吃好几种中成药了，想再加一个活血化瘀的，有没有需要注意的地方？`,
        ]
      }
    }

    const categoryOpenings = openingsByCategory[category]
    if (categoryOpenings) {
      const pool = categoryOpenings[difficulty] || categoryOpenings['medium']
      return pool[Math.floor(Math.random() * pool.length)]
    }

    // 兜底：通用自然开场
    const generic = {
      easy: `你好，我想买点药，${case_.现病史 ? case_.现病史.slice(0, 30) + '……' : '你帮我推荐一下'}`,
      medium: `你好，我${case_.现病史 || '身体不舒服'}，现在在吃${case_.目前用药 || '一些药'}，你帮我看看有没有合适的。`,
      hard: `你好，我有个问题想咨询一下。${case_.现病史 || ''}。我在网上查了一些资料，但还是不确定，${case_.销售目标 ? '我想了解' + case_.销售目标.slice(0, 20) : '你帮我分析一下'}。`
    }
    return generic[difficulty] || generic['medium']
  }

  const buildAIStaffOpening = (case_) => {
    if (!case_) return '您好，欢迎光临！请问您今天有什么需要帮助的吗？'
    const name = case_.姓名 || '这位顾客'
    const templates = [
      `您好，欢迎光临！请问您今天有什么不舒服，或者有什么需要吗？`,
      `您好！请问您是自己来配药，还是帮家人来的呢？`,
      `您好，欢迎！今天有什么可以帮到您的？是身体有什么不舒服吗？`,
    ]
    return templates[Math.floor(Math.random() * templates.length)]
  }

  const handleVoiceTranscript = (transcript, isInterim = false, isFinal = false) => {
    if (transcript && transcript.trim()) {
      setInput(() => transcript)

      if (isFinal) {
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

  useEffect(() => {
    const textarea = document.querySelector('textarea')
    if (textarea) {
      textarea.style.height = 'auto'
      textarea.style.height = Math.min(textarea.scrollHeight, 200) + 'px'
    }
  }, [input])

  const parseMetadata = (content) => {
    try {
      if (!content || content.trim() === '') {
        return {
          content: '（顾客正在思考，请继续沟通...）',
          trustScore: 50,
          currentStage: 'initial'
        }
      }

      let separator = null
      if (content.includes('@@@')) {
        separator = '@@@'
      } else if (content.includes('[/METADATA]')) {
        separator = '[/METADATA]'
      }

      if (!separator) {
        return {
          content: content.trim(),
          trustScore: 50,
          currentStage: 'initial'
        }
      }

      const parts = content.split(separator)

      if (parts.length >= 2) {
        const dialogueContent = parts[0].trim()
        const jsonData = parts[1].trim()

        let parsedMetadata = { trustScore: 50, currentStage: 'initial' }

        try {
          parsedMetadata = JSON.parse(jsonData)
        } catch (e) {
          console.error('解析JSON失败:', e, jsonData)
        }

        return {
          content: dialogueContent || '（顾客正在思考，请继续沟通...）',
          trustScore: parsedMetadata.trust_score || 50,
          currentStage: parsedMetadata.current_stage || 'initial',
          purchaseIntent: parsedMetadata.purchase_intent || 25
        }
      }

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

      await fetchStreamResponse(
        [...messages, userMessage],
        (partialContent) => {
          // 流式更新：每收到一段文字就更新气泡内容
          const displayContent = partialContent.includes('@@@')
            ? partialContent.split('@@@')[0]
            : partialContent.includes('[/METADATA]')
            ? partialContent.split('[/METADATA]')[0]
            : partialContent
          setMessages(prev => prev.map(msg =>
            msg.id === assistantMessage.id
              ? { ...msg, content: displayContent }
              : msg
          ))
        },
        (metadata) => {
          setTrustScore(metadata.trustScore)
          setCurrentStage(metadata.currentStage)
          setPurchaseIntent(metadata.purchaseIntent)
          setMessages(prev => prev.map(msg =>
            msg.id === assistantMessage.id
              ? { ...msg, content: metadata.content, isStreaming: false }
              : msg
          ))
          if (metadata.purchaseIntent >= 85 || metadata.currentStage === 'purchase') {
            setShowPurchaseSuccess(true)
          }
        }
      )
    } catch (error) {
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

  const fetchStreamResponse = async (conversationHistory, onChunk, onComplete) => {
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

    const difficultyConfig = {
      easy: {
        desc: '简单顾客：性格温和配合，对医药知识了解少，容易被引导，不太会主动提出质疑，推荐什么基本会接受，偶尔问问价格',
        trust_base: 60,
        intent_base: 40
      },
      medium: {
        desc: '普通顾客：有一定主见，会询问效果和副作用，有时会说"让我再想想"或比较价格，需要店员耐心解释才会信任',
        trust_base: 45,
        intent_base: 25
      },
      hard: {
        desc: '困难顾客：自己查过资料，有既定想法，容易质疑推荐，可能提出挑战性问题（副作用、价格贵、药效存疑），需要专业、有说服力的回答才会改变主意',
        trust_base: 30,
        intent_base: 15
      }
    }
    const dc = difficultyConfig[practiceCase?.difficulty || 'medium']

    const requestBody = {
      messages: messages,
      practice_case: practiceCase || {
        category: '通用',
        name: '模拟顾客',
        age: 45,
        过敏史: '无',
        现病史: '最近肠胃不舒服',
        目前用药: '',
        饮食习惯: '饮食不规律',
        销售目标: '推荐消化类产品'
      },
      difficulty: practiceCase?.difficulty || 'medium',
      difficulty_description: dc.desc,
      role_mode: roleMode,
      temperature: 0.85,
      max_tokens: 400
    }

    const response = await fetch('/api/chat/stream', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(requestBody),
      signal: AbortSignal.timeout(45000)
    })

    if (!response.ok) {
      const text = await response.text()
      throw new Error(`HTTP error! status: ${response.status}: ${text}`)
    }

    const reader = response.body.getReader()
    const decoder = new TextDecoder()
    let buffer = ''
    let fullContent = ''

    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      buffer += decoder.decode(value, { stream: true })
      const lines = buffer.split('\n')
      buffer = lines.pop()
      for (const line of lines) {
        if (!line.startsWith('data: ')) continue
        const dataStr = line.slice(6)
        try {
          const data = JSON.parse(dataStr)
          if (data.error) throw new Error(data.error)
          if (data.delta) {
            fullContent += data.delta
            onChunk(fullContent)
          }
          if (data.done) {
            const parsed = parseMetadata(data.content)
            onComplete(parsed)
          }
        } catch (e) {
          if (e.message && !e.message.includes('JSON')) throw e
        }
      }
    }
  }

  const handleReview = async () => {
    setIsLoading(true)
    try {
      const review = await fetchReview(messages)
      
      const difficultyMultiplier = {
        'easy': 1.0,
        'medium': 1.2,
        'hard': 1.5
      }
      const multiplier = difficultyMultiplier[practiceCase?.difficulty || 'medium']
      
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
    const opening = roleMode === 'ai'
      ? buildAIStaffOpening(practiceCase)
      : practiceCase ? buildOpeningMessage(practiceCase) : '你好，我想买点东西，你们有什么可以推荐的吗？'
    setMessages([{ id: Date.now(), role: 'assistant', content: opening }])
    setShowReview(false)
    setReviewData(null)
    setTrustScore(50)
    setCurrentStage('initial')
    setPurchaseIntent(25)
    setShowPurchaseSuccess(false)
  }

  const getStageLabel = (stage) => {
    const stageMap = {
      'initial': '初次接触',
      'interest': '产生兴趣',
      'inquiry': '询问了解',
      'objection': '提出异议',
      'consideration': '考虑评估',
      'decision': '决定购买',
      'purchase': '完成购买',
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
    <div className="bg-white md:rounded-xl md:shadow-lg md:p-6 h-full flex flex-col pb-14 md:pb-0">
      <div className="hidden md:flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-gradient-to-r from-blue-400 to-cyan-500 rounded-lg flex items-center justify-center">
            <MessageSquare className="w-5 h-5 text-white" />
          </div>
          <h2 className="text-xl font-bold text-gray-800">模拟对话</h2>
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => setRoleMode(m => m === 'user' ? 'ai' : 'user')}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all text-sm ${
              roleMode === 'ai'
                ? 'bg-gradient-to-r from-amber-400 to-orange-500 text-white shadow-sm'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
            title={roleMode === 'ai' ? '当前：AI示范店员模式' : '当前：练习模式'}
          >
            <ArrowLeftRight className="w-4 h-4" />
            <span>{roleMode === 'ai' ? 'AI示范店员' : '练习模式'}</span>
          </button>
          <button
            onClick={handleReset}
            className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
          >
            <RotateCcw className="w-4 h-4" />
            <span className="text-sm">重新开始</span>
          </button>
          {roleMode === 'user' && (
          <button
            onClick={handleReview}
            disabled={messages.length < 3 || isLoading}
            className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-green-500 to-emerald-600 text-white rounded-lg hover:from-green-600 hover:to-emerald-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <TrendingUp className="w-4 h-4" />
            <span className="text-sm">复盘分析</span>
          </button>
          )}
        </div>
      </div>

      {roleMode === 'user' && (
      <div className={`mb-4 p-3 md:p-4 bg-gradient-to-r from-purple-50 to-pink-50 rounded-lg ${showStatusBar ? '' : 'hidden md:block'}`}>
        {showPurchaseSuccess && (
          <div className="mb-3 p-3 bg-gradient-to-r from-green-100 to-emerald-100 rounded-lg border border-green-200">
            <div className="flex items-center gap-2">
              <span className="text-2xl">🎉</span>
              <div>
                <p className="text-green-700 font-bold">销售成功！</p>
                <p className="text-green-600 text-sm">顾客决定购买您推荐的产品</p>
              </div>
            </div>
          </div>
        )}
        <div className="grid grid-cols-2 gap-4">
          <div>
            <div className="flex items-center justify-between mb-1">
              <span className="text-sm font-medium text-gray-700">顾客满意度</span>
              {trustScore < 30 && (
                <AlertCircle className="w-4 h-4 text-red-500 animate-pulse" />
              )}
            </div>
            <div className="flex items-center gap-2 mb-1">
              <span className={`text-xl font-bold ${trustScore < 30 ? 'text-red-600' : 'text-purple-600'}`}>
                {trustScore}
              </span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className={`h-2 rounded-full transition-all duration-500 ${getTrustColor(trustScore)}`}
                style={{ width: `${trustScore}%` }}
              />
            </div>
          </div>
          <div>
            <div className="flex items-center justify-between mb-1">
              <span className="text-sm font-medium text-gray-700">购买意向</span>
              {purchaseIntent >= 70 && (
                <span className="text-xs text-green-500">✓ 接近成交</span>
              )}
            </div>
            <div className="flex items-center gap-2 mb-1">
              <span className={`text-xl font-bold ${purchaseIntent >= 70 ? 'text-green-600' : purchaseIntent >= 50 ? 'text-yellow-600' : 'text-gray-600'}`}>
                {purchaseIntent}
              </span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className={`h-2 rounded-full transition-all duration-500 ${purchaseIntent >= 85 ? 'bg-green-500' : purchaseIntent >= 70 ? 'bg-emerald-400' : purchaseIntent >= 50 ? 'bg-yellow-400' : 'bg-gray-400'}`}
                style={{ width: `${purchaseIntent}%` }}
              />
            </div>
          </div>
        </div>
        <div className="mt-3 flex items-center justify-between text-xs text-gray-500">
          <span>当前阶段：{getStageLabel(currentStage)}</span>
          <button 
            onClick={() => setShowStatusBar(!showStatusBar)}
            className="md:hidden p-1 text-gray-400"
          >
            <ChevronDown className="w-4 h-4" />
          </button>
        </div>
      </div>
      )}

      {roleMode === 'user' && !showStatusBar && (
        <button
          onClick={() => setShowStatusBar(true)}
          className="md:hidden mb-2 p-2 bg-purple-50 rounded-lg flex items-center justify-center gap-2 text-purple-600"
        >
          <ChevronUp className="w-4 h-4" />
          <span className="text-sm">显示状态栏</span>
        </button>
      )}

      {roleMode === 'ai' && (
        <div className="mb-3 px-3 py-2 bg-amber-50 border border-amber-200 rounded-lg flex items-center gap-2 text-sm text-amber-700">
          <ArrowLeftRight className="w-4 h-4 flex-shrink-0" />
          <span>AI示范店员模式：你扮演顾客，观察专业店员如何问诊和推荐</span>
        </div>
      )}

      <div className="flex-1 overflow-y-auto space-y-3 md:space-y-4 mb-4 p-3 md:p-4 bg-gray-50 rounded-lg">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex items-start gap-2 md:gap-3 ${
              message.role === 'user' ? 'flex-row-reverse' : ''
            }`}
          >
            <div className={`w-7 h-7 md:w-8 md:h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
              message.role === 'user'
                ? roleMode === 'ai'
                  ? 'bg-gradient-to-r from-orange-400 to-red-500'
                  : 'bg-gradient-to-r from-blue-500 to-indigo-600'
                : roleMode === 'ai'
                  ? 'bg-gradient-to-r from-green-500 to-emerald-600'
                  : 'bg-gradient-to-r from-orange-400 to-red-500'
            }`}>
              {message.role === 'user' ? (
                <User className="w-3.5 h-3.5 md:w-4 md:h-4 text-white" />
              ) : (
                <Bot className="w-3.5 h-3.5 md:w-4 md:h-4 text-white" />
              )}
            </div>
            <div
              className={`max-w-[85%] md:max-w-[80%] p-3 md:p-4 rounded-2xl ${
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
          <div className="flex items-start gap-2 md:gap-3">
            <div className="w-7 h-7 md:w-8 md:h-8 rounded-full flex items-center justify-center bg-gradient-to-r from-orange-400 to-red-500">
              <Bot className="w-3.5 h-3.5 md:w-4 md:h-4 text-white" />
            </div>
            <div className="bg-white border border-gray-200 p-3 md:p-4 rounded-2xl">
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
        <Suspense fallback={null}>
          <ReviewModal
            reviewData={reviewData}
            onClose={() => setShowReview(false)}
          />
        </Suspense>
      )}

      <div className="flex flex-col md:flex-row gap-2 md:gap-3">
        <div className="flex gap-2">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && !e.shiftKey && handleSendMessage()}
            placeholder="输入您的回复..."
            disabled={isLoading}
            className="flex-1 px-3 md:px-4 py-2 md:py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all disabled:opacity-50 resize-none min-h-[44px] max-h-[120px] md:max-h-[200px] overflow-y-auto text-sm md:text-base"
            style={{ height: 'auto' }}
            ref={(textarea) => {
              if (textarea) {
                textarea.style.height = 'auto'
                textarea.style.height = Math.min(textarea.scrollHeight, window.innerWidth < 768 ? 120 : 200) + 'px'
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
            className="px-4 md:px-6 py-2 md:py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-lg hover:from-blue-600 hover:to-indigo-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
          >
            <Send className="w-4 h-4" />
          </button>
        </div>
        <div className="flex gap-2 md:hidden">
          <button
            onClick={() => setRoleMode(m => m === 'user' ? 'ai' : 'user')}
            className={`flex-1 flex items-center justify-center gap-2 px-3 py-2 rounded-lg text-sm ${
              roleMode === 'ai'
                ? 'bg-gradient-to-r from-amber-400 to-orange-500 text-white'
                : 'bg-gray-100 text-gray-700'
            }`}
          >
            <ArrowLeftRight className="w-4 h-4" />
            <span>{roleMode === 'ai' ? 'AI示范' : '练习'}</span>
          </button>
          <button
            onClick={handleReset}
            className="flex-1 flex items-center justify-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg"
          >
            <RotateCcw className="w-4 h-4" />
            <span className="text-sm">重新开始</span>
          </button>
          {roleMode === 'user' && (
          <button
            onClick={handleReview}
            disabled={messages.length < 3 || isLoading}
            className="flex-1 flex items-center justify-center gap-2 px-4 py-2 bg-gradient-to-r from-green-500 to-emerald-600 text-white rounded-lg disabled:opacity-50"
          >
            <TrendingUp className="w-4 h-4" />
            <span className="text-sm">复盘分析</span>
          </button>
          )}
        </div>
      </div>
    </div>
  )
}

export default ChatInterface
