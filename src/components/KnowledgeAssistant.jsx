import { useState } from 'react'
import { BookOpen, Lightbulb, ChevronRight, EyeOff } from 'lucide-react'

function KnowledgeAssistant({ examMode = false }) {
  const [selectedCategory, setSelectedCategory] = useState('selling')

  const categories = [
    { id: 'selling', name: '销售技巧', icon: Lightbulb },
    { id: 'products', name: '产品卖点', icon: BookOpen }
  ]

  const sellingTips = [
    {
      title: '益生菌卖点',
      content: [
        '调节肠道菌群平衡',
        '增强免疫力',
        '改善消化功能',
        '适合各年龄段人群'
      ]
    },
    {
      title: '联合用药公式',
      content: [
        '感冒药 + 维生素C：加速康复',
        '钙片 + 维生素D3：促进吸收',
                        '益生菌 + 益生元：协同增效',
        '止痛药 + 胃黏膜保护剂：减少刺激'
      ]
    },
    {
      title: '沟通技巧',
      content: [
        '先倾听再推荐',
        '用专业术语建立信任',
        '强调产品独特优势',
        '提供多种选择方案'
      ]
    }
  ]

  const productInfo = [
    {
      name: '益生菌',
      category: '保健品',
      keyPoints: ['调节肠道', '增强免疫', '改善消化'],
      targetCustomers: ['肠胃不适', '免疫力低下', '老人儿童']
    },
    {
      name: '维生素C',
      category: '维生素',
      keyPoints: ['抗氧化', '增强免疫', '促进吸收'],
      targetCustomers: ['易感冒', '压力大', '饮食不均衡']
    },
    {
      name: '钙片',
      category: '矿物质',
      keyPoints: ['强健骨骼', '预防骨质疏松', '促进发育'],
      targetCustomers: ['中老年', '青少年', '孕妇']
    }
  ]

  if (examMode) {
    return (
      <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col items-center justify-center">
        <div className="text-center">
          <EyeOff className="w-12 h-12 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-700">考试模式已启用</h3>
          <p className="text-sm text-gray-500 mt-2">药店知识助手已隐藏</p>
        </div>
      </div>
    )
  }

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 h-full overflow-y-auto">
      <div className="flex items-center gap-3 mb-6">
        <div className="w-10 h-10 bg-gradient-to-r from-purple-400 to-pink-500 rounded-lg flex items-center justify-center">
          <BookOpen className="w-5 h-5 text-white" />
        </div>
        <h2 className="text-xl font-bold text-gray-800">药店知识助手</h2>
      </div>

      <div className="flex gap-2 mb-6">
        {categories.map((category) => {
          const Icon = category.icon
          return (
            <button
              key={category.id}
              onClick={() => setSelectedCategory(category.id)}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
                selectedCategory === category.id
                  ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white'
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              <Icon className="w-4 h-4" />
              <span className="text-sm font-medium">{category.name}</span>
            </button>
          )
        })}
      </div>

      <div className="space-y-4">
        {selectedCategory === 'selling' ? (
          sellingTips.map((tip, index) => (
            <div key={index} className="border border-gray-200 rounded-lg overflow-hidden">
              <div className="bg-gradient-to-r from-purple-50 to-pink-50 px-4 py-3 flex items-center justify-between">
                <h3 className="font-semibold text-gray-800">{tip.title}</h3>
                <ChevronRight className="w-4 h-4 text-gray-400" />
              </div>
              <ul className="p-4 space-y-2">
                {tip.content.map((item, idx) => (
                  <li key={idx} className="flex items-start gap-2 text-sm text-gray-600">
                    <span className="w-1.5 h-1.5 bg-purple-500 rounded-full mt-1.5 flex-shrink-0" />
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          ))
        ) : (
          productInfo.map((product, index) => (
            <div key={index} className="border border-gray-200 rounded-lg overflow-hidden">
              <div className="bg-gradient-to-r from-purple-50 to-pink-50 px-4 py-3">
                <div className="flex items-center justify-between">
                  <h3 className="font-semibold text-gray-800">{product.name}</h3>
                  <span className="text-xs bg-purple-100 text-purple-600 px-2 py-1 rounded-full">
                    {product.category}
                  </span>
                </div>
              </div>
              <div className="p-4 space-y-3">
                <div>
                  <p className="text-xs font-medium text-gray-500 mb-2">核心卖点</p>
                  <div className="flex flex-wrap gap-2">
                    {product.keyPoints.map((point, idx) => (
                      <span
                        key={idx}
                        className="text-xs bg-blue-50 text-blue-600 px-2 py-1 rounded"
                      >
                        {point}
                      </span>
                    ))}
                  </div>
                </div>
                <div>
                  <p className="text-xs font-medium text-gray-500 mb-2">适用人群</p>
                  <div className="flex flex-wrap gap-2">
                    {product.targetCustomers.map((customer, idx) => (
                      <span
                        key={idx}
                        className="text-xs bg-green-50 text-green-600 px-2 py-1 rounded"
                      >
                        {customer}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  )
}

export default KnowledgeAssistant
