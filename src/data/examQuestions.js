import examData from './examQuestionsData.json'

export const examCategories = [
  {
    id: 'pharmacy_1',
    name: '药学专业知识(一)',
    shortName: '西药一',
    type: 'pharmacy',
    color: '#3B82F6',
    icon: '💊',
    description: '药物化学、药剂学、药物分析等',
    totalQuestions: 565,
    years: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
  },
  {
    id: 'pharmacy_2',
    name: '药学专业知识(二)',
    shortName: '西药二',
    type: 'pharmacy',
    color: '#10B981',
    icon: '💉',
    description: '临床药物治疗学、药理学等',
    totalQuestions: 574,
    years: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
  },
  {
    id: 'pharmacy_comprehensive',
    name: '药学综合知识与技能',
    shortName: '西药综合',
    type: 'pharmacy',
    color: '#8B5CF6',
    icon: '🏥',
    description: '处方审核、用药指导、药品管理等',
    totalQuestions: 512,
    years: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
  },
  {
    id: 'pharmacy_regulation',
    name: '药事管理与法规',
    shortName: '药管',
    type: 'common',
    color: '#F59E0B',
    icon: '📋',
    description: '药品管理法、药品经营质量管理等',
    totalQuestions: 394,
    years: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
  },
  {
    id: 'tcm_1',
    name: '中药学专业知识(一)',
    shortName: '中药一',
    type: 'tcm',
    color: '#EF4444',
    icon: '🌿',
    description: '中药学、中药药剂学、中药鉴定学等',
    totalQuestions: 574,
    years: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
  },
  {
    id: 'tcm_2',
    name: '中药学专业知识(二)',
    shortName: '中药二',
    type: 'tcm',
    color: '#EC4899',
    icon: '🍃',
    description: '常用单味药、常用中成药等',
    totalQuestions: 570,
    years: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
  },
  {
    id: 'tcm_comprehensive',
    name: '中药学综合知识与技能',
    shortName: '中药综合',
    type: 'tcm',
    color: '#06B6D4',
    icon: '🎋',
    description: '中医基础理论、中医诊断学、中药调剂等',
    totalQuestions: 572,
    years: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
  }
]

export const sampleQuestions = examData

export const examRecords = []

export const userExamStats = {
  totalExams: 0,
  totalQuestions: 0,
  correctQuestions: 0,
  totalTime: 0,
  categoryStats: {}
}

export function getQuestionsByCategory(categoryId, year = null) {
  const questions = sampleQuestions[categoryId]
  if (!questions) return []
  if (year) {
    return questions[year] || []
  }
  return Object.values(questions).flat()
}

export function getYearsByCategory(categoryId) {
  const category = examCategories.find(c => c.id === categoryId)
  return category ? category.years : []
}

export function getRandomQuestions(categoryId, count = 10, year = null) {
  const questions = getQuestionsByCategory(categoryId, year)
  return shuffleArray(questions).slice(0, count)
}

export function shuffleArray(array) {
  const shuffled = [...array]
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
  }
  return shuffled
}

export function calculateScore(questions, answers) {
  let score = 0
  let correct = 0
  let wrong = 0
  let unanswered = 0

  questions.forEach(q => {
    const userAnswer = answers[q.id]
    if (!userAnswer) {
      unanswered++
    } else if (userAnswer === q.answer) {
      correct++
      score += q.points
    } else {
      wrong++
    }
  })

  return {
    score,
    correct,
    wrong,
    unanswered,
    total: questions.length,
    accuracy: questions.length > 0 ? ((correct / questions.length) * 100).toFixed(1) : 0
  }
}
