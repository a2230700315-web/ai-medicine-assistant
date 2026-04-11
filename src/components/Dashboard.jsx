import { useState, useEffect } from 'react'
import { GraduationCap, BookOpen, Eye, EyeOff, Play, FileText, ChevronLeft, ChevronRight } from 'lucide-react'
import CaseCategorySelector from './CaseCategorySelector'
import CaseList from './CaseList'
import CaseDetail from './CaseDetail'
import ChatInterface from './ChatInterface'
import KnowledgeAssistant from './KnowledgeAssistant'
import LearningModule from './LearningModule'
import PracticeExam from './PracticeExam'
import RealExam from './RealExam'

function Dashboard() {
  const [cases, setCases] = useState([])
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [selectedCase, setSelectedCase] = useState(null)
  const [currentPracticeCase, setCurrentPracticeCase] = useState(null)
  const [examMode, setExamMode] = useState(false)
  const [currentMode, setCurrentMode] = useState('practice')
  const [assistantCollapsed, setAssistantCollapsed] = useState(true)

  useEffect(() => {
    fetch('/cases_filtered.json')
      .then(res => res.json())
      .then(data => setCases(data))
      .catch(err => console.error('加载案例数据失败:', err))
  }, [])

  const handleCategorySelect = (categoryId) => {
    setSelectedCategory(categoryId)
    setSelectedCase(null)
  }

  const handleCaseSelect = (case_) => {
    setSelectedCase(case_)
  }

  const handleBackToCategories = () => {
    setSelectedCategory(null)
    setSelectedCase(null)
  }

  const handleBackToList = () => {
    setSelectedCase(null)
    setCurrentPracticeCase(null)
  }

  const handleStartPractice = (case_, difficulty = 'medium') => {
    setCurrentPracticeCase({
      ...case_,
      difficulty: difficulty
    })
    setSelectedCase(null)
    setSelectedCategory(null)
  }

  const handleCaseRecommend = (relatedCases) => {
    setCurrentMode('practice')
    setSelectedCategory(relatedCases[0])
    setSelectedCase(null)
    setCurrentPracticeCase(null)
  }

  const handleBackToMain = () => {
    setCurrentMode('practice')
    setSelectedCategory(null)
    setSelectedCase(null)
    setCurrentPracticeCase(null)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-lg">药</span>
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-800">药房健康顾问培训平台</h1>
                <p className="text-sm text-gray-500">欢迎回来</p>
              </div>
            </div>
            <div className="flex items-center gap-3">
              <button
                onClick={() => setCurrentMode('practice')}
                className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
                  currentMode === 'practice' 
                    ? 'bg-blue-500 text-white hover:bg-blue-600' 
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                }`}
              >
                <GraduationCap className="w-4 h-4" />
                <span className="text-sm">案例练习</span>
              </button>
              <button
                onClick={() => setCurrentMode('learning')}
                className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
                  currentMode === 'learning' 
                    ? 'bg-green-500 text-white hover:bg-green-600' 
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                }`}
              >
                <BookOpen className="w-4 h-4" />
                <span className="text-sm">学习中心</span>
              </button>
              <button
                onClick={() => setCurrentMode('practiceExam')}
                className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
                  currentMode === 'practiceExam' 
                    ? 'bg-emerald-500 text-white hover:bg-emerald-600' 
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                }`}
              >
                <Play className="w-4 h-4" />
                <span className="text-sm">模拟题</span>
              </button>
              <button
                onClick={() => setCurrentMode('realExam')}
                className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
                  currentMode === 'realExam' 
                    ? 'bg-red-500 text-white hover:bg-red-600' 
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                }`}
              >
                <FileText className="w-4 h-4" />
                <span className="text-sm">真题考试</span>
              </button>
              {currentMode === 'practice' && (
                <button
                  onClick={() => setExamMode(!examMode)}
                  className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
                    examMode 
                      ? 'bg-orange-500 text-white hover:bg-orange-600' 
                      : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                  }`}
                >
                  {examMode ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                  <span className="text-sm">{examMode ? '考试模式' : '练习模式'}</span>
                </button>
              )}
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {currentMode === 'practice' ? (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <div className="lg:col-span-3 lg:sticky lg:top-6 lg:self-start">
              {!examMode && !selectedCategory && !selectedCase && !currentPracticeCase && (
                <CaseCategorySelector
                  cases={cases}
                  onCategorySelect={handleCategorySelect}
                  selectedCategory={selectedCategory}
                  onBack={handleBackToCategories}
                />
              )}
              {!examMode && selectedCategory && !selectedCase && !currentPracticeCase && (
                <CaseList
                  cases={cases}
                  category={selectedCategory}
                  onCaseSelect={handleCaseSelect}
                  onBack={handleBackToCategories}
                />
              )}
              {!examMode && (selectedCase || currentPracticeCase) && (
                <CaseDetail
                  case_={selectedCase || currentPracticeCase}
                  onStartPractice={handleStartPractice}
                  onBack={handleBackToList}
                />
              )}
              {examMode && (
                <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col items-center justify-center">
                  <div className="text-center">
                    <EyeOff className="w-12 h-12 text-gray-400 mx-auto mb-4" />
                    <h3 className="text-lg font-medium text-gray-700">考试模式已启用</h3>
                    <p className="text-sm text-gray-500 mt-2">案例档案已隐藏</p>
                  </div>
                </div>
              )}
            </div>
            <div className="lg:col-span-6">
              <ChatInterface practiceCase={currentPracticeCase} examMode={examMode} />
            </div>
            <div className="lg:col-span-3">
              <KnowledgeAssistant examMode={examMode} />
            </div>
          </div>
        ) : currentMode === 'learning' ? (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 relative">
            <div className={assistantCollapsed ? "lg:col-span-12" : "lg:col-span-8"}>
              <LearningModule onCaseRecommend={handleCaseRecommend} />
            </div>
            <div className={assistantCollapsed ? "hidden" : "lg:col-span-4"}>
              <KnowledgeAssistant examMode={false} />
            </div>
            <button
              onClick={() => setAssistantCollapsed(!assistantCollapsed)}
              className="fixed right-6 top-1/2 -translate-y-1/2 z-50 w-12 h-12 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-full shadow-lg hover:shadow-xl transition-all flex items-center justify-center hover:scale-110"
            >
              {assistantCollapsed ? <ChevronLeft className="w-6 h-6" /> : <ChevronRight className="w-6 h-6" />}
            </button>
          </div>
        ) : currentMode === 'practiceExam' ? (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <div className="lg:col-span-8">
              <PracticeExam onBack={handleBackToMain} />
            </div>
            <div className="lg:col-span-4">
              <KnowledgeAssistant examMode={false} />
            </div>
          </div>
        ) : currentMode === 'realExam' ? (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <div className="lg:col-span-8">
              <RealExam onBack={handleBackToMain} />
            </div>
            <div className="lg:col-span-4">
              <KnowledgeAssistant examMode={false} />
            </div>
          </div>
        ) : null}
      </main>
    </div>
  )
}

export default Dashboard
