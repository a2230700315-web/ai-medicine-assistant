import React from 'react'
import ReactECharts from 'echarts-for-react'
import { Award, Star, Trophy, Medal, TrendingUp } from 'lucide-react'

function ReviewModal({ reviewData, onClose }) {
  if (!reviewData) return null

  const scores = reviewData.scores || {}
  const totalScore = reviewData.totalScore || 0
  const originalScore = reviewData.originalTotalScore || totalScore
  const difficultyMultiplier = reviewData.difficultyMultiplier || 1.0
  const difficulty = reviewData.difficulty || 'medium'

  const radarData = [
    {
      name: '专业知识',
      value: scores.professionalKnowledge || 0,
      max: 25
    },
    {
      name: '沟通技巧',
      value: scores.communicationSkills || 0,
      max: 25
    },
    {
      name: '推销意识',
      value: scores.salesAwareness || 0,
      max: 25
    },
    {
      name: '合规性',
      value: scores.compliance || 0,
      max: 25
    }
  ]

  const getMedal = () => {
    if (totalScore >= 90) {
      return { icon: Trophy, title: '金牌药师', color: 'text-yellow-500' }
    } else if (totalScore >= 80) {
      return { icon: Medal, title: '银牌药师', color: 'text-gray-400' }
    } else if (totalScore >= 70) {
      return { icon: Star, title: '销售之星', color: 'text-blue-500' }
    } else if (totalScore >= 60) {
      return { icon: Award, title: '合格药师', color: 'text-green-500' }
    } else {
      return { icon: Award, title: '继续努力', color: 'text-orange-500' }
    }
  }

  const medal = getMedal()
  const MedalIcon = medal.icon

  const getOption = () => {
    return {
      tooltip: {
        trigger: 'item'
      },
      radar: {
        indicator: radarData.map(item => ({
          name: item.name,
          max: item.max
        })),
        radius: '65%',
        center: ['50%', '50%'],
        axisName: {
          color: '#666',
          fontSize: 14
        },
        splitArea: {
          areaStyle: {
            color: ['rgba(114, 172, 209, 0.1)', 'rgba(114, 172, 209, 0.2)']
          }
        },
        splitLine: {
          lineStyle: {
            color: 'rgba(114, 172, 209, 0.3)'
          }
        },
        axisLine: {
          lineStyle: {
            color: 'rgba(114, 172, 209, 0.3)'
          }
        }
      },
      series: [
        {
          name: '能力评估',
          type: 'radar',
          data: [
            {
              value: radarData.map(item => item.value),
              name: '当前表现',
              areaStyle: {
                color: 'rgba(114, 172, 209, 0.5)'
              },
              lineStyle: {
                color: '#72ACD1',
                width: 2
              },
              itemStyle: {
                color: '#72ACD1'
              }
            }
          ]
        }
      ]
    }
  }

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        <div className="p-6">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold text-gray-800">复盘分析报告</h2>
            <button
              onClick={onClose}
              className="text-gray-500 hover:text-gray-700 text-2xl font-bold"
            >
              ×
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <div className="bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl p-6">
              <div className="flex items-center justify-center mb-4">
                <div className={`bg-white rounded-full p-6 shadow-lg ${medal.color}`}>
                  <MedalIcon size={48} />
                </div>
              </div>
              <div className="text-center">
                <div className={`text-3xl font-bold mb-2 ${medal.color}`}>
                  {medal.title}
                </div>
                <div className="text-5xl font-bold text-gray-800 mb-2">
                  {totalScore}
                </div>
                <div className="text-gray-600">总分</div>
                
                {/* 难度信息 */}
                {difficultyMultiplier > 1.0 && (
                  <div className="mt-4 p-2 bg-white rounded-lg border border-gray-200">
                    <div className="text-sm text-gray-600">
                      <span className="font-medium">难度：</span>
                      <span className={`font-bold ${
                        difficulty === 'easy' ? 'text-green-600' : 
                        difficulty === 'medium' ? 'text-blue-600' : 
                        'text-red-600'
                      }`}>
                        {difficulty === 'easy' ? '简单' : difficulty === 'medium' ? '中等' : '困难'}
                      </span>
                    </div>
                    <div className="text-xs text-gray-500 mt-1">
                      原始得分：{originalScore} × {difficultyMultiplier.toFixed(1)}倍率
                    </div>
                  </div>
                )}
              </div>
            </div>

            <div className="bg-white rounded-xl p-6 border-2 border-purple-200">
              <div className="text-lg font-semibold text-gray-800 mb-4 text-center">
                能力雷达图
              </div>
              <ReactECharts
                option={getOption()}
                style={{ height: '300px', width: '100%' }}
              />
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <div className="bg-green-50 rounded-xl p-6">
              <h3 className="text-lg font-semibold text-green-800 mb-4 flex items-center gap-2">
                <Award className="w-5 h-5" />
                优点
              </h3>
              <ul className="space-y-2">
                {reviewData.advantages && reviewData.advantages.map((advantage, index) => (
                  <li key={index} className="flex items-start gap-2 text-green-700">
                    <span className="text-green-500 mt-1">✓</span>
                    <span>{advantage}</span>
                  </li>
                ))}
              </ul>
            </div>

            <div className="bg-orange-50 rounded-xl p-6">
              <h3 className="text-lg font-semibold text-orange-800 mb-4 flex items-center gap-2">
                <TrendingUp className="w-5 h-5" />
                改进建议
              </h3>
              <ul className="space-y-2">
                {reviewData.suggestions && reviewData.suggestions.map((suggestion, index) => (
                  <li key={index} className="flex items-start gap-2 text-orange-700">
                    <span className="text-orange-500 mt-1">→</span>
                    <span>{suggestion}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {reviewData.knowledgeBaseAnalysis && (
            <div className="bg-blue-50 rounded-xl p-6 mb-6">
              <h3 className="text-lg font-semibold text-blue-800 mb-4 flex items-center gap-2">
                <Star className="w-5 h-5" />
                知识库分析
              </h3>
              
              {reviewData.knowledgeBaseAnalysis.mentionedKeyPoints && reviewData.knowledgeBaseAnalysis.mentionedKeyPoints.length > 0 && (
                <div className="mb-4">
                  <h4 className="font-medium text-blue-700 mb-2">提到的关键点：</h4>
                  <ul className="space-y-1">
                    {reviewData.knowledgeBaseAnalysis.mentionedKeyPoints.map((point, index) => (
                      <li key={index} className="text-blue-600 flex items-start gap-2">
                        <span className="text-blue-400">•</span>
                        <span>{point}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {reviewData.knowledgeBaseAnalysis.missedKeyPoints && reviewData.knowledgeBaseAnalysis.missedKeyPoints.length > 0 && (
                <div className="mb-4">
                  <h4 className="font-medium text-blue-700 mb-2">遗漏的关键点：</h4>
                  <ul className="space-y-1">
                    {reviewData.knowledgeBaseAnalysis.missedKeyPoints.map((point, index) => (
                      <li key={index} className="text-blue-600 flex items-start gap-2">
                        <span className="text-blue-400">•</span>
                        <span>{point}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {reviewData.knowledgeBaseAnalysis.suggestedImprovements && reviewData.knowledgeBaseAnalysis.suggestedImprovements.length > 0 && (
                <div>
                  <h4 className="font-medium text-blue-700 mb-2">建议改进方向：</h4>
                  <ul className="space-y-1">
                    {reviewData.knowledgeBaseAnalysis.suggestedImprovements.map((suggestion, index) => (
                      <li key={index} className="text-blue-600 flex items-start gap-2">
                        <span className="text-blue-400">•</span>
                        <span>{suggestion}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}

          <div className="flex justify-end gap-3">
            <button
              onClick={onClose}
              className="px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-lg font-semibold hover:from-purple-700 hover:to-pink-700 transition-all"
            >
              关闭
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ReviewModal
