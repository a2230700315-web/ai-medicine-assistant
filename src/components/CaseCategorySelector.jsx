import { useState } from 'react'
import { Droplet, Heart, Activity, Flame, Leaf, Stethoscope, ArrowLeft } from 'lucide-react'

const categoryConfig = [
  { id: 'high_blood_sugar', name: '高血糖', icon: Droplet, color: 'from-red-400 to-pink-500', bgColor: 'bg-red-50' },
  { id: 'high_blood_pressure', name: '高血压', icon: Heart, color: 'from-rose-400 to-red-500', bgColor: 'bg-rose-50' },
  { id: 'high_blood_lipids', name: '高血脂', icon: Activity, color: 'from-orange-400 to-amber-500', bgColor: 'bg-orange-50' },
  { id: 'high_uric_acid', name: '高尿酸', icon: Flame, color: 'from-yellow-400 to-orange-500', bgColor: 'bg-yellow-50' },
  { id: 'tcm_internal', name: '中医内科', icon: Leaf, color: 'from-green-400 to-emerald-500', bgColor: 'bg-green-50' },
  { id: 'digestive', name: '消化内科', icon: Stethoscope, color: 'from-blue-400 to-cyan-500', bgColor: 'bg-blue-50' }
]

function CaseCategorySelector({ cases, onCategorySelect, selectedCategory, onBack }) {
  const getCategoryCount = (categoryId) => {
    return cases.filter(c => c.category === categoryConfig.find(cat => cat.id === categoryId)?.name).length
  }

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 h-full">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-gradient-to-r from-purple-400 to-pink-500 rounded-lg flex items-center justify-center">
            <Stethoscope className="w-5 h-5 text-white" />
          </div>
          <h2 className="text-xl font-bold text-gray-800">模拟案例库</h2>
        </div>
        {selectedCategory && (
          <button
            onClick={onBack}
            className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
          >
            <ArrowLeft className="w-4 h-4" />
            <span className="text-sm">返回</span>
          </button>
        )}
      </div>

      <div className="grid grid-cols-2 gap-4">
        {categoryConfig.map((category) => {
          const Icon = category.icon
          const count = getCategoryCount(category.id)
          const isSelected = selectedCategory === category.id

          return (
            <button
              key={category.id}
              onClick={() => onCategorySelect(category.id)}
              className={`p-6 rounded-xl border-2 transition-all hover:scale-105 ${
                isSelected
                  ? `border-transparent bg-gradient-to-r ${category.color} text-white shadow-lg`
                  : `border-gray-200 ${category.bgColor} hover:border-gray-300`
              }`}
            >
              <div className="flex flex-col items-center gap-3">
                <div className={`w-12 h-12 rounded-full flex items-center justify-center ${
                  isSelected ? 'bg-white bg-opacity-20' : `bg-gradient-to-r ${category.color}`
                }`}>
                  <Icon className={`w-6 h-6 ${isSelected ? 'text-white' : 'text-white'}`} />
                </div>
                <h3 className={`font-bold ${isSelected ? 'text-white' : 'text-gray-800'}`}>
                  {category.name}
                </h3>
                <span className={`text-sm ${isSelected ? 'text-white text-opacity-90' : 'text-gray-500'}`}>
                  {count} 个案例
                </span>
              </div>
            </button>
          )
        })}
      </div>

      <div className="mt-6 p-4 bg-gradient-to-r from-purple-50 to-pink-50 rounded-lg">
        <p className="text-sm text-gray-600 text-center">
          总计 <span className="font-bold text-purple-600">{cases.length}</span> 个模拟案例
        </p>
      </div>
    </div>
  )
}

export default CaseCategorySelector
