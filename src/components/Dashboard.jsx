import { useState, useEffect } from 'react'
import { GraduationCap, BookOpen, Eye, EyeOff, Play, FileText, ChevronLeft, ChevronRight, LogOut, Store, Building2, Menu, X, User, Home, Award, Settings } from 'lucide-react'
import CaseCategorySelector from './CaseCategorySelector'
import CaseList from './CaseList'
import CaseDetail from './CaseDetail'
import ChatInterface from './ChatInterface'
import KnowledgeAssistant from './KnowledgeAssistant'
import LearningModule from './LearningModule'
import PracticeExam from './PracticeExam'
import ExamSystem from './ExamSystem'
import StoreManagement from './StoreManagement'
import HeadquartersDashboard from './HeadquartersDashboard'
import { useAuth } from '../context/AuthContext'

function Dashboard() {
  const { user, logout, canAccess } = useAuth()
  const [cases, setCases] = useState([])
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [selectedCase, setSelectedCase] = useState(null)
  const [currentPracticeCase, setCurrentPracticeCase] = useState(null)
  const [examMode, setExamMode] = useState(false)
  const [currentMode, setCurrentMode] = useState('learning')
  const [assistantCollapsed, setAssistantCollapsed] = useState(true)
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const [permissionDenied, setPermissionDenied] = useState(false)
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const [isMobile, setIsMobile] = useState(false)

  useEffect(() => {
    fetch('/cases_filtered.json')
      .then(res => res.json())
      .then(data => setCases(data))
      .catch(err => console.error('加载案例数据失败:', err))
  }, [])

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 768)
      if (window.innerWidth >= 768) {
        setMobileMenuOpen(false)
      }
    }
    checkMobile()
    window.addEventListener('resize', checkMobile)
    return () => window.removeEventListener('resize', checkMobile)
  }, [])

  const handleModeChange = (mode) => {
    if (mode === 'storeManagement' && !canAccess('storeManagement')) {
      setPermissionDenied(true)
      setTimeout(() => setPermissionDenied(false), 3000)
      return
    }
    if (mode === 'headquarters' && !canAccess('headquarters')) {
      setPermissionDenied(true)
      setTimeout(() => setPermissionDenied(false), 3000)
      return
    }
    setCurrentMode(mode)
    setSelectedCategory(null)
    setSelectedCase(null)
    setCurrentPracticeCase(null)
    setMobileMenuOpen(false)
  }

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

  const getWelcomeText = () => {
    if (!user) return '欢迎回来'
    return `欢迎您，${user.storeName}${user.roleName}`
  }

  const menuItems = [
    { id: 'learning', label: '学习', icon: BookOpen, color: 'green', permission: 'learning' },
    { id: 'practice', label: '练习', icon: GraduationCap, color: 'blue', permission: 'practice' },
    { id: 'practiceExam', label: '模拟', icon: Play, color: 'emerald', permission: 'practiceExam' },
    { id: 'realExam', label: '真题', icon: FileText, color: 'red', permission: 'realExam' },
  ]

  if (canAccess('storeManagement')) {
    menuItems.push({ id: 'storeManagement', label: '门店', icon: Store, color: 'purple', permission: 'storeManagement' })
  }

  if (canAccess('headquarters')) {
    menuItems.push({ id: 'headquarters', label: '总部', icon: Building2, color: 'orange', permission: 'headquarters' })
  }

  const getColorClasses = (color, isActive) => {
    const colors = {
      green: isActive ? 'bg-green-500 text-white' : 'bg-gray-100 text-gray-700',
      blue: isActive ? 'bg-blue-500 text-white' : 'bg-gray-100 text-gray-700',
      emerald: isActive ? 'bg-emerald-500 text-white' : 'bg-gray-100 text-gray-700',
      red: isActive ? 'bg-red-500 text-white' : 'bg-gray-100 text-gray-700',
      purple: isActive ? 'bg-purple-500 text-white' : 'bg-gray-100 text-gray-700',
      orange: isActive ? 'bg-orange-500 text-white' : 'bg-gray-100 text-gray-700',
    }
    return colors[color] || colors.blue
  }

  const getMobileNavColor = (color, isActive) => {
    const colors = {
      green: isActive ? 'text-green-500' : 'text-gray-500',
      blue: isActive ? 'text-blue-500' : 'text-gray-500',
      emerald: isActive ? 'text-emerald-500' : 'text-gray-500',
      red: isActive ? 'text-red-500' : 'text-gray-500',
      purple: isActive ? 'text-purple-500' : 'text-gray-500',
      orange: isActive ? 'text-orange-500' : 'text-gray-500',
    }
    return colors[color] || colors.blue
  }

  const getPageTitle = () => {
    switch(currentMode) {
      case 'learning': return '学习中心'
      case 'practice': return '案例练习'
      case 'practiceExam': return '模拟题'
      case 'realExam': return '真题考试'
      case 'storeManagement': return '门店管理'
      case 'headquarters': return '总部看板'
      default: return '药房培训平台'
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex flex-col">
      {permissionDenied && (
        <div className="fixed top-4 left-1/2 -translate-x-1/2 z-50 bg-red-500 text-white px-6 py-3 rounded-lg shadow-lg flex items-center gap-2 animate-pulse">
          <X className="w-5 h-5" />
          <span className="font-medium">权限不足，无法访问该功能</span>
        </div>
      )}

      {isMobile ? (
        <>
          <header className="bg-white shadow-sm border-b border-gray-200 safe-area-top sticky top-0 z-40">
            <div className="px-4 py-3 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-9 h-9 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center">
                  <span className="text-white font-bold">药</span>
                </div>
                <div>
                  <h1 className="text-base font-bold text-gray-800">{getPageTitle()}</h1>
                  <p className="text-xs text-gray-500">{user?.storeName} · {user?.roleName}</p>
                </div>
              </div>
              <div className="flex items-center gap-2">
                {currentMode === 'practice' && (
                  <button
                    onClick={() => setExamMode(!examMode)}
                    className={`p-2 rounded-lg ${examMode ? 'bg-orange-500 text-white' : 'bg-gray-100 text-gray-700'}`}
                  >
                    {examMode ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                  </button>
                )}
                <button
                  onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                  className="p-2 bg-gray-100 rounded-lg"
                >
                  <Menu className="w-5 h-5 text-gray-700" />
                </button>
              </div>
            </div>
          </header>

          {mobileMenuOpen && (
            <div className="fixed inset-0 z-50 bg-black/50" onClick={() => setMobileMenuOpen(false)}>
              <div 
                className="absolute right-0 top-0 bottom-0 w-72 bg-white shadow-xl safe-area-top"
                onClick={e => e.stopPropagation()}
              >
                <div className="p-4 border-b border-gray-200 flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                      <User className="w-5 h-5 text-blue-600" />
                    </div>
                    <div>
                      <p className="font-medium text-gray-800">{user?.storeName}</p>
                      <p className="text-xs text-gray-500">{user?.roleName}</p>
                    </div>
                  </div>
                  <button onClick={() => setMobileMenuOpen(false)} className="p-2">
                    <X className="w-5 h-5 text-gray-500" />
                  </button>
                </div>
                <nav className="p-3 space-y-1">
                  {menuItems.map((item) => {
                    const Icon = item.icon
                    const isActive = currentMode === item.id
                    return (
                      <button
                        key={item.id}
                        onClick={() => handleModeChange(item.id)}
                        className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-all ${getColorClasses(item.color, isActive)}`}
                      >
                        <Icon className="w-5 h-5" />
                        <span className="font-medium">{item.label}</span>
                      </button>
                    )
                  })}
                </nav>
                <div className="absolute bottom-0 left-0 right-0 p-4 border-t border-gray-200 safe-area-bottom">
                  <button
                    onClick={logout}
                    className="w-full flex items-center justify-center gap-2 px-4 py-3 bg-red-50 text-red-600 rounded-lg"
                  >
                    <LogOut className="w-5 h-5" />
                    <span className="font-medium">退出登录</span>
                  </button>
                </div>
              </div>
            </div>
          )}

          <main className="flex-1 overflow-y-auto pb-20">
            {currentMode === 'practice' ? (
              <div className="flex flex-col h-full">
                {!examMode && !currentPracticeCase && (
                  <div className="p-3">
                    {!selectedCategory && !selectedCase && (
                      <CaseCategorySelector
                        cases={cases}
                        onCategorySelect={handleCategorySelect}
                        selectedCategory={selectedCategory}
                        onBack={handleBackToCategories}
                      />
                    )}
                    {selectedCategory && !selectedCase && (
                      <CaseList
                        cases={cases}
                        category={selectedCategory}
                        onCaseSelect={handleCaseSelect}
                        onBack={handleBackToCategories}
                      />
                    )}
                    {selectedCase && (
                      <CaseDetail
                        case_={selectedCase}
                        onStartPractice={handleStartPractice}
                        onBack={handleBackToList}
                      />
                    )}
                  </div>
                )}
                <div className="flex-1 flex flex-col">
                  <ChatInterface practiceCase={currentPracticeCase} examMode={examMode} />
                </div>
              </div>
            ) : currentMode === 'learning' ? (
              <div className="p-3">
                <LearningModule onCaseRecommend={handleCaseRecommend} />
              </div>
            ) : currentMode === 'practiceExam' ? (
              <div className="p-3 h-full">
                <PracticeExam onBack={handleBackToMain} />
              </div>
            ) : currentMode === 'realExam' ? (
              <ExamSystem onBack={() => setCurrentMode('learning')} />
            ) : currentMode === 'storeManagement' ? (
              <div className="p-3">
                <StoreManagement />
              </div>
            ) : currentMode === 'headquarters' ? (
              <div className="p-3">
                <HeadquartersDashboard />
              </div>
            ) : null}
          </main>

          <nav className="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 safe-area-bottom z-40">
            <div className="flex items-center justify-around py-2">
              {menuItems.slice(0, 5).map((item) => {
                const Icon = item.icon
                const isActive = currentMode === item.id
                return (
                  <button
                    key={item.id}
                    onClick={() => handleModeChange(item.id)}
                    className={`flex flex-col items-center py-1 px-3 ${getMobileNavColor(item.color, isActive)}`}
                  >
                    <Icon className="w-5 h-5" />
                    <span className="text-xs mt-1">{item.label}</span>
                  </button>
                )
              })}
            </div>
          </nav>
        </>
      ) : (
        <div className="flex flex-1">
          <aside className={`${sidebarOpen ? 'w-64' : 'w-20'} bg-white shadow-lg transition-all duration-300 flex flex-col`}>
            <div className="p-4 border-b border-gray-200">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center flex-shrink-0">
                  <span className="text-white font-bold text-lg">药</span>
                </div>
                {sidebarOpen && (
                  <div className="overflow-hidden">
                    <h1 className="text-lg font-bold text-gray-800 whitespace-nowrap">药房培训平台</h1>
                    <p className="text-xs text-gray-500 whitespace-nowrap">执业药师考试助手</p>
                  </div>
                )}
              </div>
            </div>

            <nav className="flex-1 p-3 space-y-2 overflow-y-auto">
              {menuItems.map((item) => {
                const Icon = item.icon
                const isActive = currentMode === item.id
                return (
                  <button
                    key={item.id}
                    onClick={() => handleModeChange(item.id)}
                    className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg transition-all hover:scale-105 ${getColorClasses(item.color, isActive)}`}
                  >
                    <Icon className="w-5 h-5 flex-shrink-0" />
                    {sidebarOpen && <span className="text-sm font-medium whitespace-nowrap">{item.label}</span>}
                  </button>
                )
              })}
            </nav>

            <div className="p-3 border-t border-gray-200">
              {sidebarOpen && user && (
                <div className="mb-3 p-3 bg-gray-50 rounded-lg">
                  <div className="flex items-center gap-2">
                    <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                      <User className="w-4 h-4 text-blue-600" />
                    </div>
                    <div className="overflow-hidden">
                      <p className="text-sm font-medium text-gray-800 truncate">{user.storeName}</p>
                      <p className="text-xs text-gray-500">{user.roleName}</p>
                    </div>
                  </div>
                </div>
              )}
              <button
                onClick={() => setSidebarOpen(!sidebarOpen)}
                className="w-full flex items-center justify-center gap-2 px-3 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all mb-2"
              >
                {sidebarOpen ? <ChevronLeft className="w-5 h-5" /> : <ChevronRight className="w-5 h-5" />}
                {sidebarOpen && <span className="text-sm">收起菜单</span>}
              </button>
              <button
                onClick={logout}
                className="w-full flex items-center justify-center gap-2 px-3 py-2 bg-red-50 text-red-600 rounded-lg hover:bg-red-100 transition-all"
              >
                <LogOut className="w-5 h-5" />
                {sidebarOpen && <span className="text-sm font-medium">退出登录</span>}
              </button>
            </div>
          </aside>

          <div className="flex-1 flex flex-col overflow-hidden">
            <header className="bg-white shadow-sm border-b border-gray-200">
              <div className="px-6 py-4">
                <div className="flex items-center justify-between">
                  <div>
                    <h2 className="text-xl font-bold text-gray-800">{getPageTitle()}</h2>
                    <p className="text-sm text-gray-500 mt-1">{getWelcomeText()}</p>
                  </div>
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
            </header>

            <main className="flex-1 overflow-y-auto p-6">
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
                <ExamSystem onBack={() => setCurrentMode('learning')} />
              ) : currentMode === 'storeManagement' ? (
                <StoreManagement />
              ) : currentMode === 'headquarters' ? (
                <HeadquartersDashboard />
              ) : null}
            </main>
          </div>
        </div>
      )}
    </div>
  )
}

export default Dashboard
