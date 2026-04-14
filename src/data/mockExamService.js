import examData from './examQuestionsData.json'

const EXAM_CONFIG = {
  totalQuestions: 120,
  timeLimit: 120,
  questionTypeRatio: {
    single: 0.40,
    multi: 0.20,
    matching: 0.40
  }
}

const KNOWLEDGE_POINTS = {
  pharmacy_1: [
    '药物化学结构', '药物理化性质', '药物剂型', '药物稳定性', '药物分析方法',
    '药物杂质检查', '药物含量测定', '药物制剂', '药物释放', '药物吸收',
    '药物分布', '药物代谢', '药物排泄', '药物相互作用', '药物不良反应'
  ],
  pharmacy_2: [
    '药理作用机制', '药物代谢动力学', '药物效应动力学', '药物相互作用', '药物不良反应',
    '抗菌药物', '抗肿瘤药物', '心血管药物', '消化系统药物', '呼吸系统药物',
    '神经系统药物', '内分泌药物', '抗炎药物', '免疫调节药物', '解毒药物'
  ],
  pharmacy_comprehensive: [
    '处方审核', '用药指导', '药品调配', '药品管理', '特殊人群用药',
    '药物治疗方案', '药物监测', '不良反应报告', '用药咨询', '健康教育',
    '慢性病管理', '急救用药', '中药西药联用', '药品储存', '药品召回'
  ],
  pharmacy_regulation: [
    '药品管理法', '药品经营质量管理', '药品生产质量管理', '药品注册管理', '药品不良反应报告',
    '特殊药品管理', '药品广告管理', '药品价格管理', '药品召回管理', '药品标签说明书',
    '药品流通管理', '医疗机构药事管理', '执业药师管理', '药品分类管理', '互联网药品交易'
  ],
  tcm_1: [
    '中药鉴定', '中药炮制', '中药制剂', '中药化学', '中药药理',
    '中药调剂', '中药储存', '中药煎煮', '中药配伍', '中药禁忌',
    '中药采收', '中药产地加工', '中药质量标准', '中药新药研发', '中药资源'
  ],
  tcm_2: [
    '解表药', '清热药', '泻下药', '祛风湿药', '化湿药',
    '利水渗湿药', '温里药', '理气药', '消食药', '止血药',
    '活血化瘀药', '化痰止咳平喘药', '安神药', '平肝息风药', '补虚药'
  ],
  tcm_comprehensive: [
    '中医基础理论', '中医诊断学', '中药调剂操作', '中药煎煮', '中成药应用',
    '中医体质辨识', '中医养生保健', '常见病辨证论治', '中医急症处理', '中药不良反应',
    '中西药联用', '特殊人群中药应用', '中药处方审核', '中药储存养护', '中药信息服务'
  ]
}

function shuffleArray(array) {
  const shuffled = [...array]
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]]
  }
  return shuffled
}

function detectQuestionType(question) {
  const answer = question.answer || ''
  if (answer.length > 1) {
    return 'multi'
  }
  const questionText = question.question || ''
  if (questionText.includes('{TSE}') || questionText.includes('{TS}') || 
      questionText.includes('配伍') || questionText.includes('共用题干')) {
    return 'matching'
  }
  return 'single'
}

function assignKnowledgePoint(question, categoryId) {
  const points = KNOWLEDGE_POINTS[categoryId] || []
  const randomIndex = Math.floor(Math.random() * points.length)
  return points[randomIndex]
}

function calculateHeatScore(question, year, categoryId) {
  const yearNum = parseInt(year)
  const recencyScore = (yearNum - 2015) / 9
  const hasExplanation = question.explanation ? 0.3 : 0
  const optionCount = question.options ? question.options.length : 0
  const complexityScore = Math.min(optionCount / 5, 0.2)
  return Math.min(1, recencyScore * 0.5 + hasExplanation + complexityScore)
}

