import { useState, useEffect, useCallback } from 'react'
import { Clock, ChevronLeft, ChevronRight, Flag, Check, X, AlertCircle, BookOpen, Award, RotateCcw, Home, BarChart2, Save } from 'lucide-react'
import { examCategories, sampleQuestions, shuffleArray, calculateScore } from '../data/examQuestions'
import { useAuth } from '../context/AuthContext'

const EXAM_TIME = 150

function ExamSystem({ onBack }) {
  const { user } = useAuth()
  const [stage, setStage] = useState('select')
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [selectedYear, setSelectedYear] = useState(null)
  const [questions, setQuestions] = useState([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [answers, setAnswers] = useState({})
  const [markedQuestions, setMarkedQuestions] = useState(new Set())
  const [timeLeft, setTimeLeft] = useState(EXAM_TIME * 60)
  const [showResult, setShowResult] = useState(false)
  const [result, setResult] = useState(null)
  const [reviewMode, setReviewMode] = useState(false)
  const [examStartTime, setExamStartTime] = useState(null)
  const [showSaveDialog, setShowSaveDialog] = useState(false)

  useEffect(() => {
    let timer
    if (stage === 'exam' && timeLeft > 0 && !showResult) {
      timer = setInterval(() => {
        setTimeLeft(prev => {
          if (prev <= 1) {
            handleSubmit()
            return 0
          }
          return prev - 1
        })
      }, 1000)
    }
    return () => clearInterval(timer)
  }, [stage, showResult])

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
  }

  const handleSelectCategory = (category) => {
    setSelectedCategory(category)
    setStage('year')
  }

  const handleSelectYear = (year) => {
    setSelectedYear(year)
    const categoryQuestions = sampleQuestions[selectedCategory.id]
    if (categoryQuestions && categoryQuestions[year]) {
      setQuestions(categoryQuestions[year])
    } else {
      const allQuestions = categoryQuestions ? Object.values(categoryQuestions).flat() : []
      setQuestions(allQuestions.slice(0, 10))
    }
    setStage('exam')
    setExamStartTime(Date.now())
    setTimeLeft(EXAM_TIME * 60)
  }

  const handleAnswer = (questionId, answer) => {
    setAnswers(prev => ({
      ...prev,
      [questionId]: answer
    }))
  }

  const handleMark = (questionId) => {
    setMarkedQuestions(prev => {
      const newSet = new Set(prev)
      if (newSet.has(questionId)) {
        newSet.delete(questionId)
      } else {
        newSet.add(questionId)
      }
      return newSet
    })
  }

  const handleSubmit = useCallback(() => {
    const examResult = calculateScore(questions, answers)
    examResult.timeUsed = EXAM_TIME * 60 - timeLeft
    examResult.categoryId = selectedCategory.id
    examResult.categoryName = selectedCategory.name
    examResult.year = selectedYear
    examResult.date = new Date().toISOString()
    setResult(examResult)
    setShowResult(true)
    setStage('result')
    
    const records = JSON.parse(localStorage.getItem('examRecords') || '[]')
    records.push({
      ...examResult,
      username: user?.username,
      storeId: user?.storeId,
      storeName: user?.storeName
    })
    localStorage.setItem('examRecords', JSON.stringify(records.slice(-100)))
  }, [questions, answers, timeLeft, selectedCategory, selectedYear, user])

  const handleRestart = () => {
    setStage('select')
    setSelectedCategory(null)
    setSelectedYear(null)
    setQuestions([])
    setCurrentIndex(0)
    setAnswers({})
    setMarkedQuestions(new Set())
    setTimeLeft(EXAM_TIME * 60)
    setShowResult(false)
    setResult(null)
    setReviewMode(false)
    setShowSaveDialog(false)
  }

  const handleSaveProgress = () => {
    const progressData = {
      categoryId: selectedCategory.id,
      categoryName: selectedCategory.name,
      year: selectedYear,
      answers: answers,
      markedQuestions: Array.from(markedQuestions),
      timeLeft: timeLeft,
      timeUsed: EXAM_TIME * 60 - timeLeft,
      currentIndex: currentIndex,
      savedAt: new Date().toISOString(),
      username: user?.username,
      storeId: user?.storeId,
      storeName: user?.storeName
    }
    
    const savedProgress = JSON.parse(localStorage.getItem('examProgress') || '[]')
    savedProgress.push(progressData)
    localStorage.setItem('examProgress', JSON.stringify(savedProgress.slice(-50)))
    
    handleRestart()
  }

  const handleBackToLibrary = () => {
    if (stage === 'exam' && !reviewMode && Object.keys(answers).length > 0) {
      setShowSaveDialog(true)
    } else {
      handleRestart()
    }
  }

  const currentQuestion = questions[currentIndex]
  const answeredCount = Object.keys(answers).length
  const progress = questions.length > 0 ? ((currentIndex + 1) / questions.length) * 100 : 0

  if (stage === 'select') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
        <div className="max-w-6xl mx-auto">
          <div className="flex items-center justify-between mb-8">
            <div>
              <h1 className="text-3xl font-bold text-gray-800">真题考试</h1>
              <p className="text-gray-500 mt-1">选择科目开始考试</p>
            </div>
            <button
              onClick={onBack}
              className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
            >
              <Home className="w-5 h-5" />
              返回首页
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {examCategories.map((category) => (
              <div
                key={category.id}
                onClick={() => handleSelectCategory(category)}
                className="bg-white rounded-2xl shadow-lg p-6 cursor-pointer hover:shadow-xl transition-all hover:-translate-y-1 border-2 border-transparent hover:border-blue-500"
              >
                <div className="flex items-center gap-4 mb-4">
                  <div
                    className="w-14 h-14 rounded-xl flex items-center justify-center text-2xl"
                    style={{ backgroundColor: `${category.color}20` }}
                  >
                    {category.icon}
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-gray-800">{category.name}</h3>
                    <p className="text-sm text-gray-500">{category.shortName}</p>
                  </div>
                </div>
                <p className="text-sm text-gray-600 mb-4">{category.description}</p>
                <div className="flex items-center justify-between text-sm">
                  <span className="text-gray-500">题目数量: {category.totalQuestions}题</span>
                  <span className="text-gray-500">{category.years.length}年真题</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    )
  }

  if (stage === 'year') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
        <div className="max-w-4xl mx-auto">
          <button
            onClick={() => setStage('select')}
            className="flex items-center gap-2 text-gray-600 hover:text-gray-800 mb-6"
          >
            <ChevronLeft className="w-5 h-5" />
            返回选择科目
          </button>

          <div className="bg-white rounded-2xl shadow-lg p-8">
            <div className="flex items-center gap-4 mb-8">
              <div
                className="w-16 h-16 rounded-xl flex items-center justify-center text-3xl"
                style={{ backgroundColor: `${selectedCategory.color}20` }}
              >
                {selectedCategory.icon}
              </div>
              <div>
                <h2 className="text-2xl font-bold text-gray-800">{selectedCategory.name}</h2>
                <p className="text-gray-500">{selectedCategory.description}</p>
              </div>
            </div>

            <h3 className="text-lg font-semibold text-gray-700 mb-4">选择考试年份</h3>
            <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
              {selectedCategory.years.map((year) => (
                <button
                  key={year}
                  onClick={() => handleSelectYear(year)}
                  className="p-4 bg-gray-50 rounded-xl text-center hover:bg-blue-50 hover:text-blue-600 transition-all border-2 border-transparent hover:border-blue-500"
                >
                  <span className="text-xl font-bold">{year}</span>
                  <span className="block text-sm text-gray-500">年真题</span>
                </button>
              ))}
            </div>

            <div className="mt-8 p-4 bg-yellow-50 rounded-xl">
              <div className="flex items-center gap-2 text-yellow-700">
                <AlertCircle className="w-5 h-5" />
                <span className="font-medium">考试说明</span>
              </div>
              <ul className="mt-2 text-sm text-yellow-600 space-y-1">
                <li>• 考试时间：150分钟</li>
                <li>• 题目数量：根据实际真题设置</li>
                <li>• 考试过程中可标记题目，方便后续检查</li>
                <li>• 提交后可查看答案解析</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (stage === 'result') {
    const timeUsedMinutes = Math.floor(result.timeUsed / 60)
    const timeUsedSeconds = result.timeUsed % 60

    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-2xl shadow-lg overflow-hidden">
            <div className="bg-gradient-to-r from-blue-500 to-indigo-600 p-8 text-white text-center">
              <Award className="w-16 h-16 mx-auto mb-4" />
              <h2 className="text-3xl font-bold mb-2">考试完成</h2>
              <p className="text-blue-100">{selectedCategory.name} - {selectedYear}年真题</p>
            </div>

            <div className="p-8">
              <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mb-8">
                <div className="text-center p-4 bg-green-50 rounded-xl">
                  <div className="text-3xl font-bold text-green-600">{result.correct}</div>
                  <div className="text-sm text-gray-600">正确</div>
                </div>
                <div className="text-center p-4 bg-red-50 rounded-xl">
                  <div className="text-3xl font-bold text-red-600">{result.wrong}</div>
                  <div className="text-sm text-gray-600">错误</div>
                </div>
                <div className="text-center p-4 bg-gray-50 rounded-xl">
                  <div className="text-3xl font-bold text-gray-600">{result.unanswered}</div>
                  <div className="text-sm text-gray-600">未答</div>
                </div>
                <div className="text-center p-4 bg-blue-50 rounded-xl">
                  <div className="text-3xl font-bold text-blue-600">{result.accuracy}%</div>
                  <div className="text-sm text-gray-600">正确率</div>
                </div>
              </div>

              <div className="flex items-center justify-center gap-8 mb-8 text-gray-600">
                <div className="flex items-center gap-2">
                  <Clock className="w-5 h-5" />
                  <span>用时: {timeUsedMinutes}分{timeUsedSeconds}秒</span>
                </div>
                <div className="flex items-center gap-2">
                  <BarChart2 className="w-5 h-5" />
                  <span>得分: {result.score}分</span>
                </div>
              </div>

              <div className="flex justify-center gap-4">
                <button
                  onClick={() => {
                    setReviewMode(true)
                    setCurrentIndex(0)
                    setStage('exam')
                    setShowResult(false)
                  }}
                  className="flex items-center gap-2 px-6 py-3 bg-blue-500 text-white rounded-xl hover:bg-blue-600 transition-all"
                >
                  <BookOpen className="w-5 h-5" />
                  查看解析
                </button>
                <button
                  onClick={handleRestart}
                  className="flex items-center gap-2 px-6 py-3 bg-gray-100 text-gray-700 rounded-xl hover:bg-gray-200 transition-all"
                >
                  <RotateCcw className="w-5 h-5" />
                  重新开始
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (stage === 'exam') {
    return (
      <div className="min-h-screen bg-gray-100 flex flex-col">
        <header className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-10">
          <div className="max-w-7xl mx-auto px-4 py-3">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-4">
                <div
                  className="w-10 h-10 rounded-lg flex items-center justify-center text-xl"
                  style={{ backgroundColor: `${selectedCategory.color}20` }}
                >
                  {selectedCategory.icon}
                </div>
                <div>
                  <h2 className="font-bold text-gray-800">{selectedCategory.name}</h2>
                  <p className="text-sm text-gray-500">{selectedYear}年真题</p>
                </div>
              </div>

              <div className="flex items-center gap-6">
                {!reviewMode && (
                  <div className={`flex items-center gap-2 px-4 py-2 rounded-lg ${
                    timeLeft < 600 ? 'bg-red-100 text-red-600' : 'bg-gray-100 text-gray-700'
                  }`}>
                    <Clock className="w-5 h-5" />
                    <span className="font-mono text-lg font-bold">{formatTime(timeLeft)}</span>
                  </div>
                )}
                
                {reviewMode && (
                  <div className="flex items-center gap-2 px-4 py-2 bg-blue-100 text-blue-600 rounded-lg">
                    <BookOpen className="w-5 h-5" />
                    <span>解析模式</span>
                  </div>
                )}

                <div className="text-sm text-gray-600">
                  <span className="font-bold text-blue-600">{answeredCount}</span> / {questions.length} 已答
                </div>

                {!reviewMode && (
                  <button
                    onClick={handleSubmit}
                    className="px-6 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-all font-medium"
                  >
                    提交试卷
                  </button>
                )}

                <button
                  onClick={handleBackToLibrary}
                  className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
                >
                  <Home className="w-4 h-4" />
                  返回题库
                </button>
              </div>
            </div>

            <div className="mt-3 h-1 bg-gray-200 rounded-full overflow-hidden">
              <div
                className="h-full bg-blue-500 transition-all duration-300"
                style={{ width: `${progress}%` }}
              />
            </div>
          </div>
        </header>

        <div className="flex-1 flex">
          <main className="flex-1 p-6 overflow-y-auto">
            {currentQuestion && (
              <div className="max-w-4xl mx-auto">
                <div className="bg-white rounded-2xl shadow-lg p-8">
                  <div className="flex items-center justify-between mb-6">
                    <div className="flex items-center gap-3">
                      <span className="px-3 py-1 bg-blue-100 text-blue-600 rounded-full text-sm font-medium">
                        第 {currentIndex + 1} 题
                      </span>
                      <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                        currentQuestion.type === 'single' ? 'bg-green-100 text-green-600' : 'bg-purple-100 text-purple-600'
                      }`}>
                        {currentQuestion.type === 'single' ? '单选题' : '多选题'}
                      </span>
                      <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                        currentQuestion.difficulty === 'easy' ? 'bg-gray-100 text-gray-600' :
                        currentQuestion.difficulty === 'medium' ? 'bg-yellow-100 text-yellow-600' :
                        'bg-red-100 text-red-600'
                      }`}>
                        {currentQuestion.difficulty === 'easy' ? '简单' : currentQuestion.difficulty === 'medium' ? '中等' : '困难'}
                      </span>
                    </div>
                    <button
                      onClick={() => handleMark(currentQuestion.id)}
                      className={`flex items-center gap-2 px-3 py-1 rounded-lg transition-all ${
                        markedQuestions.has(currentQuestion.id)
                          ? 'bg-yellow-100 text-yellow-600'
                          : 'bg-gray-100 text-gray-500 hover:bg-gray-200'
                      }`}
                    >
                      <Flag className="w-4 h-4" />
                      {markedQuestions.has(currentQuestion.id) ? '已标记' : '标记'}
                    </button>
                  </div>

                  <div className="mb-8">
                    <p className="text-lg text-gray-800 leading-relaxed">{currentQuestion.question}</p>
                  </div>

                  <div className="space-y-3">
                    {currentQuestion.options.map((option, index) => {
                      const optionLetter = option.charAt(0)
                      const isSelected = answers[currentQuestion.id]?.includes(optionLetter)
                      const isCorrect = currentQuestion.answer.includes(optionLetter)
                      
                      let optionClass = 'border-2 border-gray-200 hover:border-blue-300 hover:bg-blue-50'
                      
                      if (reviewMode) {
                        if (isCorrect) {
                          optionClass = 'border-2 border-green-500 bg-green-50'
                        } else if (isSelected && !isCorrect) {
                          optionClass = 'border-2 border-red-500 bg-red-50'
                        }
                      } else if (isSelected) {
                        optionClass = 'border-2 border-blue-500 bg-blue-50'
                      }

                      return (
                        <button
                          key={index}
                          onClick={() => !reviewMode && handleAnswer(
                            currentQuestion.id,
                            currentQuestion.type === 'single'
                              ? optionLetter
                              : (answers[currentQuestion.id] || '').includes(optionLetter)
                                ? (answers[currentQuestion.id] || '').replace(optionLetter, '')
                                : (answers[currentQuestion.id] || '') + optionLetter
                          )}
                          className={`w-full text-left p-4 rounded-xl transition-all ${optionClass} ${reviewMode ? 'cursor-default' : ''}`}
                        >
                          <div className="flex items-start gap-3">
                            <span className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0 ${
                              reviewMode && isCorrect ? 'bg-green-500 text-white' :
                              reviewMode && isSelected && !isCorrect ? 'bg-red-500 text-white' :
                              isSelected ? 'bg-blue-500 text-white' : 'bg-gray-200 text-gray-600'
                            }`}>
                              {reviewMode && isCorrect ? <Check className="w-4 h-4" /> :
                               reviewMode && isSelected && !isCorrect ? <X className="w-4 h-4" /> :
                               optionLetter}
                            </span>
                            <span className="text-gray-700 pt-1">{option.substring(3)}</span>
                          </div>
                        </button>
                      )
                    })}
                  </div>

                  {reviewMode && (
                    <div className="mt-8 p-6 bg-blue-50 rounded-xl">
                      <div className="flex items-center gap-2 mb-3">
                        <BookOpen className="w-5 h-5 text-blue-600" />
                        <span className="font-bold text-blue-600">答案解析</span>
                      </div>
                      <div className="mb-3">
                        <span className="text-sm text-gray-600">正确答案：</span>
                        <span className="font-bold text-green-600">{currentQuestion.answer}</span>
                      </div>
                      {currentQuestion.explanation && (
                        <div className="mt-3">
                          <span className="text-sm text-gray-600">解析：</span>
                          <p className="text-gray-700 leading-relaxed mt-1">{currentQuestion.explanation}</p>
                        </div>
                      )}
                      {currentQuestion.chapter && (
                        <div className="mt-3 p-3 bg-yellow-50 rounded-lg">
                          <span className="text-sm text-yellow-700">考点：{currentQuestion.chapter}</span>
                        </div>
                      )}
                    </div>
                  )}
                </div>

                <div className="flex items-center justify-between mt-6">
                  <button
                    onClick={() => setCurrentIndex(Math.max(0, currentIndex - 1))}
                    disabled={currentIndex === 0}
                    className="flex items-center gap-2 px-6 py-3 bg-white rounded-xl shadow hover:shadow-md transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    <ChevronLeft className="w-5 h-5" />
                    上一题
                  </button>

                  <button
                    onClick={() => setCurrentIndex(Math.min(questions.length - 1, currentIndex + 1))}
                    disabled={currentIndex === questions.length - 1}
                    className="flex items-center gap-2 px-6 py-3 bg-white rounded-xl shadow hover:shadow-md transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    下一题
                    <ChevronRight className="w-5 h-5" />
                  </button>
                </div>
              </div>
            )}
          </main>

          <aside className="w-80 bg-white border-l border-gray-200 p-4 overflow-y-auto hidden lg:block">
            <h3 className="font-bold text-gray-800 mb-4">答题卡</h3>
            <div className="grid grid-cols-5 gap-2">
              {questions.map((q, index) => {
                const isAnswered = answers[q.id]
                const isMarked = markedQuestions.has(q.id)
                const isCurrent = index === currentIndex

                return (
                  <button
                    key={q.id}
                    onClick={() => setCurrentIndex(index)}
                    className={`w-10 h-10 rounded-lg text-sm font-medium transition-all relative ${
                      isCurrent ? 'ring-2 ring-blue-500 ring-offset-2' : ''
                    } ${
                      isAnswered
                        ? 'bg-blue-500 text-white'
                        : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                    }`}
                  >
                    {index + 1}
                    {isMarked && (
                      <span className="absolute -top-1 -right-1 w-3 h-3 bg-yellow-500 rounded-full" />
                    )}
                  </button>
                )
              })}
            </div>

            <div className="mt-6 pt-4 border-t border-gray-200">
              <div className="flex items-center gap-4 text-sm text-gray-600">
                <div className="flex items-center gap-2">
                  <span className="w-4 h-4 bg-blue-500 rounded" />
                  <span>已答</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="w-4 h-4 bg-gray-100 rounded" />
                  <span>未答</span>
                </div>
              </div>
              <div className="flex items-center gap-2 mt-2 text-sm text-gray-600">
                <span className="w-4 h-4 bg-yellow-500 rounded-full" />
                <span>已标记</span>
              </div>
            </div>
          </aside>
        </div>

        {showSaveDialog && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
            <div className="bg-white rounded-2xl shadow-xl p-6 max-w-md w-full mx-4">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                  <Save className="w-6 h-6 text-blue-600" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-gray-800">保存做题记录</h3>
                  <p className="text-sm text-gray-500">您已答 {Object.keys(answers).length} 题</p>
                </div>
              </div>
              
              <p className="text-gray-600 mb-6">
                返回题库前是否保存当前做题进度？保存后可随时继续答题。
              </p>
              
              <div className="flex gap-3">
                <button
                  onClick={handleSaveProgress}
                  className="flex-1 px-4 py-3 bg-blue-500 text-white rounded-xl hover:bg-blue-600 transition-all font-medium"
                >
                  保存并返回
                </button>
                <button
                  onClick={handleRestart}
                  className="flex-1 px-4 py-3 bg-gray-100 text-gray-700 rounded-xl hover:bg-gray-200 transition-all font-medium"
                >
                  不保存
                </button>
                <button
                  onClick={() => setShowSaveDialog(false)}
                  className="px-4 py-3 bg-gray-100 text-gray-700 rounded-xl hover:bg-gray-200 transition-all"
                >
                  取消
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    )
  }

  return null
}

export default ExamSystem
