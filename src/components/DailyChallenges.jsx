import { useState } from 'react'
import { Target, CheckCircle, Circle } from 'lucide-react'

function DailyChallenges({ completedChallenges, onToggleChallenge }) {
  const challenges = [
    { id: 1, title: '成功推荐益生菌', description: '向顾客介绍益生菌的益处并完成推荐' },
    { id: 2, title: '联合用药推荐', description: '为感冒顾客推荐感冒药+维生素C的组合' },
    { id: 3, title: '建立信任关系', description: '通过专业建议获得顾客信任' }
  ]

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 h-full">
      <div className="flex items-center gap-3 mb-6">
        <div className="w-10 h-10 bg-gradient-to-r from-orange-400 to-red-500 rounded-lg flex items-center justify-center">
          <Target className="w-5 h-5 text-white" />
        </div>
        <h2 className="text-xl font-bold text-gray-800">今日挑战任务</h2>
      </div>

      <div className="space-y-4">
        {challenges.map((challenge) => (
          <div
            key={challenge.id}
            className={`p-4 rounded-lg border-2 transition-all cursor-pointer ${
              completedChallenges.includes(challenge.id)
                ? 'bg-green-50 border-green-300'
                : 'bg-gray-50 border-gray-200 hover:border-blue-300'
            }`}
            onClick={() => onToggleChallenge(challenge.id)}
          >
            <div className="flex items-start gap-3">
              <button className="mt-1">
                {completedChallenges.includes(challenge.id) ? (
                  <CheckCircle className="w-6 h-6 text-green-500" />
                ) : (
                  <Circle className="w-6 h-6 text-gray-300" />
                )}
              </button>
              <div className="flex-1">
                <h3 className="font-semibold text-gray-800">{challenge.title}</h3>
                <p className="text-sm text-gray-600 mt-1">{challenge.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-6 p-4 bg-blue-50 rounded-lg">
        <div className="flex items-center justify-between">
          <span className="text-sm text-gray-600">完成进度</span>
          <span className="text-sm font-bold text-blue-600">
            {completedChallenges.length} / {challenges.length}
          </span>
        </div>
        <div className="w-full bg-blue-200 rounded-full h-2 mt-2">
          <div
            className="bg-gradient-to-r from-blue-500 to-indigo-600 h-2 rounded-full transition-all"
            style={{ width: `${(completedChallenges.length / challenges.length) * 100}%` }}
          />
        </div>
      </div>
    </div>
  )
}

export default DailyChallenges