export function generateMockPaper(categoryId, options = {}) {
  const {
    totalQuestions = EXAM_CONFIG.totalQuestions,
    timeLimit = EXAM_CONFIG.timeLimit,
    includeYears = null,
    excludeDone = [],
    difficulty = 'mixed'
  } = options

  const categoryQuestions = examData[categoryId]
  if (!categoryQuestions) {
    return { questions: [], metadata: { error: '科目不存在' } }
  }

  let allQuestions = []
  Object.entries(categoryQuestions).forEach(([year, questions]) => {
    if (includeYears && !includeYears.includes(year)) return
    questions.forEach(q => {
      if (!excludeDone.includes(q.id)) {
        allQuestions.push({
          ...q,
          year,
          categoryId,
          type: detectQuestionType(q),
          knowledgePoint: assignKnowledgePoint(q, categoryId),
          heatScore: calculateHeatScore(q, year, categoryId)
        })
      }
    })
  })

  const singleQuestions = allQuestions.filter(q => q.type === 'single')
  const multiQuestions = allQuestions.filter(q => q.type === 'multi')
  const matchingQuestions = allQuestions.filter(q => q.type === 'matching')

  const singleCount = Math.floor(totalQuestions * EXAM_CONFIG.questionTypeRatio.single)
  const multiCount = Math.floor(totalQuestions * EXAM_CONFIG.questionTypeRatio.multi)
  const matchingCount = totalQuestions - singleCount - multiCount

  const selectedSingle = shuffleArray(singleQuestions).slice(0, singleCount)
  const selectedMulti = shuffleArray(multiQuestions).slice(0, multiCount)
  const selectedMatching = shuffleArray(matchingQuestions).slice(0, matchingCount)

  let selectedQuestions = [
    ...selectedSingle,
    ...selectedMulti,
    ...selectedMatching
  ]

  selectedQuestions = shuffleArray(selectedQuestions)

  selectedQuestions = selectedQuestions.map((q, index) => ({
    ...q,
    id: `mock_${categoryId}_${Date.now()}_${index}`,
    questionNumber: index + 1,
    points: q.type === 'multi' ? 1.5 : 1
  }))

  const knowledgeCoverage = new Set(selectedQuestions.map(q => q.knowledgePoint))
  const totalKnowledgePoints = KNOWLEDGE_POINTS[categoryId]?.length || 15
  const coverageRate = knowledgeCoverage.size / totalKnowledgePoints

  return {
    questions: selectedQuestions,
    metadata: {
      categoryId,
      totalQuestions: selectedQuestions.length,
      timeLimit,
      generatedAt: new Date().toISOString(),
      questionTypes: {
        single: selectedSingle.length,
        multi: selectedMulti.length,
        matching: selectedMatching.length
      },
      knowledgeCoverage: {
        covered: knowledgeCoverage.size,
        total: totalKnowledgePoints,
        rate: (coverageRate * 100).toFixed(1) + '%'
      },
      averageHeatScore: (selectedQuestions.reduce((sum, q) => sum + q.heatScore, 0) / selectedQuestions.length).toFixed(2)
    }
  }
}

export function generateWeaknessPaper(userRecords, categoryId, options = {}) {
  const {
    totalQuestions = 20,
    minErrorRate = 0.5
  } = options

  const errorStats = {}
  const doneQuestions = new Set()

  if (userRecords && userRecords.length > 0) {
    userRecords.forEach(record => {
      if (record.categoryId !== categoryId) return
      
      record.questions?.forEach(q => {
        doneQuestions.add(q.id)
        if (!q.isCorrect) {
          const kp = q.knowledgePoint || '其他'
          errorStats[kp] = (errorStats[kp] || 0) + 1
        }
      })
    })
  }

  const sortedWeakness = Object.entries(errorStats)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 3)
    .map(([point]) => point)

  const categoryQuestions = examData[categoryId]
  if (!categoryQuestions) {
    return { questions: [], metadata: { error: '科目不存在' } }
  }

  let allQuestions = []
  Object.entries(categoryQuestions).forEach(([year, questions]) => {
    questions.forEach(q => {
      if (!doneQuestions.has(q.id)) {
        allQuestions.push({
          ...q,
          year,
          categoryId,
          type: detectQuestionType(q),
          knowledgePoint: assignKnowledgePoint(q, categoryId),
          heatScore: calculateHeatScore(q, year, categoryId)
        })
      }
    })
  })

  let selectedQuestions = []
  const questionsPerWeakness = Math.ceil(totalQuestions / 3)

  sortedWeakness.forEach(weakPoint => {
    const matchingQuestions = allQuestions.filter(q => q.knowledgePoint === weakPoint)
    const shuffled = shuffleArray(matchingQuestions)
    selectedQuestions.push(...shuffled.slice(0, questionsPerWeakness))
  })

  if (selectedQuestions.length < totalQuestions) {
    const remaining = allQuestions.filter(q => 
      !selectedQuestions.find(s => s.id === q.id)
    )
    selectedQuestions.push(...shuffleArray(remaining).slice(0, totalQuestions - selectedQuestions.length))
  }

  selectedQuestions = selectedQuestions.slice(0, totalQuestions)

  selectedQuestions = selectedQuestions.map((q, index) => ({
    ...q,
    id: `weakness_${categoryId}_${Date.now()}_${index}`,
    questionNumber: index + 1,
    points: q.type === 'multi' ? 1.5 : 1,
    isWeaknessTarget: sortedWeakness.includes(q.knowledgePoint)
  }))

  return {
    questions: selectedQuestions,
    metadata: {
      categoryId,
      totalQuestions: selectedQuestions.length,
      timeLimit: 30,
      generatedAt: new Date().toISOString(),
      weaknessPoints: sortedWeakness,
      paperType: 'weakness'
    }
  }
}

