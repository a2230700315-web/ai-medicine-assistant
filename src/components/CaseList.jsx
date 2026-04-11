import { User, Calendar, Activity, AlertTriangle, Pill, Utensils, Target, CheckCircle, Star } from 'lucide-react'
import { getCaseProgress, getMedal } from '../utils/progressStorage'

function CaseList({ cases, category, onCaseSelect, onBack }) {
  const categoryMap = {
    'high_blood_sugar': '高血糖',
    'high_blood_pressure': '高血压',
    'high_blood_lipids': '高血脂',
    'high_uric_acid': '高尿酸',
    'tcm_internal': '中医内科',
    'digestive': '消化内科'
  }

  const categoryName = categoryMap[category] || category
  const filteredCases = cases.filter(c => c.category === categoryName)

  const getBMICategory = (bmi) => {
    if (bmi < 18.5) return { label: '偏瘦', color: 'text-blue-600' }
    if (bmi < 24) return { label: '正常', color: 'text-green-600' }
    if (bmi < 28) return { label: '超重', color: 'text-orange-600' }
    return { label: '肥胖', color: 'text-red-600' }
  }

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 h-full flex flex-col">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h2 className="text-xl font-bold text-gray-800">{categoryName}案例</h2>
          <p className="text-sm text-gray-500 mt-1">共 {filteredCases.length} 个案例</p>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto space-y-4">
        {filteredCases.map((case_) => {
          const progress = getCaseProgress(case_.id)
          const medal = progress ? getMedal(progress.score) : null
          
          return (
            <button
              key={case_.id}
              onClick={() => onCaseSelect(case_)}
              className="w-full p-4 bg-gray-50 rounded-xl border-2 border-gray-200 hover:border-blue-400 hover:shadow-md transition-all text-left group relative"
            >
              {medal && (
                <div className={`absolute top-2 right-2 px-2 py-1 rounded-full text-xs font-bold ${medal.color} bg-white shadow-md`}>
                  {medal.icon} {medal.title}
                </div>
              )}
              
              <div className="flex items-start gap-4">
                <div className="w-12 h-12 bg-gradient-to-r from-blue-400 to-indigo-500 rounded-full flex items-center justify-center flex-shrink-0">
                  <User className="w-6 h-6 text-white" />
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 mb-2">
                    <h3 className="font-bold text-gray-800 group-hover:text-blue-600 transition-colors">
                      {case_.name}
                    </h3>
                    <span className="text-xs bg-blue-100 text-blue-600 px-2 py-0.5 rounded-full">
                      {case_.age}岁
                    </span>
                    {progress && (
                      <div className="flex items-center gap-1 text-xs text-green-600">
                        <CheckCircle className="w-3 h-3" />
                        <span>{progress.score}分</span>
                      </div>
                    )}
                  </div>

                <div className="grid grid-cols-2 gap-2 text-sm">
                  <div className="flex items-center gap-2 text-gray-600">
                    <Activity className="w-4 h-4 text-gray-400" />
                    <span>BMI: {case_.bmi}</span>
                    <span className={`text-xs font-medium ${getBMICategory(case_.bmi).color}`}>
                      ({getBMICategory(case_.bmi).label})
                    </span>
                  </div>
                  {case_.过敏史 && case_.过敏史 !== '无' && (
                    <div className="flex items-center gap-2 text-gray-600">
                      <AlertTriangle className="w-4 h-4 text-orange-400" />
                      <span className="text-xs text-orange-600">有过敏史</span>
                    </div>
                  )}
                </div>

                <div className="mt-3 p-2 bg-white rounded-lg">
                  <p className="text-xs text-gray-500 line-clamp-2">
                    {case_.现病史}
                  </p>
                </div>

                <div className="mt-3 flex items-center gap-2 text-xs text-gray-500">
                  <Target className="w-3 h-3 text-purple-400" />
                  <span className="truncate">{case_.销售目标}</span>
                </div>
              </div>
            </div>
          </button>
          )
        })}
      </div>

      <div className="mt-4 pt-4 border-t border-gray-200">
        <button
          onClick={onBack}
          className="w-full py-3 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all font-medium"
        >
          返回分类选择
        </button>
      </div>
    </div>
  )
}

export default CaseList
