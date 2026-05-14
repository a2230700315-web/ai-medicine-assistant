import { User, Activity, AlertTriangle, Pill, Utensils, Target, ArrowLeft, Play, Star } from 'lucide-react'
import { useState } from 'react'

function CaseDetail({ case_, onStartPractice, onBack }) {
  const [selectedDifficulty, setSelectedDifficulty] = useState('medium')
  const getBMICategory = (bmi) => {
    if (bmi < 18.5) return { label: '偏瘦', color: 'bg-blue-100 text-blue-600' }
    if (bmi < 24) return { label: '正常', color: 'bg-green-100 text-green-600' }
    if (bmi < 28) return { label: '超重', color: 'bg-orange-100 text-orange-600' }
    return { label: '肥胖', color: 'bg-red-100 text-red-600' }
  }

  const bmiCategory = getBMICategory(case_.bmi)

  return (
    <div className="bg-white rounded-xl shadow-lg p-4 flex flex-col">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <div className="w-9 h-9 bg-gradient-to-r from-blue-400 to-indigo-500 rounded-full flex items-center justify-center">
            <User className="w-4 h-4 text-white" />
          </div>
          <div>
            <h2 className="text-sm font-bold text-gray-800">{case_.name}</h2>
            <p className="text-xs text-gray-400">#{case_.id}</p>
          </div>
        </div>
        <button
          onClick={onBack}
          className="flex items-center gap-1 px-3 py-1.5 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all text-xs"
        >
          <ArrowLeft className="w-3 h-3" />
          返回
        </button>
      </div>

      <div className="space-y-3">
        <div className="grid grid-cols-3 gap-2">
          <div className="p-3 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl text-center">
            <p className="text-xs text-gray-500 mb-1">年龄</p>
            <p className="text-xl font-bold text-gray-800">{case_.age}</p>
            <p className="text-xs text-gray-400">岁</p>
          </div>
          <div className="p-3 bg-gradient-to-br from-green-50 to-emerald-50 rounded-xl text-center">
            <p className="text-xs text-gray-500 mb-1">BMI</p>
            <p className="text-xl font-bold text-gray-800">{case_.bmi}</p>
            <span className={`text-xs px-1.5 py-0.5 rounded-full ${bmiCategory.color}`}>{bmiCategory.label}</span>
          </div>
          <div className="p-3 bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl text-center">
            <p className="text-xs text-gray-500 mb-1">分类</p>
            <p className="text-xs font-bold text-gray-800 leading-tight">{case_.category}</p>
          </div>
        </div>

        {[
          { icon: AlertTriangle, color: 'text-orange-500', bg: 'from-orange-50 to-amber-50', label: '过敏史', value: case_.过敏史 || '无' },
          { icon: Activity, color: 'text-red-500', bg: 'from-red-50 to-rose-50', label: '现病史', value: case_.现病史 },
          { icon: Pill, color: 'text-blue-500', bg: 'from-blue-50 to-cyan-50', label: '目前用药', value: case_.目前用药 },
          { icon: Utensils, color: 'text-green-500', bg: 'from-green-50 to-teal-50', label: '饮食习惯', value: case_.饮食习惯 },
        ].map(({ icon: Icon, color, bg, label, value }) => (
          <div key={label} className={`p-3 bg-gradient-to-br ${bg} rounded-xl`}>
            <div className="flex items-center gap-1.5 mb-1.5">
              <Icon className={`w-3.5 h-3.5 ${color}`} />
              <h3 className="text-xs font-bold text-gray-700">{label}</h3>
            </div>
            <p className="text-xs text-gray-600 leading-relaxed">{value}</p>
          </div>
        ))}

        <div className="p-3 bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl border-2 border-purple-200">
          <div className="flex items-center gap-1.5 mb-1.5">
            <Target className="w-3.5 h-3.5 text-purple-500" />
            <h3 className="text-xs font-bold text-gray-700">销售目标</h3>
          </div>
          <p className="text-xs text-gray-700 leading-relaxed font-medium">{case_.销售目标}</p>
        </div>
      </div>

      <div className="mt-3 pt-3 border-t border-gray-200">
        <div className="mb-3">
          <div className="flex items-center gap-1.5 mb-2">
            <Star className="w-3.5 h-3.5 text-yellow-500" />
            <h3 className="text-xs font-semibold text-gray-700">选择难度</h3>
          </div>
          <div className="grid grid-cols-3 gap-2">
            {[
              { id: 'easy', label: '简单', sub: '新手', active: 'bg-green-500 text-white', inactive: 'bg-green-50 text-green-700' },
              { id: 'medium', label: '中等', sub: '实战', active: 'bg-blue-500 text-white', inactive: 'bg-blue-50 text-blue-700' },
              { id: 'hard', label: '困难', sub: '挑剔', active: 'bg-red-500 text-white', inactive: 'bg-red-50 text-red-700' },
            ].map(d => (
              <button
                key={d.id}
                onClick={() => setSelectedDifficulty(d.id)}
                className={`py-2 rounded-lg text-xs font-medium transition-all ${selectedDifficulty === d.id ? d.active + ' shadow-md' : d.inactive}`}
              >
                <div className="flex flex-col items-center">
                  <span>{d.label}</span>
                  <span className="text-xs opacity-70">{d.sub}</span>
                </div>
              </button>
            ))}
          </div>
        </div>

        <button
          onClick={() => onStartPractice(case_, selectedDifficulty)}
          className="w-full py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-xl hover:from-blue-600 hover:to-indigo-700 transition-all font-bold text-sm flex items-center justify-center gap-2 shadow-md"
        >
          <Play className="w-4 h-4" />
          开始模拟练习
        </button>
      </div>
    </div>
  )
}

export default CaseDetail
