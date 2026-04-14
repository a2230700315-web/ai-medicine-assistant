import React, { useState } from 'react'
import { CheckCircle, XCircle, ArrowRight, FileText, Clock, Award } from 'lucide-react'
import { getQuestionsByCategory, getRandomQuestions } from '../data/examQuestions'

function RealExam({ onBack }) {
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0)
  const [selectedAnswer, setSelectedAnswer] = useState(null)
  const [answers, setAnswers] = useState({})
  const [examFinished, setExamFinished] = useState(false)
  const [showReview, setShowReview] = useState(false)
  const [questions, setQuestions] = useState([])
  const [examStartTime, setExamStartTime] = useState(null)
  const [examEndTime, setExamEndTime] = useState(null)

  const categories = [
    { id: 'pharmacy', name: '药学知识', icon: '💊', color: 'from-blue-50 to-blue-100' },
    { id: 'diseases', name: '疾病知识', icon: '🏥', color: 'from-green-50 to-green-100' },
    { id: 'regulations', name: '法规与合规', icon: '⚖️', color: 'from-purple-50 to-purple-100' },
    { id: 'communication', name: '沟通技巧', icon: '💬', color: 'from-orange-50 to-orange-100' }
  ]

  const handleCategorySelect = (categoryId) => {
    setSelectedCategory(categoryId)
    const categoryQuestions = getQuestionsByCategory(categoryId, 'real')
    setQuestions(categoryQuestions)
    setCurrentQuestionIndex(0)
    setSelectedAnswer(null)
    setAnswers({})
    setExamFinished(false)
    setShowReview(false)
    setExamStartTime(Date.now())
    setExamEndTime(null)
  }

  const handleAnswerSelect = (answer) => {
    setSelectedAnswer(answer)
    setAnswers({
      ...answers,
      [currentQuestionIndex]: answer
    })
  }

  const handleNextQuestion = () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1)
      setSelectedAnswer(answers[currentQuestionIndex + 1] || null)
    } else {
      handleFinishExam()
    }
  }

  const handlePreviousQuestion = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(currentQuestionIndex - 1)
      setSelectedAnswer(answers[currentQuestionIndex - 1] || null)
    }
  }

  const handleFinishExam = () => {
    setExamFinished(true)
    setExamEndTime(Date.now())
  }

  const handleReview = () => {
    setShowReview(true)
  }

  const handleRestart = () => {
    setCurrentQuestionIndex(0)
    setSelectedAnswer(null)
    setAnswers({})
    setExamFinished(false)
    setShowReview(false)
    setExamStartTime(Date.now())
    setExamEndTime(null)
  }

  const handleBackToCategories = () => {
    setSelectedCategory(null)
    setCurrentQuestionIndex(0)
    setSelectedAnswer(null)
    setAnswers({})
    setExamFinished(false)
    setShowReview(false)
    setQuestions([])
    setExamStartTime(null)
    setExamEndTime(null)
  }

  const calculateScore = () => {
    let correctCount = 0
    questions.forEach((question, index) => {
      if (answers[index] === question.answer) {
        correctCount++
      }
    })
    return correctCount
  }

  const formatTime = (milliseconds) => {
    const seconds = Math.floor(milliseconds / 1000)
    const minutes = Math.floor(seconds / 60)
    const remainingSeconds = seconds % 60
    return `${minutes}分${remainingSeconds}秒`
  }

  const currentQuestion = questions[currentQuestionIndex]
  const score = calculateScore()
  const progress = ((currentQuestionIndex + 1) / questions.length) * 100
  const answeredCount = Object.keys(answers).length
  const examTime = examEndTime && examStartTime ? examEndTime - examStartTime : null

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 bg-gradient-to-r from-red-400 to-pink-500 rounded-full flex items-center justify-center">
            <FileText className="w-6 h-6 text-white" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-gray-800">真题考试</h2>
            <p className="text-sm text-gray-500">执业药师真题 · 完成后复盘</p>
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

      {!selectedCategory ? (
        <div className="flex-1 overflow-y-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {categories.map((category) => (
              <div
                key={category.id}
                onClick={() => handleCategorySelect(category.id)}
                className={`p-6 rounded-xl cursor-pointer transition-all hover:scale-105 ${category.color}`}
              >
                <div className="text-4xl mb-3">{category.icon}</div>
                <h3 className="text-lg font-semibold text-gray-800 mb-2">
                  {category.name}
                </h3>
                <p className="text-sm text-gray-600">
                  {getQuestionsByCategory(category.id, 'real').length} 道真题
                </p>
              </div>
            ))}
          </div>
        </div>
      ) : examFinished ? (
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center">
            <Award className="w-16 h-16 text-yellow-500 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-700 mb-2">
              考试完成
            </h3>
            <p className="text-sm text-gray-500 mb-4">
              恭喜您完成本次考试
            </p>
            <div className="text-2xl font-bold text-green-600 mb-2">
              得分: {score} / {questions.length}
            </div>
            <div className="text-sm text-gray-600 mb-4">
              用时: {examTime ? formatTime(examTime) : '计算中...'}
            </div>
            <div className="flex justify-center gap-3">
              <button
                onClick={handleBackToCategories}
                className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
              >
                <ArrowRight className="w-4 h-4 rotate-180" />
                <span className="text-sm">返回分类</span>
              </button>
              <button
                onClick={handleReview}
                className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-indigo-500 to-purple-600 text-white rounded-lg hover:from-indigo-600 hover:to-purple-700 transition-all"
              >
                <FileText className="w-4 h-4" />
                <span className="text-sm">查看解析</span>
              </button>
              <button
                onClick={handleRestart}
                className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-green-500 to-emerald-600 text-white rounded-lg hover:from-green-600 hover:to-emerald-700 transition-all"
              >
                <FileText className="w-4 h-4" />
                <span className="text-sm">重新考试</span>
              </button>
            </div>
          </div>
        </div>
      ) : showReview ? (
        <div className="flex-1 flex flex-col">
          <div className="mb-6">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-600">
                第 {currentQuestionIndex + 1} 题 / 共 {questions.length} 题
              </span>
              <span className="text-sm font-medium text-gray-700">
                得分: {score} / {questions.length}
              </span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className="bg-gradient-to-r from-red-400 to-pink-500 h-2 rounded-full transition-all duration-300"
                style={{ width: `${progress}%` }}
              />
            </div>
          </div>

          <div className="flex-1 overflow-y-auto">
            <div className="mb-6">
              <h3 className="text-lg font-semibold text-gray-800 mb-4">
                {currentQuestion.question}
              </h3>
              <div className="space-y-3">
                {currentQuestion.options.map((option, index) => {
                  const optionLetter = option.charAt(0)
                  const isCorrect = currentQuestion.answer === optionLetter
                  const selectedOption = answers[currentQuestionIndex]
                  const isSelected = selectedOption === optionLetter
                  
                  let optionClass = 'border-2 bg-white'
                  
                  if (isCorrect) {
                    optionClass = 'border-2 bg-green-50 border-green-400'
                  } else if (isSelected && !isCorrect) {
                    optionClass = 'border-2 bg-red-50 border-red-400'
                  }
                  
                  return (
                    <div
                      key={index}
                      className={`p-4 rounded-lg ${optionClass}`}
                    >
                      <div className="flex items-center gap-3">
                        {isCorrect && (
                          <CheckCircle className="w-5 h-5 text-green-600 flex-shrink-0" />
                        )}
                        {isSelected && !isCorrect && (
                          <XCircle className="w-5 h-5 text-red-600 flex-shrink-0" />
                        )}
                        {!isCorrect && !isSelected && (
                          <div className="w-5 h-5" />
                        )}
                        <span className="text-gray-800">{option}</span>
                      </div>
                    </div>
                  )
                })}
              </div>
            </div>

            <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg p-4 mb-4">
              <div className="flex items-start gap-2 mb-2">
                <FileText className="w-5 h-5 text-indigo-600 flex-shrink-0 mt-0.5" />
                <div>
                  <h4 className="font-semibold text-indigo-800 mb-1">答案解析</h4>
                  <p className="text-sm text-gray-700 leading-relaxed">
                    {currentQuestion.explanation}
                  </p>
                </div>
              </div>
            </div>

            <div className="bg-gray-50 rounded-lg p-4">
              <h4 className="font-semibold text-gray-800 mb-2">考试信息</h4>
              <div className="grid grid-cols-2 gap-4 text-sm">
                <div>
                  <span className="text-gray-600">年份:</span>
                  <span className="ml-2 font-medium">{currentQuestion.year}</span>
                </div>
                <div>
                  <span className="text-gray-600">来源:</span>
                  <span className="ml-2 font-medium">{currentQuestion.source}</span>
                </div>
                <div>
                  <span className="text-gray-600">难度:</span>
                  <span className="ml-2 font-medium">{currentQuestion.difficulty}</span>
                </div>
                <div>
                  <span className="text-gray-600">您的答案:</span>
                  <span className={`ml-2 font-medium ${
                    answers[currentQuestionIndex] === currentQuestion.answer 
                      ? 'text-green-600' 
                      : 'text-red-600'
                  }`}>
                    {answers[currentQuestionIndex] || '未作答'}
                  </span>
                </div>
              </div>
            </div>
          </div>

          <div className="flex justify-between mt-4">
            <button
              onClick={handleBackToCategories}
              className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
            >
              <ArrowRight className="w-4 h-4 rotate-180" />
              <span className="text-sm">返回分类</span>
            </button>
            <div className="flex gap-2">
              <button
                onClick={handlePreviousQuestion}
                disabled={currentQuestionIndex === 0}
                className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <ArrowRight className="w-4 h-4 rotate-180" />
                <span className="text-sm">上一题</span>
              </button>
              <button
                onClick={handleNextQuestion}
                disabled={currentQuestionIndex >= questions.length - 1}
                className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-indigo-500 to-purple-600 text-white rounded-lg hover:from-indigo-600 hover:to-purple-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span className="text-sm">
                  {currentQuestionIndex >= questions.length - 1 ? '完成' : '下一题'}
                </span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      ) : currentQuestion ? (
        <div className="flex-1 flex flex-col">
          <div className="mb-6">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-600">
                第 {currentQuestionIndex + 1} 题 / 共 {questions.length} 题
              </span>
              <div className="flex items-center gap-4">
                <span className="text-sm text-gray-600">
                  已答: {answeredCount} / {questions.length}
                </span>
                {examStartTime && (
                  <div className="flex items-center gap-1 text-sm text-gray-600">
                    <Clock className="w-4 h-4" />
                    <span>
                      {formatTime(Date.now() - examStartTime)}
                    </span>
                  </div>
                )}
              </div>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className="bg-gradient-to-r from-red-400 to-pink-500 h-2 rounded-full transition-all duration-300"
                style={{ width: `${progress}%` }}
              />
            </div>
          </div>

          <div className="flex-1 overflow-y-auto">
            <div className="mb-6">
              <h3 className="text-lg font-semibold text-gray-800 mb-4">
                {currentQuestion.question}
              </h3>
              <div className="space-y-3">
                {currentQuestion.options.map((option, index) => {
                  const optionLetter = option.charAt(0)
                  const isSelected = selectedAnswer === optionLetter
                  
                  return (
                    <div
                      key={index}
                      onClick={() => handleAnswerSelect(optionLetter)}
                      className={`p-4 rounded-lg cursor-pointer transition-all border-2 ${
                        isSelected 
                          ? 'bg-indigo-50 border-indigo-400' 
                          : 'bg-white border-gray-200 hover:border-indigo-300'
                      }`}
                    >
                      <div className="flex items-center gap-3">
                        {isSelected ? (
                          <div className="w-5 h-5 rounded-full bg-indigo-500 flex-shrink-0" />
                        ) : (
                          <div className="w-5 h-5 rounded-full border-2 border-gray-300 flex-shrink-0" />
                        )}
                        <span className="text-gray-800">{option}</span>
                      </div>
                    </div>
                  )
                })}
              </div>
            </div>
          </div>

          <div className="flex justify-between mt-4">
            <button
              onClick={handleBackToCategories}
              className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
            >
              <ArrowRight className="w-4 h-4 rotate-180" />
              <span className="text-sm">返回分类</span>
            </button>
            <div className="flex gap-2">
              <button
                onClick={handlePreviousQuestion}
                disabled={currentQuestionIndex === 0}
                className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <ArrowRight className="w-4 h-4 rotate-180" />
                <span className="text-sm">上一题</span>
              </button>
              <button
                onClick={handleNextQuestion}
                disabled={!selectedAnswer}
                className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-red-500 to-pink-600 text-white rounded-lg hover:from-red-600 hover:to-pink-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span className="text-sm">
                  {currentQuestionIndex >= questions.length - 1 ? '提交试卷' : '下一题'}
                </span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      ) : (
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center">
            <FileText className="w-16 h-16 text-gray-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-700 mb-2">
              暂无真题
            </h3>
            <p className="text-sm text-gray-500">
              该分类暂无真题题目
            </p>
          </div>
        </div>
      )}
    </div>
  )
}

export default RealExam
