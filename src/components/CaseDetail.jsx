import { User, Calendar, Activity, AlertTriangle, Pill, Utensils, Target, ArrowLeft, Play, Star } from 'lucide-react'
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
    <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 bg-gradient-to-r from-blue-400 to-indigo-500 rounded-full flex items-center justify-center">
            <User className="w-6 h-6 text-white" />
          </div>
          <div>
            <h2 className="text-xl font-bold text-gray-800">{case_.name}</h2>
            <p className="text-sm text-gray-500">案例编号: #{case_.id}</p>
          </div>
        </div>
        <button
          onClick={onBack}
          className="flex items-center gap-2 px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
        >
          <ArrowLeft className="w-4 h-4" />
          <span className="text-sm">返回</span>
        </button>
      </div>

      <div className="flex-1 overflow-y-auto space-y-4">
        <div className="grid grid-cols-3 gap-4">
          <div className="p-4 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl">
            <div className="flex items-center gap-2 mb-2">
              <Calendar className="w-4 h-4 text-blue-500" />
              <span className="text-xs text-gray-500">年龄</span>
            </div>
            <p className="text-2xl font-bold text-gray-800">{case_.age}</p>
            <p className="text-xs text-gray-500">岁</p>
          </div>

          <div className="p-4 bg-gradient-to-br from-green-50 to-emerald-50 rounded-xl">
            <div className="flex items-center gap-2 mb-2">
              <Activity className="w-4 h-4 text-green-500" />
              <span className="text-xs text-gray-500">BMI</span>
            </div>
            <p className="text-2xl font-bold text-gray-800">{case_.bmi}</p>
            <span className={`text-xs px-2 py-0.5 rounded-full ${bmiCategory.color}`}>
              {bmiCategory.label}
            </span>
          </div>

          <div className="p-4 bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl">
            <div className="flex items-center gap-2 mb-2">
              <Pill className="w-4 h-4 text-purple-500" />
              <span className="text-xs text-gray-500">分类</span>
            </div>
            <p className="text-lg font-bold text-gray-800">{case_.category}</p>
          </div>
        </div>

        <div className="p-4 bg-gradient-to-br from-orange-50 to-amber-50 rounded-xl">
          <div className="flex items-center gap-2 mb-3">
            <AlertTriangle className="w-5 h-5 text-orange-500" />
            <h3 className="font-bold text-gray-800">过敏史</h3>
          </div>
          <p className="text-gray-700">{case_.过敏史 || '无'}</p>
        </div>

        <div className="p-4 bg-gradient-to-br from-red-50 to-rose-50 rounded-xl">
          <div className="flex items-center gap-2 mb-3">
            <Activity className="w-5 h-5 text-red-500" />
            <h3 className="font-bold text-gray-800">现病史</h3>
          </div>
          <p className="text-gray-700 leading-relaxed">{case_.现病史}</p>
        </div>

        <div className="p-4 bg-gradient-to-br from-blue-50 to-cyan-50 rounded-xl">
          <div className="flex items-center gap-2 mb-3">
            <Pill className="w-5 h-5 text-blue-500" />
            <h3 className="font-bold text-gray-800">目前用药</h3>
          </div>
          <p className="text-gray-700 leading-relaxed">{case_.目前用药}</p>
        </div>

        <div className="p-4 bg-gradient-to-br from-green-50 to-teal-50 rounded-xl">
          <div className="flex items-center gap-2 mb-3">
            <Utensils className="w-5 h-5 text-green-500" />
            <h3 className="font-bold text-gray-800">饮食习惯</h3>
          </div>
          <p className="text-gray-700 leading-relaxed">{case_.饮食习惯}</p>
        </div>

        <div className="p-4 bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl border-2 border-purple-200">
          <div className="flex items-center gap-2 mb-3">
            <Target className="w-5 h-5 text-purple-500" />
            <h3 className="font-bold text-gray-800">销售目标</h3>
          </div>
          <p className="text-gray-700 leading-relaxed font-medium">{case_.销售目标}</p>
        </div>
      </div>

      <div className="mt-6 pt-4 border-t border-gray-200">
        {/* 难度选择 */}
        <div className="mb-6">
          <h3 className="text-lg font-semibold text-gray-800 mb-3 flex items-center gap-2">
            <Star className="w-5 h-5 text-yellow-500" />
            选择对话难度
          </h3>
          <div className="grid grid-cols-3 gap-2">
            <button
              onClick={() => setSelectedDifficulty('easy')}
              className={`p-3 rounded-lg text-sm font-medium transition-all ${
                selectedDifficulty === 'easy'
                  ? 'bg-green-500 text-white shadow-md'
                  : 'bg-green-50 text-green-700 hover:bg-green-100'
              }`}
            >
              <div className="flex flex-col items-center">
                <span>简单</span>
                <span className="text-xs opacity-80">新手</span>
              </div>
            </button>
            <button
              onClick={() => setSelectedDifficulty('medium')}
              className={`p-3 rounded-lg text-sm font-medium transition-all ${
                selectedDifficulty === 'medium'
                  ? 'bg-blue-500 text-white shadow-md'
                  : 'bg-blue-50 text-blue-700 hover:bg-blue-100'
              }`}
            >
              <div className="flex flex-col items-center">
                <span>中等</span>
                <span className="text-xs opacity-80">实战</span>
              </div>
            </button>
            <button
              onClick={() => setSelectedDifficulty('hard')}
              className={`p-3 rounded-lg text-sm font-medium transition-all ${
                selectedDifficulty === 'hard'
                  ? 'bg-red-500 text-white shadow-md'
                  : 'bg-red-50 text-red-700 hover:bg-red-100'
              }`}
            >
              <div className="flex flex-col items-center">
                <span>困难</span>
                <span className="text-xs opacity-80">挑剔</span>
              </div>
            </button>
          </div>
          <p className="text-xs text-gray-500 mt-2 text-center">
            {selectedDifficulty === 'easy' && '顾客信任度高，容易被说服'}
            {selectedDifficulty === 'medium' && '正常顾客，会对价格和副作用有疑问'}
            {selectedDifficulty === 'hard' && '极度专业且敏感，难以建立信任'}
          </p>
        </div>

        <button
          onClick={() => onStartPractice(case_, selectedDifficulty)}
          className="w-full py-4 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-xl hover:from-blue-600 hover:to-indigo-700 transition-all font-bold text-lg flex items-center justify-center gap-3 shadow-lg hover:shadow-xl transform hover:scale-[1.02]"
        >
          <Play className="w-6 h-6" />
          开始模拟练习
        </button>
      </div>
    </div>
  )
}

export default CaseDetail
