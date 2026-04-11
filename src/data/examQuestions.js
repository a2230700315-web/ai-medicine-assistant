export const examQuestions = {
  pharmacy: [
    {
      id: "p1",
      type: "single",
      question: "下列哪种药物属于处方药？",
      options: [
        "A. 维生素C片",
        "B. 阿司匹林肠溶片",
        "C. 头孢克肟胶囊",
        "D. 板蓝根颗粒"
      ],
      answer: "C",
      explanation: "头孢克肟胶囊属于抗生素类药物，根据《药品管理法》规定，抗生素类药物必须凭医师处方购买和使用。",
      category: "pharmacy",
      difficulty: "easy"
    },
    {
      id: "p2",
      type: "single",
      question: "药品储存时，下列哪种做法是正确的？",
      options: [
        "A. 所有药品都放在冰箱冷藏",
        "B. 药品按照说明书要求储存",
        "C. 药品开封后可以长期使用",
        "D. 不同批号的药品可以混放"
      ],
      answer: "B",
      explanation: "药品储存必须严格按照说明书要求，不同药品的储存条件不同，不能一概而论。",
      category: "pharmacy",
      difficulty: "easy"
    },
    {
      id: "p3",
      type: "single",
      question: "关于药品有效期，下列说法正确的是？",
      options: [
        "A. 过期药品可以继续使用",
        "B. 药品有效期可以延长",
        "C. 过期药品必须及时处理",
        "D. 药品开封后有效期不变"
      ],
      answer: "C",
      explanation: "过期药品药效会降低甚至产生有害物质，必须按照医疗废物处理规定及时处理。",
      category: "pharmacy",
      difficulty: "easy"
    },
    {
      id: "p4",
      type: "single",
      question: "下列哪种情况需要核对患者身份证？",
      options: [
        "A. 购买感冒药",
        "B. 购买含麻黄碱类药品",
        "C. 购买维生素",
        "D. 购买创可贴"
      ],
      answer: "B",
      explanation: "含麻黄碱类药品属于特殊管理药品，购买时需要实名登记并核对身份证。",
      category: "pharmacy",
      difficulty: "medium"
    },
    {
      id: "p5",
      type: "single",
      question: "关于药品不良反应，下列说法错误的是？",
      options: [
        "A. 所有药品都可能发生不良反应",
        "B. 不良反应都是严重的",
        "C. 发现不良反应应及时报告",
        "D. 用药前应了解可能的不良反应"
      ],
      answer: "B",
      explanation: "不良反应有轻有重，不是所有不良反应都是严重的，但都需要重视和及时处理。",
      category: "pharmacy",
      difficulty: "medium"
    }
  ],
  diseases: [
    {
      id: "d1",
      type: "single",
      question: "高血压患者用药期间，下列哪种情况需要特别注意？",
      options: [
        "A. 血压波动",
        "B. 体重变化",
        "C. 睡眠质量",
        "D. 食欲变化"
      ],
      answer: "A",
      explanation: "高血压患者用药期间需要密切监测血压变化，及时调整用药方案。",
      category: "diseases",
      difficulty: "easy"
    },
    {
      id: "d2",
      type: "single",
      question: "糖尿病患者出现低血糖时，正确的处理方法是？",
      options: [
        "A. 立即注射胰岛素",
        "B. 进食含糖食物",
        "C. 继续观察",
        "D. 停止所有用药"
      ],
      answer: "B",
      explanation: "糖尿病患者出现低血糖时应立即补充含糖食物，如糖果、果汁等，严重时需就医。",
      category: "diseases",
      difficulty: "medium"
    },
    {
      id: "d3",
      type: "single",
      question: "关于感冒用药，下列说法正确的是？",
      options: [
        "A. 抗生素可以治疗病毒性感冒",
        "B. 感冒药可以预防感冒",
        "C. 多种感冒药可以同时服用",
        "D. 感冒药应按照说明书使用"
      ],
      answer: "D",
      explanation: "感冒药必须按照说明书使用，避免重复用药和超量使用。",
      category: "diseases",
      difficulty: "easy"
    },
    {
      id: "d4",
      type: "single",
      question: "下列哪种症状需要立即就医？",
      options: [
        "A. 轻微头痛",
        "B. 持续性胸痛",
        "C. 轻度咳嗽",
        "D. 偶尔胃部不适"
      ],
      answer: "B",
      explanation: "持续性胸痛可能是心绞痛或心肌梗死的前兆，需要立即就医。",
      category: "diseases",
      difficulty: "medium"
    }
  ],
  regulations: [
    {
      id: "r1",
      type: "single",
      question: "根据《药品管理法》，下列哪种行为是违法的？",
      options: [
        "A. 凭处方销售处方药",
        "B. 无证经营药品",
        "C. 按规定储存药品",
        "D. 如实记录销售情况"
      ],
      answer: "B",
      explanation: "无证经营药品属于违法行为，违反《药品管理法》相关规定。",
      category: "regulations",
      difficulty: "easy"
    },
    {
      id: "r2",
      type: "single",
      question: "关于药品广告，下列说法正确的是？",
      options: [
        "A. 可以夸大药品疗效",
        "B. 必须经过审批",
        "C. 可以使用患者形象",
        "D. 可以承诺治愈率"
      ],
      answer: "B",
      explanation: "药品广告必须经过药品监督管理部门审批，不得夸大疗效或使用患者形象。",
      category: "regulations",
      difficulty: "medium"
    },
    {
      id: "r3",
      type: "single",
      question: "下列哪种药品需要特殊管理？",
      options: [
        "A. 维生素C",
        "B. 麻醉药品",
        "C. 创可贴",
        "D. 感冒药"
      ],
      answer: "B",
      explanation: "麻醉药品属于特殊管理药品，需要严格的处方管理和使用记录。",
      category: "regulations",
      difficulty: "easy"
    }
  ],
  communication: [
    {
      id: "c1",
      type: "single",
      question: "当顾客询问药品副作用时，正确的做法是？",
      options: [
        "A. 回避问题",
        "B. 如实告知可能副作用",
        "C. 夸大药品安全性",
        "D. 推荐更贵的药品"
      ],
      answer: "B",
      explanation: "应如实告知药品可能的副作用，并指导顾客正确用药和注意事项。",
      category: "communication",
      difficulty: "easy"
    },
    {
      id: "c2",
      type: "single",
      question: "遇到情绪激动的顾客，应该如何处理？",
      options: [
        "A. 与顾客争吵",
        "B. 保持冷静耐心倾听",
        "C. 立即叫保安",
        "D. 不予理睬"
      ],
      answer: "B",
      explanation: "应保持冷静，耐心倾听顾客诉求，理解其情绪，寻求合理解决方案。",
      category: "communication",
      difficulty: "medium"
    },
    {
      id: "c3",
      type: "single",
      question: "关于用药指导，下列说法正确的是？",
      options: [
        "A. 只需简单说明",
        "B. 应根据患者情况详细指导",
        "C. 让患者自己看说明书",
        "D. 不需要重复强调"
      ],
      answer: "B",
      explanation: "应根据患者的具体情况，详细指导用药方法、剂量、时间和注意事项。",
      category: "communication",
      difficulty: "easy"
    }
  ]
}

export const getQuestionsByCategory = (category, type = 'practice') => {
  const questions = examQuestions[category] || []
  
  if (type === 'practice') {
    return questions
  }
  
  // 对于考试模式，可以随机选择题目或设置不同难度
  return questions
}

export const getRandomQuestions = (count = 10) => {
  const allQuestions = Object.values(examQuestions).flat()
  const shuffled = allQuestions.sort(() => 0.5 - Math.random())
  return shuffled.slice(0, count)
}