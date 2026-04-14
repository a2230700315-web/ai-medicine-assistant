import React, { useState, useEffect, useRef } from 'react'
import { BookOpen, CheckCircle, ArrowRight, Play, ChevronDown, ChevronRight, FolderOpen, Folder, Circle, CheckCircle2 } from 'lucide-react'
import { learningContent } from '../data/learningContent'

function LearningModule({ onCaseRecommend }) {
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [selectedSubject, setSelectedSubject] = useState(null)
  const [selectedTopic, setSelectedTopic] = useState(null)
  const [completedTopics, setCompletedTopics] = useState([])
  const [expandedCategories, setExpandedCategories] = useState({})
  const [expandedSubjects, setExpandedSubjects] = useState({})
  const [expandedUnits, setExpandedUnits] = useState({})
  const [expandedSubunits, setExpandedSubunits] = useState({})
  const [viewMode, setViewMode] = useState('catalog')
  const contentRef = useRef(null)

  const mainCategories = [
    {
      id: 'public',
      name: '公共科目',
      icon: '📚',
      color: 'from-blue-50 to-blue-100',
      data: learningContent.publicSubjects
    },
    {
      id: 'pharmacy',
      name: '药学类专业科目',
      icon: '💊',
      color: 'from-green-50 to-green-100',
      data: learningContent.pharmacySubjects
    },
    {
      id: 'tcm',
      name: '中药学类专业科目',
      icon: '🌿',
      color: 'from-yellow-50 to-yellow-100',
      data: learningContent.tcmSubjects
    }
  ]

  const handleTopicComplete = (topicId) => {
    if (!completedTopics.includes(topicId)) {
      setCompletedTopics([...completedTopics, topicId])
    }
  }

  const handleBack = () => {
    if (viewMode === 'learning') {
      setViewMode('catalog')
      setSelectedTopic(null)
    } else if (selectedSubject) {
      setSelectedSubject(null)
    } else if (selectedCategory) {
      setSelectedCategory(null)
    }
  }

  const handlePracticeRecommendedCases = (relatedCases) => {
    if (onCaseRecommend && relatedCases && relatedCases.length > 0) {
      onCaseRecommend(relatedCases)
    }
  }

  const toggleCategory = (categoryId) => {
    setExpandedCategories(prev => ({
      ...prev,
      [categoryId]: !prev[categoryId]
    }))
  }

  const toggleSubject = (subjectId) => {
    setExpandedSubjects(prev => ({
      ...prev,
      [subjectId]: !prev[subjectId]
    }))
  }

  const toggleUnit = (unitId) => {
    setExpandedUnits(prev => ({
      ...prev,
      [unitId]: !prev[unitId]
    }))
  }

  const toggleSubunit = (subunitId) => {
    setExpandedSubunits(prev => ({
      ...prev,
      [subunitId]: !prev[subunitId]
    }))
  }

  const calculateProgress = (units) => {
    if (!units || !Array.isArray(units)) {
      return 0
    }
    
    let totalTopics = 0
    let completedCount = 0

    units.forEach(unit => {
      if (unit && unit.subunits && Array.isArray(unit.subunits)) {
        unit.subunits.forEach(subunit => {
          if (subunit && subunit.details && Array.isArray(subunit.details)) {
            subunit.details.forEach(detail => {
              totalTopics++
              if (completedTopics.includes(detail.id)) {
                completedCount++
              }
            })
          }
        })
      }
    })

    return totalTopics > 0 ? Math.round((completedCount / totalTopics) * 100) : 0
  }

  const handleSubjectClick = (subject) => {
    setSelectedSubject(subject)
    setViewMode('learning')
    if (subject.units && subject.units.length > 0 && subject.units[0].subunits && subject.units[0].subunits.length > 0) {
      const firstDetail = subject.units[0].subunits[0].details[0]
      if (firstDetail) {
        setSelectedTopic(firstDetail)
      }
    }
  }

  const handleTopicClick = (topic) => {
    setSelectedTopic(topic)
    if (contentRef.current) {
      contentRef.current.scrollTop = 0
    }
  }

  const handleScroll = () => {
    if (contentRef.current && selectedTopic && !completedTopics.includes(selectedTopic.id)) {
      const { scrollTop, scrollHeight, clientHeight } = contentRef.current
      const isAtBottom = scrollTop + clientHeight >= scrollHeight - 50
      
      if (isAtBottom) {
        handleTopicComplete(selectedTopic.id)
      }
    }
  }

  const getSubjectProgress = (subject) => {
    return calculateProgress(subject.units)
  }

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 bg-gradient-to-r from-indigo-400 to-purple-500 rounded-full flex items-center justify-center">
            <BookOpen className="w-6 h-6 text-white" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-gray-800">学习中心</h2>
            <p className="text-sm text-gray-500">专业知识学习 · 任务点完成</p>
          </div>
        </div>
        {viewMode === 'learning' && selectedSubject && (
          <div className="flex items-center gap-2">
            <span className="text-sm text-gray-600">已完成任务点</span>
            <div className="w-32 h-2 bg-gray-200 rounded-full overflow-hidden">
              <div 
                className="h-full bg-gradient-to-r from-green-400 to-green-600 transition-all duration-300"
                style={{ width: `${getSubjectProgress(selectedSubject)}%` }}
              />
            </div>
            <span className="text-sm font-bold text-green-600">{getSubjectProgress(selectedSubject)}%</span>
          </div>
        )}
      </div>

      {viewMode === 'catalog' && !selectedSubject ? (
        <div className="flex-1 overflow-y-auto">
          <div className="space-y-3">
            {mainCategories.map((category) => {
              const isExpanded = expandedCategories[category.id]
              return (
                <div
                  key={category.id}
                  className="border border-gray-200 rounded-lg overflow-hidden"
                >
                  <button
                    onClick={() => toggleCategory(category.id)}
                    className="w-full flex items-center justify-between p-4 bg-gradient-to-r from-gray-50 to-gray-100 hover:from-gray-100 hover:to-gray-150 transition-all"
                  >
                    <div className="flex items-center gap-3">
                      <span className="text-2xl">{category.icon}</span>
                      <div className="text-left">
                        <h4 className="font-semibold text-gray-800">{category.name}</h4>
                        <p className="text-sm text-gray-600">{category.data.subjects.length} 个科目</p>
                      </div>
                    </div>
                    {isExpanded ? (
                      <ChevronDown className="w-5 h-5 text-gray-600" />
                    ) : (
                      <ChevronRight className="w-5 h-5 text-gray-600" />
                    )}
                  </button>
                  {isExpanded && (
                    <div className="p-4 bg-white border-t border-gray-200">
                      <div className="space-y-2">
                        {category.data.subjects.map((subject) => {
                          const progress = calculateProgress(subject.units)
                          return (
                            <div
                              key={subject.id}
                              className="border border-gray-200 rounded-lg overflow-hidden"
                            >
                              <button
                                onClick={() => handleSubjectClick(subject)}
                                className="w-full flex items-center justify-between p-3 bg-gray-50 hover:bg-gray-100 transition-all"
                              >
                                <div className="flex items-center gap-2">
                                  <span className="text-xl">{subject.icon}</span>
                                  <span className="font-medium text-gray-800">{subject.name}</span>
                                </div>
                                <div className="flex items-center gap-2">
                                  <div className="text-right">
                                    <div className="text-sm text-gray-600">完成进度</div>
                                    <div className="text-lg font-bold text-indigo-600">{progress}%</div>
                                  </div>
                                  <ArrowRight className="w-5 h-5 text-gray-600" />
                                </div>
                              </button>
                            </div>
                          )
                        })}
                      </div>
                    </div>
                  )}
                </div>
              )
            })}
          </div>
        </div>
      ) : (
        <div className="flex-1 flex flex-col lg:flex-row overflow-hidden">
          <div className="w-full lg:w-80 border-r border-gray-200 flex flex-col border-b lg:border-b-0">
            <div className="p-4 border-b border-gray-200 bg-gray-50 flex-shrink-0">
              <button
                onClick={handleBack}
                className="flex items-center gap-2 text-gray-600 hover:text-gray-800 transition-colors w-full"
              >
                <ArrowRight className="w-4 h-4 rotate-180" />
                <span className="text-sm">返回目录</span>
              </button>
              <h3 className="text-lg font-bold text-gray-800 mt-3">{selectedSubject?.name}</h3>
              <p className="text-sm text-gray-600 mt-1">{selectedSubject?.units.length} 个大单元</p>
            </div>
            <div className="flex-1 overflow-y-auto p-2">
              {selectedSubject?.units.map((unit) => {
                const isExpanded = expandedUnits[unit.id]
                return (
                  <div key={unit.id} className="mb-2">
                    <button
                      onClick={() => toggleUnit(unit.id)}
                      className="w-full flex items-center justify-between p-2 bg-gray-50 hover:bg-gray-100 rounded-lg transition-all"
                    >
                      <div className="flex items-center gap-2">
                        <FolderOpen className="w-4 h-4 text-indigo-600" />
                        <span className="font-medium text-gray-800 text-sm">{unit.name}</span>
                      </div>
                      {isExpanded ? (
                        <ChevronDown className="w-4 h-4 text-gray-600" />
                      ) : (
                        <ChevronRight className="w-4 h-4 text-gray-600" />
                      )}
                    </button>
                    {isExpanded && unit.subunits && (
                      <div className="mt-1 ml-2 space-y-1">
                        {unit.subunits.map((subunit) => {
                          const isSubunitExpanded = expandedSubunits[subunit.id]
                          return (
                            <div key={subunit.id}>
                              <button
                                onClick={() => toggleSubunit(subunit.id)}
                                className="w-full flex items-center justify-between p-2 bg-white hover:bg-gray-50 rounded-lg transition-all"
                              >
                                <div className="flex items-center gap-2">
                                  <Folder className="w-3 h-3 text-purple-600" />
                                  <span className="text-sm text-gray-700">{subunit.name}</span>
                                </div>
                                {isSubunitExpanded ? (
                                  <ChevronDown className="w-3 h-3 text-gray-600" />
                                ) : (
                                  <ChevronRight className="w-3 h-3 text-gray-600" />
                                )}
                              </button>
                              {isSubunitExpanded && subunit.details && (
                                <div className="mt-1 ml-4 space-y-1">
                                  {subunit.details.map((detail) => {
                                    const isCompleted = completedTopics.includes(detail.id)
                                    const isSelected = selectedTopic?.id === detail.id
                                    return (
                                      <button
                                        key={detail.id}
                                        onClick={() => handleTopicClick(detail)}
                                        className={`w-full flex items-center gap-2 p-2 rounded-lg transition-all text-left ${
                                          isSelected
                                            ? 'bg-indigo-50 border-2 border-indigo-300'
                                            : 'bg-white border-2 border-gray-200 hover:border-indigo-300'
                                        }`}
                                      >
                                        <div className="flex-shrink-0">
                                          {isCompleted ? (
                                            <CheckCircle2 className="w-4 h-4 text-green-600" />
                                          ) : (
                                            <Circle className="w-4 h-4 text-gray-400" />
                                          )}
                                        </div>
                                        <span className={`text-sm ${isSelected ? 'font-semibold text-indigo-700' : 'text-gray-700'}`}>
                                          {detail.name}
                                        </span>
                                      </button>
                                    )
                                  })}
                                </div>
                              )}
                            </div>
                          )
                        })}
                      </div>
                    )}
                  </div>
                )
              })}
            </div>
          </div>
          <div className="flex-1 overflow-y-auto" ref={contentRef} onScroll={handleScroll}>
            {selectedTopic ? (
              <div className="p-6">
                <div className="bg-white rounded-lg border border-gray-200">
                  <div className="p-6 border-b border-gray-200">
                    <h3 className="text-xl font-bold text-gray-800 mb-2">{selectedTopic.name}</h3>
                    <div className="flex items-center gap-4">
                      {completedTopics.includes(selectedTopic.id) ? (
                        <div className="flex items-center gap-2 text-green-600">
                          <CheckCircle2 className="w-5 h-5" />
                          <span className="text-sm font-medium">已完成</span>
                        </div>
                      ) : (
                        <div className="flex items-center gap-2 text-gray-600">
                          <Circle className="w-5 h-5" />
                          <span className="text-sm">未完成</span>
                        </div>
                      )}
                    </div>
                  </div>
                  <div className="p-6">
                    {!completedTopics.includes(selectedTopic.id) && (
                      <div className="mb-4 p-3 bg-blue-50 border border-blue-200 rounded-lg text-sm text-blue-700">
                        💡 提示：滚动到内容底部会自动标记为已完成
                      </div>
                    )}
                    <div className="prose prose max-w-none space-y-6">
                      {selectedTopic.content.coreExplanation && (
                        <div dangerouslySetInnerHTML={{ __html: selectedTopic.content.coreExplanation }} />
                      )}
                    </div>
                  </div>
                  <div className="p-6 border-t border-gray-200 bg-gray-50">
                    <div className="flex flex-col gap-3">
                      {!completedTopics.includes(selectedTopic.id) && (
                        <button
                          onClick={() => handleTopicComplete(selectedTopic.id)}
                          className="w-full px-4 py-3 bg-indigo-500 text-white rounded-lg text-sm hover:bg-indigo-600 transition-all font-medium flex items-center justify-center gap-2"
                        >
                          <CheckCircle2 className="w-5 h-5" />
                          标记完成
                        </button>
                      )}
                    </div>
                  </div>
                </div>
              </div>
            ) : (
              <div className="flex items-center justify-center h-full text-gray-500">
                <div className="text-center">
                  <BookOpen className="w-16 h-16 mx-auto mb-4 text-gray-300" />
                  <p>请选择一个知识点开始学习</p>
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  )
}

export default LearningModule