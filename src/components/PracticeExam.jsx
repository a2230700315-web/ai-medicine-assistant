import React, { useState } from 'react'
import { CheckCircle, XCircle, ArrowRight, Play, BookOpen } from 'lucide-react'
import { getQuestionsByCategory, getRandomQuestions } from '../data/examQuestions'

function PracticeExam({ onBack }) {
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0)
  const [selectedAnswer, setSelectedAnswer] = useState(null)
  const [showExplanation, setShowExplanation] = useState(false)
  const [score, setScore] = useState(0)
  const [answeredQuestions, setAnsweredQuestions] = useState([])
  const [questions, setQuestions] = useState([])

  const categories = [
    { id: 'pharmacy', name: '药学知识', icon: '💊', color: 'from-blue-50 to-blue-100' },
    { id: 'diseases', name: '疾病知识', icon: '🏥', color: 'from-green-50 to-green-100' },
    { id: 'regulations', name: '法规与合规', icon: '⚖️', color: 'from-purple-50 to-purple-100' },
    { id: 'communication', name: '沟通技巧', icon: '💬', color: 'from-orange-50 to-orange-100' }
  ]

  const handleCategorySelect = (categoryId) => {
    setSelectedCategory(categoryId)
    const categoryQuestions = getQuestionsByCategory(categoryId, 'practice')
    setQuestions(categoryQuestions)
    setCurrentQuestionIndex(0)
    setSelectedAnswer(null)
    setShowExplanation(false)
    setScore(0)
    setAnsweredQuestions([])
  }

  const handleAnswerSelect = (answer) => {
    if (showExplanation) return
    
    setSelectedAnswer(answer)
    const currentQuestion = questions[currentQuestionIndex]
    const isCorrect = answer === currentQuestion.answer
    
    setAnsweredQuestions([
      ...answeredQuestions,
      {
        questionIndex: currentQuestionIndex,
        selectedAnswer: answer,
        correctAnswer: currentQuestion.answer,
        isCorrect
      }
    ])
    
    if (isCorrect) {
      setScore(score + 1)
    }
    
    setShowExplanation(true)
  }

  const handleNextQuestion = () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1)
      setSelectedAnswer(null)
      setShowExplanation(false)
    }
  }

  const handleRestart = () => {
    setCurrentQuestionIndex(0)
    setSelectedAnswer(null)
    setShowExplanation(false)
    setScore(0)
    setAnsweredQuestions([])
  }

  const handleBackToCategories = () => {
    setSelectedCategory(null)
    setCurrentQuestionIndex(0)
    setSelectedAnswer(null)
    setShowExplanation(false)
    setScore(0)
    setAnsweredQuestions([])
    setQuestions([])
  }

  const currentQuestion = questions[currentQuestionIndex]
  const progress = ((currentQuestionIndex + 1) / questions.length) * 100

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 bg-gradient-to-r from-green-400 to-emerald-500 rounded-full flex items-center justify-center">
            <Play className="w-6 h-6 text-white" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-gray-800">模拟题练习</h2>
            <p className="text-sm text-gray-500">实时反馈 · 即时解析</p>
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
                  {getQuestionsByCategory(category.id, 'practice').length} 道题目
                </p>
              </div>
            ))}
          </div>
        </div>
      ) : currentQuestion ? (
        <div className="flex-1 flex flex-col">
          <div className="mb-6">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-600">
                第 {currentQuestionIndex + 1} 题 / 共 {questions.length} 题
              </span>
              <span className="text-sm font-medium text-gray-700">
                得分: {score} / {answeredQuestions.length}
              </span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className="bg-gradient-to-r from-green-400 to-emerald-500 h-2 rounded-full transition-all duration-300"
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
                  const isCorrect = currentQuestion.answer === optionLetter
                  
                  let optionClass = 'border-2 bg-white'
                  
                  if (showExplanation) {
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
                      className={`p-4 rounded-lg cursor-pointer transition-all ${optionClass}`}
                    >
                      <div className="flex items-center gap-3">
                        {showExplanation && isCorrect && (
                          <CheckCircle className="w-5 h-5 text-green-600 flex-shrink-0" />
                        )}
                        {showExplanation && isSelected && !isCorrect && (
                          <XCircle className="w-5 h-5 text-red-600 flex-shrink-0" />
                        )}
                        {!showExplanation && isSelected && (
                          <div className="w-5 h-5 rounded-full border-2 border-indigo-400 flex-shrink-0" />
                        )}
                        <span className="text-gray-800">{option}</span>
                      </div>
                    </div>
                  )
                })}
              </div>
            </div>

            {showExplanation && (
              <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg p-4 mb-4">
                <div className="flex items-start gap-2 mb-2">
                  <BookOpen className="w-5 h-5 text-indigo-600 flex-shrink-0 mt-0.5" />
                  <div>
                    <h4 className="font-semibold text-indigo-800 mb-1">答案解析</h4>
                    <p className="text-sm text-gray-700 leading-relaxed">
                      {currentQuestion.explanation}
                    </p>
                  </div>
                </div>
              </div>
            )}
          </div>

          <div className="flex justify-between mt-4">
            <button
              onClick={handleBackToCategories}
              className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
            >
              <ArrowRight className="w-4 h-4 rotate-180" />
              <span className="text-sm">返回分类</span>
            </button>
            <button
              onClick={handleRestart}
              className="flex items-center gap-2 px-4 py-2 bg-indigo-100 text-indigo-700 rounded-lg hover:bg-indigo-200 transition-all"
            >
              <Play className="w-4 h-4" />
              <span className="text-sm">重新开始</span>
            </button>
            <button
              onClick={handleNextQuestion}
              disabled={!showExplanation || currentQuestionIndex >= questions.length - 1}
              className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-green-500 to-emerald-600 text-white rounded-lg hover:from-green-600 hover:to-emerald-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span className="text-sm">
                {currentQuestionIndex >= questions.length - 1 ? '完成' : '下一题'}
              </span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      ) : (
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center">
            <BookOpen className="w-16 h-16 text-gray-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-700 mb-2">
              练习完成
            </h3>
            <p className="text-sm text-gray-500 mb-4">
              您已完成所有题目
            </p>
            <div className="text-2xl font-bold text-green-600 mb-4">
              得分: {score} / {questions.length}
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
                onClick={handleRestart}
                className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-green-500 to-emerald-600 text-white rounded-lg hover:from-green-600 hover:to-emerald-700 transition-all"
              >
                <Play className="w-4 h-4" />
                <span className="text-sm">重新开始</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default PracticeExam
