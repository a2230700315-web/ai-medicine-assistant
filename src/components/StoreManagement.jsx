import { useState, useEffect, useRef } from 'react'
import ReactECharts from 'echarts-for-react'
import { Users, TrendingUp, AlertTriangle, BookOpen, Clock, Award } from 'lucide-react'
import { useAuth } from '../context/AuthContext'
import { mockLearningProgress, mockErrorDistribution, mockStaff } from '../data/mockData'

function StoreManagement() {
  const { user } = useAuth()
  const [activeTab, setActiveTab] = useState('progress')
  const progressChartRef = useRef(null)
  const errorChartRef = useRef(null)

  const storeId = user?.storeId || 'store_001'
  const storeProgress = mockLearningProgress[storeId] || mockLearningProgress.store_001
  const storeErrors = mockErrorDistribution[storeId] || mockErrorDistribution.store_001
  const storeStaff = mockStaff.filter(s => s.storeId === storeId)

  const progressOption = {
    title: {
      text: '员工学习进度分布',
      left: 'center',
      textStyle: { fontSize: 16, fontWeight: 'bold' }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: storeProgress.staffProgress.map(s => s.name),
      axisLabel: { rotate: 30, fontSize: 11 }
    },
    yAxis: {
      type: 'value',
      max: 100,
      axisLabel: { formatter: '{value}%' }
    },
    series: [{
      name: '学习进度',
      type: 'bar',
      data: storeProgress.staffProgress.map(s => ({
        value: s.progress,
        itemStyle: {
          color: s.progress >= 80 ? '#10B981' : s.progress >= 60 ? '#3B82F6' : s.progress >= 40 ? '#F59E0B' : '#EF4444'
        }
      })),
      label: {
        show: true,
        position: 'top',
        formatter: '{c}%'
      }
    }]
  }

  const errorOption = {
    title: {
      text: '错题科目分布',
      left: 'center',
      textStyle: { fontSize: 16, fontWeight: 'bold' }
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b}: {c}题 ({d}%)'
    },
    legend: {
      orient: 'vertical',
      left: 'left',
      top: 'middle'
    },
    series: [{
      name: '错题分布',
      type: 'pie',
      radius: ['40%', '70%'],
      center: ['60%', '50%'],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 10,
        borderColor: '#fff',
        borderWidth: 2
      },
      label: {
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: 16,
          fontWeight: 'bold'
        }
      },
      labelLine: { show: false },
      data: storeErrors.categories.map(c => ({
        value: c.count,
        name: c.name
      }))
    }]
  }

  const getProgressColor = (progress) => {
    if (progress >= 80) return 'text-green-600 bg-green-100'
    if (progress >= 60) return 'text-blue-600 bg-blue-100'
    if (progress >= 40) return 'text-yellow-600 bg-yellow-100'
    return 'text-red-600 bg-red-100'
  }

  const getErrorColor = (count) => {
    if (count <= 100) return 'text-green-600 bg-green-100'
    if (count <= 150) return 'text-blue-600 bg-blue-100'
    if (count <= 200) return 'text-yellow-600 bg-yellow-100'
    return 'text-red-600 bg-red-100'
  }

  return (
    <div className="space-y-6">
      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-2xl font-bold text-gray-800">门店管理</h2>
            <p className="text-gray-500 mt-1">{user?.storeName} · 数据概览</p>
          </div>
          <div className="flex gap-2">
            <button
              onClick={() => setActiveTab('progress')}
              className={`px-4 py-2 rounded-lg transition-all ${
                activeTab === 'progress' 
                  ? 'bg-blue-500 text-white' 
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              学习进度
            </button>
            <button
              onClick={() => setActiveTab('errors')}
              className={`px-4 py-2 rounded-lg transition-all ${
                activeTab === 'errors' 
                  ? 'bg-blue-500 text-white' 
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              错题分析
            </button>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
          <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-blue-500 rounded-lg flex items-center justify-center">
                <Users className="w-5 h-5 text-white" />
              </div>
              <div>
                <p className="text-sm text-gray-600">员工总数</p>
                <p className="text-2xl font-bold text-gray-800">{storeStaff.length}</p>
              </div>
            </div>
          </div>
          <div className="bg-gradient-to-br from-green-50 to-green-100 rounded-xl p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-green-500 rounded-lg flex items-center justify-center">
                <TrendingUp className="w-5 h-5 text-white" />
              </div>
              <div>
                <p className="text-sm text-gray-600">平均进度</p>
                <p className="text-2xl font-bold text-gray-800">{storeProgress.averageProgress}%</p>
              </div>
            </div>
          </div>
          <div className="bg-gradient-to-br from-yellow-50 to-yellow-100 rounded-xl p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-yellow-500 rounded-lg flex items-center justify-center">
                <AlertTriangle className="w-5 h-5 text-white" />
              </div>
              <div>
                <p className="text-sm text-gray-600">总错题数</p>
                <p className="text-2xl font-bold text-gray-800">{storeErrors.totalErrors}</p>
              </div>
            </div>
          </div>
          <div className="bg-gradient-to-br from-purple-50 to-purple-100 rounded-xl p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-purple-500 rounded-lg flex items-center justify-center">
                <BookOpen className="w-5 h-5 text-white" />
              </div>
              <div>
                <p className="text-sm text-gray-600">知识点总数</p>
                <p className="text-2xl font-bold text-gray-800">{storeProgress.totalTopics}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {activeTab === 'progress' && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white rounded-xl shadow-lg p-6">
            <ReactECharts option={progressOption} style={{ height: '400px' }} />
          </div>
          
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-bold text-gray-800 mb-4">员工学习详情</h3>
            <div className="space-y-3 max-h-[360px] overflow-y-auto">
              {storeProgress.staffProgress.map((staff, index) => (
                <div key={staff.staffId} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-all">
                  <div className="flex items-center gap-3">
                    <span className="text-2xl">{storeStaff[index]?.avatar || '👤'}</span>
                    <div>
                      <p className="font-medium text-gray-800">{staff.name}</p>
                      <div className="flex items-center gap-2 text-xs text-gray-500">
                        <Clock className="w-3 h-3" />
                        <span>最后活跃: {staff.lastActive}</span>
                      </div>
                    </div>
                  </div>
                  <div className="text-right">
                    <span className={`px-3 py-1 rounded-full text-sm font-medium ${getProgressColor(staff.progress)}`}>
                      {staff.progress}%
                    </span>
                    <p className="text-xs text-gray-500 mt-1">{staff.studyHours}学时</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {activeTab === 'errors' && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white rounded-xl shadow-lg p-6">
            <ReactECharts option={errorOption} style={{ height: '400px' }} />
          </div>
          
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-bold text-gray-800 mb-4">员工错题排行</h3>
            <div className="space-y-3 max-h-[360px] overflow-y-auto">
              {storeErrors.staffErrors
                .sort((a, b) => b.errorCount - a.errorCount)
                .map((staff, index) => {
                  const staffInfo = storeStaff.find(s => s.id === staff.staffId)
                  return (
                    <div key={staff.staffId} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-all">
                      <div className="flex items-center gap-3">
                        <span className={`w-6 h-6 rounded-full flex items-center justify-center text-white text-sm font-bold ${
                          index < 3 ? 'bg-red-500' : 'bg-gray-400'
                        }`}>
                          {index + 1}
                        </span>
                        <span className="text-2xl">{staffInfo?.avatar || '👤'}</span>
                        <div>
                          <p className="font-medium text-gray-800">{staff.name}</p>
                          <p className="text-xs text-gray-500">薄弱: {staff.topErrorCategory}</p>
                        </div>
                      </div>
                      <div className="text-right">
                        <span className={`px-3 py-1 rounded-full text-sm font-medium ${getErrorColor(staff.errorCount)}`}>
                          {staff.errorCount}题
                        </span>
                      </div>
                    </div>
                  )
                })}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default StoreManagement