export function generateReviewPaper(userRecords, categoryId, options = {}) {
  const {
    totalQuestions = 20,
    reviewDays = [1, 3, 7]
  } = options

  const now = new Date()
  const reviewCandidates = []

  if (userRecords && userRecords.length > 0) {
    userRecords.forEach(record => {
      if (record.categoryId !== categoryId) return
      
      const recordDate = new Date(record.completedAt)
      const daysDiff = Math.floor((now - recordDate) / (1000 * 60 * 60 * 24))
      
      record.questions?.forEach(q => {
        if (!q.isCorrect && reviewDays.includes(daysDiff)) {
          reviewCandidates.push({
            ...q,
            reviewDay: daysDiff,
            originalRecordId: record.id
          })
        }
      })
    })
  }

  const selectedQuestions = shuffleArray(reviewCandidates).slice(0, totalQuestions)

  return {
    questions: selectedQuestions.map((q, index) => ({
      ...q,
      id: `review_${categoryId}_${Date.now()}_${index}`,
      questionNumber: index + 1,
      isReviewQuestion: true
    })),
    metadata: {
      categoryId,
      totalQuestions: selectedQuestions.length,
      timeLimit: 30,
      generatedAt: new Date().toISOString(),
      paperType: 'review',
      reviewDays
    }
  }
}

export function getDailyReviewQuestions(userRecords, categoryId) {
  const now = new Date()
  const today = now.toISOString().split('T')[0]
  
  const reviewSchedule = [
    { day: 1, weight: 1.0 },
    { day: 3, weight: 0.8 },
    { day: 7, weight: 0.6 },
    { day: 15, weight: 0.4 },
    { day: 30, weight: 0.2 }
  ]

  const dueReviews = []

  if (userRecords && userRecords.length > 0) {
    userRecords.forEach(record => {
      if (record.categoryId !== categoryId) return
      
      const recordDate = new Date(record.completedAt)
      const daysDiff = Math.floor((now - recordDate) / (1000 * 60 * 60 * 24))
      
      const schedule = reviewSchedule.find(s => s.day === daysDiff)
      if (schedule) {
        record.questions?.forEach(q => {
          if (!q.isCorrect) {
            dueReviews.push({
              ...q,
              dueDay: daysDiff,
              priority: schedule.weight
            })
          }
        })
      }
    })
  }

  return dueReviews.sort((a, b) => b.priority - a.priority)
}

export function analyzeUserWeakness(userRecords, categoryId) {
  const errorByKnowledge = {}
  const totalByKnowledge = {}
  const errorByType = { single: 0, multi: 0, matching: 0 }
  const totalByType = { single: 0, multi: 0, matching: 0 }

  if (userRecords && userRecords.length > 0) {
    userRecords.forEach(record => {
      if (record.categoryId !== categoryId) return
      
      record.questions?.forEach(q => {
        const kp = q.knowledgePoint || '其他'
        const type = q.type || 'single'
        
        totalByKnowledge[kp] = (totalByKnowledge[kp] || 0) + 1
        totalByType[type]++
        
        if (!q.isCorrect) {
          errorByKnowledge[kp] = (errorByKnowledge[kp] || 0) + 1
          errorByType[type]++
        }
      })
    })
  }

  const weaknessPoints = Object.entries(totalByKnowledge)
    .map(([point, total]) => ({
      point,
      total,
      errors: errorByKnowledge[point] || 0,
      errorRate: total > 0 ? ((errorByKnowledge[point] || 0) / total * 100).toFixed(1) : 0
    }))
    .filter(w => w.total >= 3)
    .sort((a, b) => parseFloat(b.errorRate) - parseFloat(a.errorRate))
    .slice(0, 5)

  return {
    weaknessPoints,
    typeStats: {
      single: { errors: errorByType.single, total: totalByType.single },
      multi: { errors: errorByType.multi, total: totalByType.multi },
      matching: { errors: errorByType.matching, total: totalByType.matching }
    }
  }
}

export function getHeatLabel(heatScore) {
  if (heatScore >= 0.8) return { label: '核心', color: '#EF4444', icon: '🔥' }
  if (heatScore >= 0.6) return { label: '高频', color: '#F59E0B', icon: '⭐' }
  if (heatScore >= 0.4) return { label: '常考', color: '#10B981', icon: '📌' }
  return { label: '基础', color: '#6B7280', icon: '📝' }
}

export function saveExamRecord(record) {
  const records = JSON.parse(localStorage.getItem('examRecords') || '[]')
  records.push({
    ...record,
    id: `record_${Date.now()}`,
    completedAt: new Date().toISOString()
  })
  localStorage.setItem('examRecords', JSON.stringify(records))
  return record
}

export function getExamRecords() {
  return JSON.parse(localStorage.getItem('examRecords') || '[]')
}

export function getUserRecordsByCategory(categoryId) {
  const records = getExamRecords()
  return records.filter(r => r.categoryId === categoryId)
}

export function clearExamRecords() {
  localStorage.removeItem('examRecords')
}
