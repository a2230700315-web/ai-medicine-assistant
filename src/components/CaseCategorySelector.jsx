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
    <div className="bg-white rounded-xl shadow-lg p-4 h-full">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 bg-gradient-to-r from-purple-400 to-pink-500 rounded-lg flex items-center justify-center">
            <Stethoscope className="w-4 h-4 text-white" />
          </div>
          <h2 className="text-base font-bold text-gray-800">模拟案例库</h2>
        </div>
        {selectedCategory && (
          <button
            onClick={onBack}
            className="flex items-center gap-1 px-3 py-1.5 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all text-xs"
          >
            <ArrowLeft className="w-3 h-3" />
            返回
          </button>
        )}
      </div>

      <div className="grid grid-cols-2 gap-3">
        {categoryConfig.map((category) => {
          const Icon = category.icon
          const count = getCategoryCount(category.id)
          const isSelected = selectedCategory === category.id

          return (
            <button
              key={category.id}
              onClick={() => onCategorySelect(category.id)}
              className={`p-4 rounded-xl border-2 transition-all active:scale-95 ${
                isSelected
                  ? `border-transparent bg-gradient-to-r ${category.color} text-white shadow-lg`
                  : `border-gray-200 ${category.bgColor} hover:border-gray-300`
              }`}
            >
              <div className="flex flex-col items-center gap-2">
                <div className={`w-9 h-9 rounded-full flex items-center justify-center ${
                  isSelected ? 'bg-white bg-opacity-20' : `bg-gradient-to-r ${category.color}`
                }`}>
                  <Icon className="w-5 h-5 text-white" />
                </div>
                <h3 className={`text-sm font-bold ${isSelected ? 'text-white' : 'text-gray-800'}`}>
                  {category.name}
                </h3>
                <span className={`text-xs ${isSelected ? 'text-white text-opacity-90' : 'text-gray-500'}`}>
                  {count} 个案例
                </span>
              </div>
            </button>
          )
        })}
      </div>

      <div className="mt-4 p-3 bg-gradient-to-r from-purple-50 to-pink-50 rounded-lg">
        <p className="text-xs text-gray-600 text-center">
          总计 <span className="font-bold text-purple-600">{cases.length}</span> 个模拟案例
        </p>
      </div>
    </div>
  )
}

export default CaseCategorySelector
