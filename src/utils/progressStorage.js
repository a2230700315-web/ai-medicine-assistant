const STORAGE_KEY = 'pharmacy_training_progress'

export const saveProgress = (caseId, score, reviewData) => {
  try {
    const existingProgress = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}')
    
    if (!existingProgress[caseId] || score > existingProgress[caseId].score) {
      existingProgress[caseId] = {
        score: score,
        completedAt: new Date().toISOString(),
        reviewData: reviewData
      }
      
      localStorage.setItem(STORAGE_KEY, JSON.stringify(existingProgress))
      console.log('进度已保存:', existingProgress[caseId])
    }
  } catch (error) {
    console.error('保存进度失败:', error)
  }
}

export const getProgress = () => {
  try {
    const progress = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}')
    return progress
  } catch (error) {
    console.error('读取进度失败:', error)
    return {}
  }
}

export const getCaseProgress = (caseId) => {
  try {
    const progress = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}')
    return progress[caseId] || null
  } catch (error) {
    console.error('读取案例进度失败:', error)
    return null
  }
}

export const clearProgress = () => {
  try {
    localStorage.removeItem(STORAGE_KEY)
    console.log('进度已清除')
  } catch (error) {
    console.error('清除进度失败:', error)
  }
}

export const getMedal = (score) => {
  if (score >= 90) {
    return { icon: '🏆', title: '金牌药师', color: 'text-yellow-500' }
  } else if (score >= 80) {
    return { icon: '🥈', title: '银牌药师', color: 'text-gray-400' }
  } else if (score >= 70) {
    return { icon: '⭐', title: '销售之星', color: 'text-blue-500' }
  } else if (score >= 60) {
    return { icon: '✅', title: '合格药师', color: 'text-green-500' }
  } else {
    return { icon: '📚', title: '继续努力', color: 'text-orange-500' }
  }
}