import { useState, useEffect } from 'react'
import { BookOpen, Lightbulb, ChevronDown, ChevronRight, EyeOff } from 'lucide-react'
import { getKnowledgeForCase } from '../data/caseKnowledge'

function KnowledgeAssistant({ examMode = false, practiceCase = null }) {
  const [selectedCategory, setSelectedCategory] = useState('selling')
  const [expandedTip, setExpandedTip] = useState(0)
  const [knowledge, setKnowledge] = useState(() => getKnowledgeForCase(null))

  useEffect(() => {
    setKnowledge(getKnowledgeForCase(practiceCase))
    setExpandedTip(0)
  }, [practiceCase?.id, practiceCase?.category])

  const categories = [
    { id: 'selling', name: '销售话术', icon: Lightbulb },
    { id: 'products', name: '产品卖点', icon: BookOpen }
  ]

  const getCategoryLabel = () => {
    if (!practiceCase) return null
    return practiceCase.category || null
  }

  if (examMode) {
    return (
      <div className="bg-white rounded-xl shadow-lg p-4 md:p-6 h-full flex flex-col items-center justify-center">
        <div className="text-center">
          <EyeOff className="w-12 h-12 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-700">考试模式已启用</h3>
          <p className="text-sm text-gray-500 mt-2">药店知识助手已隐藏</p>
        </div>
      </div>
    )
  }

  const label = getCategoryLabel()

  return (
    <div className="bg-white rounded-xl shadow-lg p-3 md:p-6 h-full overflow-y-auto">
      <div className="flex items-center gap-2 md:gap-3 mb-4">
        <div className="w-9 h-9 md:w-10 md:h-10 bg-gradient-to-r from-purple-400 to-pink-500 rounded-lg flex items-center justify-center flex-shrink-0">
          <BookOpen className="w-4 h-4 md:w-5 md:h-5 text-white" />
        </div>
        <div className="min-w-0">
          <h2 className="text-base md:text-lg font-bold text-gray-800 leading-tight">药店知识助手</h2>
          {label && (
            <span className="text-xs px-2 py-0.5 bg-purple-100 text-purple-600 rounded-full">
              {label}
            </span>
          )}
        </div>
      </div>

      {!practiceCase && (
        <div className="mb-3 p-2 bg-amber-50 border border-amber-200 rounded-lg text-xs text-amber-700">
          💡 选择左侧案例后，知识助手会自动更新对应内容
        </div>
      )}

      <div className="flex gap-2 mb-4">
        {categories.map((category) => {
          const Icon = category.icon
          return (
            <button
              key={category.id}
              onClick={() => setSelectedCategory(category.id)}
              className={`flex-1 flex items-center justify-center gap-1.5 px-3 py-2 rounded-lg transition-all text-sm ${
                selectedCategory === category.id
                  ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white shadow-sm'
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              <Icon className="w-3.5 h-3.5 flex-shrink-0" />
              <span className="font-medium">{category.name}</span>
            </button>
          )
        })}
      </div>

      <div className="space-y-2">
        {selectedCategory === 'selling' ? (
          knowledge.sellingTips.map((tip, index) => (
            <div key={index} className="border border-gray-200 rounded-lg overflow-hidden">
              <button
                onClick={() => setExpandedTip(expandedTip === index ? -1 : index)}
                className="w-full flex items-center justify-between px-3 py-2.5 bg-gradient-to-r from-purple-50 to-pink-50 hover:from-purple-100 hover:to-pink-100 transition-all"
              >
                <h3 className="font-semibold text-gray-800 text-sm text-left">{tip.title}</h3>
                {expandedTip === index
                  ? <ChevronDown className="w-4 h-4 text-purple-500 flex-shrink-0" />
                  : <ChevronRight className="w-4 h-4 text-gray-400 flex-shrink-0" />
                }
              </button>
              {expandedTip === index && (
                <ul className="px-3 py-2 space-y-2 bg-white">
                  {tip.content.map((item, idx) => (
                    <li key={idx} className="flex items-start gap-2 text-sm text-gray-700">
                      <span className="w-1.5 h-1.5 bg-purple-400 rounded-full mt-1.5 flex-shrink-0" />
                      <span className="leading-relaxed">{item}</span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          ))
        ) : (
          knowledge.products.map((product, index) => (
            <div key={index} className="border border-gray-200 rounded-lg overflow-hidden">
              <div className="bg-gradient-to-r from-purple-50 to-pink-50 px-3 py-2.5">
                <div className="flex items-center justify-between">
                  <h3 className="font-semibold text-gray-800 text-sm">{product.name}</h3>
                  <span className="text-xs bg-purple-100 text-purple-600 px-2 py-0.5 rounded-full flex-shrink-0 ml-2">
                    {product.category}
                  </span>
                </div>
              </div>
              <div className="px-3 py-2 space-y-2 bg-white">
                <div>
                  <p className="text-xs font-medium text-gray-500 mb-1">核心卖点</p>
                  <div className="flex flex-wrap gap-1">
                    {product.keyPoints.map((point, idx) => (
                      <span key={idx} className="text-xs bg-blue-50 text-blue-600 px-2 py-0.5 rounded">
                        {point}
                      </span>
                    ))}
                  </div>
                </div>
                <div>
                  <p className="text-xs font-medium text-gray-500 mb-1">适用人群</p>
                  <div className="flex flex-wrap gap-1">
                    {product.targetCustomers.map((customer, idx) => (
                      <span key={idx} className="text-xs bg-green-50 text-green-600 px-2 py-0.5 rounded">
                        {customer}
                      </span>
                    ))}
                  </div>
                </div>
                {product.combo && (
                  <div className="flex items-start gap-1.5 mt-1 p-2 bg-orange-50 rounded text-xs text-orange-700">
                    <span className="flex-shrink-0">💊</span>
                    <span>{product.combo}</span>
                  </div>
                )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  )
}

export default KnowledgeAssistant
