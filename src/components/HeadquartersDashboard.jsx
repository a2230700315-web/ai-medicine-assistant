import { useState } from 'react'
import ReactECharts from 'echarts-for-react'
import { Building2, Users, TrendingUp, Award, Activity, Target, Clock, MapPin } from 'lucide-react'
import { mockHeadquartersData, mockStores } from '../data/mockData'

function HeadquartersDashboard() {
  const [activeView, setActiveView] = useState('overview')
  const data = mockHeadquartersData

  const rankingOption = {
    title: {
      text: '门店排行榜 TOP 10',
      left: 'center',
      textStyle: { fontSize: 16, fontWeight: 'bold' }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' }
    },
    legend: {
      data: ['学习进度', '预测通过率'],
      bottom: 0
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '15%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: data.storeRankings.map(s => s.name.replace('店', '')),
      axisLabel: { rotate: 30, fontSize: 10 }
    },
    yAxis: [
      {
        type: 'value',
        name: '进度%',
        max: 100,
        axisLabel: { formatter: '{value}' }
      },
      {
        type: 'value',
        name: '通过率%',
        max: 100,
        axisLabel: { formatter: '{value}' }
      }
    ],
    series: [
      {
        name: '学习进度',
        type: 'bar',
        data: data.storeRankings.map(s => s.progress),
        itemStyle: {
          color: {
            type: 'linear',
            x: 0, y: 0, x2: 0, y2: 1,
            colorStops: [
              { offset: 0, color: '#3B82F6' },
              { offset: 1, color: '#1D4ED8' }
            ]
          },
          borderRadius: [4, 4, 0, 0]
        }
      },
      {
        name: '预测通过率',
        type: 'line',
        yAxisIndex: 1,
        data: data.storeRankings.map(s => s.passRate),
        smooth: true,
        symbol: 'circle',
        symbolSize: 8,
        lineStyle: { color: '#10B981', width: 3 },
        itemStyle: { color: '#10B981' }
      }
    ]
  }

  const regionOption = {
    title: {
      text: '各区业绩对比',
      left: 'center',
      textStyle: { fontSize: 16, fontWeight: 'bold' }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' }
    },
    legend: {
      data: ['门店数', '平均进度', '通过率'],
      bottom: 0
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '15%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: data.regionStats.map(r => r.region)
    },
    yAxis: [
      {
        type: 'value',
        name: '数量',
        axisLabel: { formatter: '{value}' }
      },
      {
        type: 'value',
        name: '%',
        max: 100,
        axisLabel: { formatter: '{value}' }
      }
    ],
    series: [
      {
        name: '门店数',
        type: 'bar',
        data: data.regionStats.map(r => r.storeCount),
        itemStyle: { color: '#8B5CF6', borderRadius: [4, 4, 0, 0] }
      },
      {
        name: '平均进度',
        type: 'bar',
        data: data.regionStats.map(r => r.averageProgress),
        itemStyle: { color: '#3B82F6', borderRadius: [4, 4, 0, 0] }
      },
      {
        name: '通过率',
        type: 'line',
        yAxisIndex: 1,
        data: data.regionStats.map(r => r.passRate),
        smooth: true,
        lineStyle: { color: '#F59E0B', width: 3 },
        itemStyle: { color: '#F59E0B' }
      }
    ]
  }

  const trendOption = {
    title: {
      text: '月度趋势分析',
      left: 'center',
      textStyle: { fontSize: 16, fontWeight: 'bold' }
    },
    tooltip: {
      trigger: 'axis'
    },
    legend: {
      data: ['活跃用户', '平均进度', '预测通过率'],
      bottom: 0
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '15%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: data.monthlyTrend.map(m => m.month.replace('2024-', '24年').replace('2025-', '25年') + '月')
    },
    yAxis: [
      {
        type: 'value',
        name: '人数',
        axisLabel: { formatter: '{value}' }
      },
      {
        type: 'value',
        name: '%',
        max: 100,
        axisLabel: { formatter: '{value}' }
      }
    ],
    series: [
      {
        name: '活跃用户',
        type: 'line',
        data: data.monthlyTrend.map(m => m.activeUsers),
        smooth: true,
        areaStyle: {
          color: {
            type: 'linear',
            x: 0, y: 0, x2: 0, y2: 1,
            colorStops: [
              { offset: 0, color: 'rgba(59, 130, 246, 0.3)' },
              { offset: 1, color: 'rgba(59, 130, 246, 0.05)' }
            ]
          }
        },
        lineStyle: { color: '#3B82F6', width: 3 },
        itemStyle: { color: '#3B82F6' }
      },
      {
        name: '平均进度',
        type: 'line',
        yAxisIndex: 1,
        data: data.monthlyTrend.map(m => m.avgProgress),
        smooth: true,
        lineStyle: { color: '#10B981', width: 3 },
        itemStyle: { color: '#10B981' }
      },
      {
        name: '预测通过率',
        type: 'line',
        yAxisIndex: 1,
        data: data.monthlyTrend.map(m => m.passRate),
        smooth: true,
        lineStyle: { color: '#F59E0B', width: 3 },
        itemStyle: { color: '#F59E0B' }
      }
    ]
  }

  const subjectOption = {
    title: {
      text: '各科目成绩分析',
      left: 'center',
      textStyle: { fontSize: 16, fontWeight: 'bold' }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' }
    },
    legend: {
      data: ['平均分', '通过率'],
      bottom: 0
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '15%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: data.subjectPerformance.map(s => s.subject.replace('药学专业知识', '药学专业').replace('中药学专业知识', '中药专业').replace('综合知识与技能', '综合')),
      axisLabel: { rotate: 30, fontSize: 10 }
    },
    yAxis: [
      {
        type: 'value',
        name: '分数',
        max: 100,
        axisLabel: { formatter: '{value}' }
      },
      {
        type: 'value',
        name: '通过率%',
        max: 100,
        axisLabel: { formatter: '{value}' }
      }
    ],
    series: [
      {
        name: '平均分',
        type: 'bar',
        data: data.subjectPerformance.map(s => s.avgScore),
        itemStyle: {
          color: {
            type: 'linear',
            x: 0, y: 0, x2: 0, y2: 1,
            colorStops: [
              { offset: 0, color: '#8B5CF6' },
              { offset: 1, color: '#6D28D9' }
            ]
          },
          borderRadius: [4, 4, 0, 0]
        }
      },
      {
        name: '通过率',
        type: 'line',
        yAxisIndex: 1,
        data: data.subjectPerformance.map(s => s.passRate),
        smooth: true,
        lineStyle: { color: '#EF4444', width: 3 },
        itemStyle: { color: '#EF4444' }
      }
    ]
  }

  const gaugeOption = {
    series: [
      {
        type: 'gauge',
        startAngle: 200,
        endAngle: -20,
        min: 0,
        max: 100,
        splitNumber: 10,
        itemStyle: {
          color: {
            type: 'linear',
            x: 0, y: 0, x2: 1, y2: 0,
            colorStops: [
              { offset: 0, color: '#3B82F6' },
              { offset: 0.5, color: '#10B981' },
              { offset: 1, color: '#F59E0B' }
            ]
          }
        },
        progress: {
          show: true,
          width: 20
        },
        pointer: {
          show: false
        },
        axisLine: {
          lineStyle: {
            width: 20,
            color: [[1, '#E5E7EB']]
          }
        },
        axisTick: { show: false },
        splitLine: { show: false },
        axisLabel: { show: false },
        anchor: { show: false },
        title: {
          show: true,
          offsetCenter: [0, '20%'],
          fontSize: 14,
          color: '#6B7280'
        },
        detail: {
          valueAnimation: true,
          fontSize: 36,
          fontWeight: 'bold',
          offsetCenter: [0, '-10%'],
          formatter: '{value}%',
          color: '#1F2937'
        },
        data: [{ value: data.predictedPassRate, name: '预测通过率' }]
      }
    ]
  }

  return (
    <div className="space-y-6">
      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-2xl font-bold text-gray-800">总部看板</h2>
            <p className="text-gray-500 mt-1">全国门店数据总览</p>
          </div>
          <div className="flex gap-2">
            <button
              onClick={() => setActiveView('overview')}
              className={`px-4 py-2 rounded-lg transition-all ${
                activeView === 'overview' 
                  ? 'bg-blue-500 text-white' 
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              数据概览
            </button>
            <button
              onClick={() => setActiveView('ranking')}
              className={`px-4 py-2 rounded-lg transition-all ${
                activeView === 'ranking' 
                  ? 'bg-blue-500 text-white' 
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              门店排行
            </button>
            <button
              onClick={() => setActiveView('analysis')}
              className={`px-4 py-2 rounded-lg transition-all ${
                activeView === 'analysis' 
                  ? 'bg-blue-500 text-white' 
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              数据分析
            </button>
          </div>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
          <div className="bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl p-4 text-white">
            <div className="flex items-center gap-2 mb-2">
              <Building2 className="w-5 h-5" />
              <span className="text-sm opacity-90">门店总数</span>
            </div>
            <p className="text-3xl font-bold">{data.totalStores}</p>
          </div>
          <div className="bg-gradient-to-br from-green-500 to-green-600 rounded-xl p-4 text-white">
            <div className="flex items-center gap-2 mb-2">
              <Users className="w-5 h-5" />
              <span className="text-sm opacity-90">员工总数</span>
            </div>
            <p className="text-3xl font-bold">{data.totalStaff}</p>
          </div>
          <div className="bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl p-4 text-white">
            <div className="flex items-center gap-2 mb-2">
              <Activity className="w-5 h-5" />
              <span className="text-sm opacity-90">今日活跃</span>
            </div>
            <p className="text-3xl font-bold">{data.activeUsersToday}</p>
          </div>
          <div className="bg-gradient-to-br from-orange-500 to-orange-600 rounded-xl p-4 text-white">
            <div className="flex items-center gap-2 mb-2">
              <TrendingUp className="w-5 h-5" />
              <span className="text-sm opacity-90">平均进度</span>
            </div>
            <p className="text-3xl font-bold">{data.averageProgress}%</p>
          </div>
          <div className="bg-gradient-to-br from-pink-500 to-pink-600 rounded-xl p-4 text-white">
            <div className="flex items-center gap-2 mb-2">
              <Target className="w-5 h-5" />
              <span className="text-sm opacity-90">预测通过率</span>
            </div>
            <p className="text-3xl font-bold">{data.predictedPassRate}%</p>
          </div>
          <div className="bg-gradient-to-br from-cyan-500 to-cyan-600 rounded-xl p-4 text-white">
            <div className="flex items-center gap-2 mb-2">
              <Clock className="w-5 h-5" />
              <span className="text-sm opacity-90">总学时</span>
            </div>
            <p className="text-3xl font-bold">{(data.totalStudyHours / 1000).toFixed(1)}k</p>
          </div>
        </div>
      </div>

      {activeView === 'overview' && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2 bg-white rounded-xl shadow-lg p-6">
            <ReactECharts option={trendOption} style={{ height: '350px' }} />
          </div>
          <div className="bg-white rounded-xl shadow-lg p-6">
            <ReactECharts option={gaugeOption} style={{ height: '350px' }} />
          </div>
        </div>
      )}

      {activeView === 'ranking' && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white rounded-xl shadow-lg p-6">
            <ReactECharts option={rankingOption} style={{ height: '400px' }} />
          </div>
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-bold text-gray-800 mb-4">门店排行榜详情</h3>
            <div className="space-y-3 max-h-[360px] overflow-y-auto">
              {data.storeRankings.map((store, index) => (
                <div key={store.storeId} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-all">
                  <div className="flex items-center gap-3">
                    <span className={`w-8 h-8 rounded-full flex items-center justify-center text-white font-bold ${
                      index === 0 ? 'bg-yellow-500' : index === 1 ? 'bg-gray-400' : index === 2 ? 'bg-orange-400' : 'bg-blue-500'
                    }`}>
                      {index + 1}
                    </span>
                    <div>
                      <p className="font-medium text-gray-800">{store.name}</p>
                      <div className="flex items-center gap-1 text-xs text-gray-500">
                        <Users className="w-3 h-3" />
                        <span>{store.staffCount}人</span>
                      </div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="flex items-center gap-2">
                      <span className="text-sm text-gray-600">进度:</span>
                      <span className="font-bold text-blue-600">{store.progress}%</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="text-sm text-gray-600">通过率:</span>
                      <span className="font-bold text-green-600">{store.passRate}%</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {activeView === 'analysis' && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white rounded-xl shadow-lg p-6">
            <ReactECharts option={regionOption} style={{ height: '400px' }} />
          </div>
          <div className="bg-white rounded-xl shadow-lg p-6">
            <ReactECharts option={subjectOption} style={{ height: '400px' }} />
          </div>
        </div>
      )}

      <div className="bg-white rounded-xl shadow-lg p-6">
        <h3 className="text-lg font-bold text-gray-800 mb-4">活跃度统计</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-blue-50 rounded-xl p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">今日活跃</p>
                <p className="text-2xl font-bold text-blue-600">{data.activeUsersToday}</p>
              </div>
              <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                <Activity className="w-6 h-6 text-blue-500" />
              </div>
            </div>
            <div className="mt-2 text-sm text-gray-500">
              占比 {((data.activeUsersToday / data.totalStaff) * 100).toFixed(1)}%
            </div>
          </div>
          <div className="bg-green-50 rounded-xl p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">本周活跃</p>
                <p className="text-2xl font-bold text-green-600">{data.activeUsersThisWeek}</p>
              </div>
              <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center">
                <TrendingUp className="w-6 h-6 text-green-500" />
              </div>
            </div>
            <div className="mt-2 text-sm text-gray-500">
              占比 {((data.activeUsersThisWeek / data.totalStaff) * 100).toFixed(1)}%
            </div>
          </div>
          <div className="bg-purple-50 rounded-xl p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600">本月活跃</p>
                <p className="text-2xl font-bold text-purple-600">{data.activeUsersThisMonth}</p>
              </div>
              <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center">
                <Award className="w-6 h-6 text-purple-500" />
              </div>
            </div>
            <div className="mt-2 text-sm text-gray-500">
              占比 {((data.activeUsersThisMonth / data.totalStaff) * 100).toFixed(1)}%
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default HeadquartersDashboard
