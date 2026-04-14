import React, { useState, useEffect, useCallback } from 'react'
import { 
  CheckCircle, XCircle, ArrowRight, Play, BookOpen, Clock, 
  Target, Brain, Zap, TrendingUp, Award, RefreshCw,
  ChevronRight, Timer, AlertCircle, Star, Flame
} from 'lucide-react'
import { examCategories } from '../data/examQuestions'
import {
  generateMockPaper,
  generateWeaknessPaper,
  generateReviewPaper,
  getDailyReviewQuestions,
  analyzeUserWeakness,
  getHeatLabel,
  saveExamRecord,
  getExamRecords,
  getUserRecordsByCategory
} from '../data/mockExamService'

function PracticeExam({ onBack }) {
  const [view, setView] = useState('menu')
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [examMode, setExamMode] = useState(null)
  const [questions, setQuestions] = useState([])
  const [metadata, setMetadata] = useState(null)
  const [currentIndex, setCurrentIndex] = useState(0)
  const [answers, setAnswers] = useState({})
  const [showExplanation, setShowExplanation] = useState(false)
  const [isSubmitted, setIsSubmitted] = useState(false)
  const [timeLeft, setTimeLeft] = useState(0)
  const [isTimerRunning, setIsTimerRunning] = useState(false)
  const [quickMode, setQuickMode] = useState(false)
  const [weaknessAnalysis, setWeaknessAnalysis] = useState(null)
  const [dailyReviews, setDailyReviews] = useState([])

  useEffect(() => {
    if (isTimerRunning && timeLeft > 0) {
      const timer = setInterval(() => {
        setTimeLeft(prev => {
          if (prev <= 1) {
            setIsTimerRunning(false)
            handleSubmit()
            return 0
          }
          return prev - 1
        })
      }, 1000)
      return () => clearInterval(timer)
    }
  }, [isTimerRunning, timeLeft])

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
  }

  const handleCategorySelect = (category) => {
    setSelectedCategory(category)
    const records = getUserRecordsByCategory(category.id)
    const analysis = analyzeUserWeakness(records, category.id)
    setWeaknessAnalysis(analysis)
    const reviews = getDailyReviewQuestions(records, category.id)
    setDailyReviews(reviews)
    setView('mode')
  }

  const handleModeSelect = (mode) => {
    setExamMode(mode)
    setCurrentIndex(0)
    setAnswers({})
    setShowExplanation(false)
    setIsSubmitted(false)
    setQuickMode(mode === 'quick')

    let result
    const records = getUserRecordsByCategory(selectedCategory.id)

    switch (mode) {
      case 'mock':
        result = generateMockPaper(selectedCategory.id, {
          totalQuestions: 120,
          timeLimit: 120
        })
        setTimeLeft(120 * 60)
        setIsTimerRunning(true)
        break
      case 'weakness':
        result = generateWeaknessPaper(records, selectedCategory.id, {
          totalQuestions: 20
        })
        setTimeLeft(30 * 60)
        setIsTimerRunning(true)
        break
      case 'review':
        result = generateReviewPaper(records, selectedCategory.id, {
          totalQuestions: 20
        })
        setTimeLeft(30 * 60)
        setIsTimerRunning(true)
        break
      case 'quick':
        result = generateMockPaper(selectedCategory.id, {
          totalQuestions: 30,
          timeLimit: 0
        })
        setTimeLeft(0)
        setIsTimerRunning(false)
        break
      default:
        result = generateMockPaper(selectedCategory.id, { totalQuestions: 30 })
    }

    setQuestions(result.questions)
    setMetadata(result.metadata)
    setView('exam')
  }

  const handleAnswerSelect = (answer) => {
    if (isSubmitted && !quickMode) return
    
    const currentQuestion = questions[currentIndex]
    const newAnswers = { ...answers, [currentQuestion.id]: answer }
    setAnswers(newAnswers)

    if (quickMode) {
      setShowExplanation(true)
    }
  }

  const handleNext = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(prev => prev + 1)
      setShowExplanation(false)
    }
  }

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(prev => prev - 1)
      setShowExplanation(false)
    }
  }

  const handleJumpTo = (index) => {
    setCurrentIndex(index)
    setShowExplanation(false)
  }

  const handleSubmit = useCallback(() => {
    setIsTimerRunning(false)
    setIsSubmitted(true)
    
    const results = questions.map(q => ({
      ...q,
      userAnswer: answers[q.id] || '',
      isCorrect: answers[q.id] === q.answer
    }))

    const correctCount = results.filter(r => r.isCorrect).length
    const totalScore = results.reduce((sum, r) => sum + (r.isCorrect ? r.points : 0), 0)

    saveExamRecord({
      categoryId: selectedCategory.id,
      categoryName: selectedCategory.name,
      mode: examMode,
      questions: results,
      score: totalScore,
      correctCount,
      totalQuestions: questions.length,
      timeSpent: (metadata?.timeLimit * 60 || 0) - timeLeft
    })
  }, [questions, answers, selectedCategory, examMode, metadata, timeLeft])

  const handleRestart = () => {
    setCurrentIndex(0)
    setAnswers({})
    setShowExplanation(false)
    setIsSubmitted(false)
    if (metadata?.timeLimit) {
      setTimeLeft(metadata.timeLimit * 60)
      setIsTimerRunning(true)
    }
  }

  const handleBackToMenu = () => {
    setView('menu')
    setSelectedCategory(null)
    setExamMode(null)
    setQuestions([])
    setMetadata(null)
    setIsTimerRunning(false)
  }

  const currentQuestion = questions[currentIndex]
  const progress = questions.length > 0 ? ((currentIndex + 1) / questions.length) * 100 : 0

  if (view === 'menu') {
    return (
      <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-gradient-to-r from-purple-500 to-indigo-600 rounded-full flex items-center justify-center">
              <Target className="w-6 h-6 text-white" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-gray-800">模拟考场</h2>
              <p className="text-sm text-gray-500">全真模拟 · 智能提分 · 高效备考</p>
            </div>
          </div>
          <button
            onClick={onBack}
            className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
          >
            <ArrowRight className="w-4 h-4 rotate-180" />
            <span className="text-sm">返回</span>
          </button>
        </div>

        <div className="flex-1 overflow-y-auto">
          <div className="mb-6">
            <h3 className="text-lg font-semibold text-gray-800 mb-4 flex items-center gap-2">
              <BookOpen className="w-5 h-5 text-indigo-600" />
              选择考试科目
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {examCategories.map((category) => (
                <div
                  key={category.id}
                  onClick={() => handleCategorySelect(category)}
                  className="p-4 rounded-xl cursor-pointer transition-all hover:scale-105 border-2 border-transparent hover:border-indigo-300"
                  style={{ backgroundColor: category.color + '15' }}
                >
                  <div className="flex items-center gap-3">
                    <div className="text-3xl">{category.icon}</div>
                    <div>
                      <h4 className="font-semibold text-gray-800">{category.shortName}</h4>
                      <p className="text-xs text-gray-500">{category.totalQuestions} 题</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-xl p-6">
            <h3 className="text-lg font-semibold text-gray-800 mb-4 flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-purple-600" />
              备考建议
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-white rounded-lg p-4">
                <div className="flex items-center gap-2 mb-2">
                  <Clock className="w-5 h-5 text-blue-500" />
                  <span className="font-medium">考前冲刺</span>
                </div>
                <p className="text-sm text-gray-600">120分钟全真模拟，体验真实考场节奏</p>
              </div>
              <div className="bg-white rounded-lg p-4">
                <div className="flex items-center gap-2 mb-2">
                  <Brain className="w-5 h-5 text-purple-500" />
                  <span className="font-medium">弱项强化</span>
                </div>
                <p className="text-sm text-gray-600">智能分析错题，精准攻克薄弱环节</p>
              </div>
              <div className="bg-white rounded-lg p-4">
                <div className="flex items-center gap-2 mb-2">
                  <Zap className="w-5 h-5 text-yellow-500" />
                  <span className="font-medium">速记模式</span>
                </div>
                <p className="text-sm text-gray-600">即选即看解析，碎片时间高效刷题</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (view === 'mode') {
    const hasWeakness = weaknessAnalysis?.weaknessPoints?.length > 0
    const hasReview = dailyReviews?.length > 0

    return (
      <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-3">
            <button
              onClick={() => setView('menu')}
              className="p-2 hover:bg-gray-100 rounded-lg transition-all"
            >
              <ArrowRight className="w-5 h-5 rotate-180 text-gray-600" />
            </button>
            <div>
              <h2 className="text-xl font-bold text-gray-800">{selectedCategory.name}</h2>
              <p className="text-sm text-gray-500">选择考试模式</p>
            </div>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
            <div
              onClick={() => handleModeSelect('mock')}
              className="p-6 rounded-xl cursor-pointer transition-all hover:scale-105 bg-gradient-to-br from-blue-50 to-indigo-100 border-2 border-transparent hover:border-blue-400"
            >
              <div className="flex items-center gap-4 mb-4">
                <div className="w-14 h-14 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-xl flex items-center justify-center">
                  <Award className="w-7 h-7 text-white" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-gray-800">考前冲刺模考</h3>
                  <p className="text-sm text-gray-500">全真模拟 · 120分钟</p>
                </div>
              </div>
              <div className="space-y-2 text-sm text-gray-600">
                <div className="flex items-center gap-2">
                  <CheckCircle className="w-4 h-4 text-green-500" />
                  <span>120道题目，严格按真题比例组卷</span>
                </div>
                <div className="flex items-center gap-2">
                  <CheckCircle className="w-4 h-4 text-green-500" />
                  <span>120分钟限时，模拟真实考场</span>
                </div>
                <div className="flex items-center gap-2">
                  <CheckCircle className="w-4 h-4 text-green-500" />
                  <span>知识点覆盖率80%以上</span>
                </div>
              </div>
            </div>

            <div
              onClick={() => hasWeakness && handleModeSelect('weakness')}
              className={`p-6 rounded-xl cursor-pointer transition-all hover:scale-105 border-2 ${
                hasWeakness 
                  ? 'bg-gradient-to-br from-purple-50 to-pink-100 hover:border-purple-400' 
                  : 'bg-gray-100 opacity-60 cursor-not-allowed'
              }`}
            >
              <div className="flex items-center gap-4 mb-4">
                <div className={`w-14 h-14 rounded-xl flex items-center justify-center ${
                  hasWeakness ? 'bg-gradient-to-r from-purple-500 to-pink-600' : 'bg-gray-400'
                }`}>
                  <Brain className="w-7 h-7 text-white" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-gray-800">智能弱项强化</h3>
                  <p className="text-sm text-gray-500">精准提分 · 30分钟</p>
                </div>
              </div>
              {hasWeakness ? (
                <div className="space-y-2">
                  <p className="text-sm text-gray-600 mb-2">基于您的错题分析，重点攻克：</p>
                  {weaknessAnalysis.weaknessPoints.slice(0, 3).map((w, i) => (
                    <div key={i} className="flex items-center gap-2 text-sm">
                      <AlertCircle className="w-4 h-4 text-red-500" />
                      <span className="text-gray-700">{w.point}</span>
                      <span className="text-red-500 font-medium">({w.errorRate}%错误率)</span>
                    </div>
                  ))}
                </div>
              ) : (
                <p className="text-sm text-gray-500">暂无错题数据，请先完成真题练习</p>
              )}
            </div>

            <div
              onClick={() => hasReview && handleModeSelect('review')}
              className={`p-6 rounded-xl cursor-pointer transition-all hover:scale-105 border-2 ${
                hasReview 
                  ? 'bg-gradient-to-br from-orange-50 to-yellow-100 hover:border-orange-400' 
                  : 'bg-gray-100 opacity-60 cursor-not-allowed'
              }`}
            >
              <div className="flex items-center gap-4 mb-4">
                <div className={`w-14 h-14 rounded-xl flex items-center justify-center ${
                  hasReview ? 'bg-gradient-to-r from-orange-500 to-yellow-500' : 'bg-gray-400'
                }`}>
                  <RefreshCw className="w-7 h-7 text-white" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-gray-800">记忆曲线复习</h3>
                  <p className="text-sm text-gray-500">错题重做 · 30分钟</p>
                </div>
              </div>
              {hasReview ? (
                <div className="space-y-2 text-sm text-gray-600">
                  <div className="flex items-center gap-2">
                    <CheckCircle className="w-4 h-4 text-green-500" />
                    <span>今日待复习错题：{dailyReviews.length}道</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <CheckCircle className="w-4 h-4 text-green-500" />
                    <span>按艾宾浩斯遗忘曲线智能推送</span>
                  </div>
                </div>
              ) : (
                <p className="text-sm text-gray-500">暂无待复习错题</p>
              )}
            </div>

            <div
              onClick={() => handleModeSelect('quick')}
              className="p-6 rounded-xl cursor-pointer transition-all hover:scale-105 bg-gradient-to-br from-green-50 to-emerald-100 border-2 border-transparent hover:border-green-400"
            >
              <div className="flex items-center gap-4 mb-4">
                <div className="w-14 h-14 bg-gradient-to-r from-green-500 to-emerald-600 rounded-xl flex items-center justify-center">
                  <Zap className="w-7 h-7 text-white" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-gray-800">速记模式</h3>
                  <p className="text-sm text-gray-500">即选即看 · 无限时间</p>
                </div>
              </div>
              <div className="space-y-2 text-sm text-gray-600">
                <div className="flex items-center gap-2">
                  <CheckCircle className="w-4 h-4 text-green-500" />
                  <span>点击选项立即显示正误和解析</span>
                </div>
                <div className="flex items-center gap-2">
                  <CheckCircle className="w-4 h-4 text-green-500" />
                  <span>适合碎片时间快速刷题</span>
                </div>
                <div className="flex items-center gap-2">
                  <CheckCircle className="w-4 h-4 text-green-500" />
                  <span>像刷抖音一样背题</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (view === 'exam' && !isSubmitted) {
    return (
      <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-4">
            <button
              onClick={() => {
                setIsTimerRunning(false)
                setView('mode')
              }}
              className="p-2 hover:bg-gray-100 rounded-lg transition-all"
            >
              <ArrowRight className="w-5 h-5 rotate-180 text-gray-600" />
            </button>
            <div>
              <h2 className="text-lg font-bold text-gray-800">
                {examMode === 'mock' ? '考前冲刺模考' : 
                 examMode === 'weakness' ? '智能弱项强化' :
                 examMode === 'review' ? '记忆曲线复习' : '速记模式'}
              </h2>
              <p className="text-sm text-gray-500">{selectedCategory.name}</p>
            </div>
          </div>
          
          <div className="flex items-center gap-4">
            {metadata?.timeLimit > 0 && (
              <div className={`flex items-center gap-2 px-4 py-2 rounded-lg ${
                timeLeft < 600 ? 'bg-red-100 text-red-600' : 'bg-blue-100 text-blue-600'
              }`}>
                <Timer className="w-5 h-5" />
                <span className="font-mono font-bold">{formatTime(timeLeft)}</span>
              </div>
            )}
            
            {quickMode && (
              <div className="flex items-center gap-2 px-3 py-1.5 bg-green-100 text-green-600 rounded-lg">
                <Zap className="w-4 h-4" />
                <span className="text-sm font-medium">速记模式</span>
              </div>
            )}
            
            <button
              onClick={handleSubmit}
              className="px-4 py-2 bg-gradient-to-r from-indigo-500 to-purple-600 text-white rounded-lg hover:from-indigo-600 hover:to-purple-700 transition-all"
            >
              交卷
            </button>
          </div>
        </div>

        <div className="flex items-center gap-2 mb-4 px-2">
          <div className="flex-1 flex gap-1 overflow-x-auto pb-2">
            {questions.map((q, index) => {
              const isAnswered = answers[q.id]
              const isCurrent = index === currentIndex
              return (
                <button
                  key={q.id}
                  onClick={() => handleJumpTo(index)}
                  className={`w-8 h-8 flex-shrink-0 rounded-lg text-sm font-medium transition-all ${
                    isCurrent
                      ? 'bg-indigo-600 text-white'
                      : isAnswered
                      ? 'bg-green-100 text-green-700'
                      : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                  }`}
                >
                  {index + 1}
                </button>
              )
            })}
          </div>
        </div>

        <div className="flex-1 overflow-y-auto">
          {currentQuestion && (
            <div className="space-y-6">
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-3">
                    <span className="px-2 py-1 bg-indigo-100 text-indigo-700 text-xs font-medium rounded">
                      第 {currentIndex + 1} 题
                    </span>
                    {currentQuestion.type === 'multi' && (
                      <span className="px-2 py-1 bg-purple-100 text-purple-700 text-xs font-medium rounded">
                        多选题
                      </span>
                    )}
                    {currentQuestion.year && (
                      <span className="px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded">
                        {currentQuestion.year}年真题
                      </span>
                    )}
                    {currentQuestion.heatScore && (
                      <span 
                        className="flex items-center gap-1 px-2 py-1 text-xs font-medium rounded"
                        style={{ 
                          backgroundColor: getHeatLabel(currentQuestion.heatScore).color + '20',
                          color: getHeatLabel(currentQuestion.heatScore).color
                        }}
                      >
                        {getHeatLabel(currentQuestion.heatScore).icon}
                        {getHeatLabel(currentQuestion.heatScore).label}
                      </span>
                    )}
                  </div>
                  <h3 className="text-lg text-gray-800 leading-relaxed">
                    {currentQuestion.question}
                  </h3>
                </div>
              </div>

              <div className="space-y-3">
                {currentQuestion.options?.map((option, index) => {
                  const optionLetter = option.charAt(0)
                  const isSelected = answers[currentQuestion.id] === optionLetter
                  const isCorrect = currentQuestion.answer === optionLetter
                  const showResult = quickMode || isSubmitted

                  let optionClass = 'border-2 bg-white hover:border-indigo-300 hover:bg-indigo-50'

                  if (showResult) {
                    if (isCorrect) {
                      optionClass = 'border-2 bg-green-50 border-green-400'
                    } else if (isSelected && !isCorrect) {
                      optionClass = 'border-2 bg-red-50 border-red-400'
                    }
                  } else if (isSelected) {
                    optionClass = 'border-2 bg-indigo-50 border-indigo-400'
                  }

                  return (
                    <div
                      key={index}
                      onClick={() => handleAnswerSelect(optionLetter)}
                      className={`p-4 rounded-xl cursor-pointer transition-all ${optionClass}`}
                    >
                      <div className="flex items-center gap-3">
                        {showResult && isCorrect && (
                          <CheckCircle className="w-5 h-5 text-green-600 flex-shrink-0" />
                        )}
                        {showResult && isSelected && !isCorrect && (
                          <XCircle className="w-5 h-5 text-red-600 flex-shrink-0" />
                        )}
                        {!showResult && (
                          <div className={`w-5 h-5 rounded-full border-2 flex-shrink-0 ${
                            isSelected ? 'border-indigo-500 bg-indigo-500' : 'border-gray-300'
                          }`}>
                            {isSelected && (
                              <div className="w-full h-full flex items-center justify-center">
                                <div className="w-2 h-2 bg-white rounded-full" />
                              </div>
                            )}
                          </div>
                        )}
                        <span className="text-gray-800">{option}</span>
                      </div>
                    </div>
                  )
                })}
              </div>

              {(quickMode || isSubmitted) && currentQuestion.explanation && (
                <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-5">
                  <div className="flex items-start gap-3">
                    <BookOpen className="w-5 h-5 text-indigo-600 flex-shrink-0 mt-0.5" />
                    <div>
                      <h4 className="font-semibold text-indigo-800 mb-2">答案解析</h4>
                      <p className="text-sm text-gray-700 leading-relaxed">
                        {currentQuestion.explanation}
                      </p>
                      {currentQuestion.knowledgePoint && (
                        <div className="mt-3 flex items-center gap-2">
                          <span className="text-xs text-gray-500">知识点：</span>
                          <span className="px-2 py-1 bg-indigo-100 text-indigo-700 text-xs rounded">
                            {currentQuestion.knowledgePoint}
                          </span>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>

        <div className="flex items-center justify-between mt-4 pt-4 border-t">
          <button
            onClick={handlePrev}
            disabled={currentIndex === 0}
            className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <ArrowRight className="w-4 h-4 rotate-180" />
            <span>上一题</span>
          </button>
          
          <div className="text-sm text-gray-500">
            已答 {Object.keys(answers).length} / {questions.length} 题
          </div>
          
          <button
            onClick={handleNext}
            disabled={currentIndex === questions.length - 1}
            className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-indigo-500 to-purple-600 text-white rounded-lg hover:from-indigo-600 hover:to-purple-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span>下一题</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    )
  }

  if (isSubmitted) {
    const correctCount = questions.filter(q => answers[q.id] === q.answer).length
    const totalScore = questions.reduce((sum, q) => 
      sum + (answers[q.id] === q.answer ? q.points : 0), 0
    )
    const maxScore = questions.reduce((sum, q) => sum + q.points, 0)
    const accuracy = ((correctCount / questions.length) * 100).toFixed(1)

    return (
      <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-gradient-to-r from-green-500 to-emerald-600 rounded-full flex items-center justify-center">
              <Award className="w-6 h-6 text-white" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-gray-800">考试完成</h2>
              <p className="text-sm text-gray-500">{selectedCategory.name}</p>
            </div>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
            <div className="bg-gradient-to-br from-blue-50 to-indigo-100 rounded-xl p-4 text-center">
              <div className="text-3xl font-bold text-indigo-600">{totalScore.toFixed(1)}</div>
              <div className="text-sm text-gray-600">得分</div>
            </div>
            <div className="bg-gradient-to-br from-green-50 to-emerald-100 rounded-xl p-4 text-center">
              <div className="text-3xl font-bold text-green-600">{correctCount}</div>
              <div className="text-sm text-gray-600">正确题数</div>
            </div>
            <div className="bg-gradient-to-br from-purple-50 to-pink-100 rounded-xl p-4 text-center">
              <div className="text-3xl font-bold text-purple-600">{accuracy}%</div>
              <div className="text-sm text-gray-600">正确率</div>
            </div>
            <div className="bg-gradient-to-br from-orange-50 to-yellow-100 rounded-xl p-4 text-center">
              <div className="text-3xl font-bold text-orange-600">
                {formatTime((metadata?.timeLimit * 60 || 0) - timeLeft)}
              </div>
              <div className="text-sm text-gray-600">用时</div>
            </div>
          </div>

          <div className="mb-6">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">答题情况</h3>
            <div className="grid grid-cols-10 gap-2">
              {questions.map((q, index) => {
                const isCorrect = answers[q.id] === q.answer
                const isAnswered = answers[q.id]
                return (
                  <button
                    key={q.id}
                    onClick={() => {
                      setCurrentIndex(index)
                      setIsSubmitted(false)
                      setView('exam')
                    }}
                    className={`w-10 h-10 rounded-lg text-sm font-medium transition-all ${
                      isCorrect
                        ? 'bg-green-100 text-green-700 hover:bg-green-200'
                        : isAnswered
                        ? 'bg-red-100 text-red-700 hover:bg-red-200'
                        : 'bg-gray-100 text-gray-500 hover:bg-gray-200'
                    }`}
                  >
                    {index + 1}
                  </button>
                )
              })}
            </div>
          </div>

          <div className="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-xl p-5">
            <h3 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-indigo-600" />
              学习建议
            </h3>
            <div className="space-y-2 text-sm text-gray-600">
              {parseFloat(accuracy) >= 80 ? (
                <p>🎉 表现优秀！继续保持，建议进行全真模拟考试检验综合能力。</p>
              ) : parseFloat(accuracy) >= 60 ? (
                <p>💪 基础扎实！建议使用"智能弱项强化"功能针对性提升薄弱知识点。</p>
              ) : (
                <p>📚 需要加强！建议先完成真题练习，再使用"记忆曲线复习"巩固错题。</p>
              )}
            </div>
          </div>
        </div>

        <div className="flex justify-center gap-4 mt-6 pt-4 border-t">
          <button
            onClick={handleBackToMenu}
            className="flex items-center gap-2 px-6 py-3 bg-gray-100 text-gray-700 rounded-xl hover:bg-gray-200 transition-all"
          >
            <ArrowRight className="w-5 h-5 rotate-180" />
            <span>返回首页</span>
          </button>
          <button
            onClick={handleRestart}
            className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-indigo-500 to-purple-600 text-white rounded-xl hover:from-indigo-600 hover:to-purple-700 transition-all"
          >
            <RefreshCw className="w-5 h-5" />
            <span>再做一次</span>
          </button>
        </div>
      </div>
    )
  }

  return null
}

export default PracticeExam
