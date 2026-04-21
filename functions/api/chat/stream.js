export async function onRequestPost(context) {
  console.log('API Request Received');
  
  const { request, env } = context;

  try {
    const body = await request.json();
    const messages = body.messages || [];
    const practice_case = body.practice_case;
    const request_type = body.type || "chat";
    const difficulty = body.difficulty || "medium";

    console.log("=== 收到请求 ===");
    console.log(`请求数据: ${JSON.stringify(body)}`);
    console.log(`消息数量: ${messages.length}`);
    console.log(`案例信息: ${practice_case}`);
    console.log(`请求类型: ${request_type}`);
    console.log(`难度: ${difficulty}`);

    let content;
    if (request_type === "review") {
      content = await handleReview(messages, practice_case, env);
    } else {
      content = await handleChat(messages, practice_case, difficulty, env);
    }

    return new Response(
      JSON.stringify(content),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );

  } catch (e) {
    console.error("=== 错误 ===");
    console.error(`错误类型: ${e.name}`);
    console.error(`错误信息: ${e.message}`);
    console.error(e.stack);

    return new Response(
      JSON.stringify({ error: e.message }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}

async function callVolcAPI(messages, env) {
  const response = await fetch("https://ark.cn-beijing.volces.com/api/v3/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${env.VOLC_API_KEY}`
    },
    body: JSON.stringify({
      model: env.VOLC_ENDPOINT_ID,
      messages: messages,
      stream: false
    })
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`API请求失败: ${response.status} - ${errorText}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}

async function handleChat(messages, practice_case, difficulty, env) {
  const system_prompt = buildSystemPrompt(practice_case, difficulty);
  
  const api_messages = [
    { "role": "system", "content": system_prompt }
  ].concat(messages.map(msg => ({ "role": msg.role, "content": msg.content })));

  console.log(`发送给 API 的消息数量: ${api_messages.length}`);

  const content = await callVolcAPI(api_messages, env);
  console.log(`收到回复: ${content.length > 100 ? content.substring(0, 100) + '...' : content}`);

  return { "content": content };
}

async function handleReview(messages, practice_case, env) {
  const system_prompt = `你是一位专业的药店销售培训师，请根据店员与顾客的对话进行评价。

对话内容：
${JSON.stringify(messages, null, 2)}

请从以下4个维度进行打分（0-100分）：
1. 专业知识（professionalKnowledge）：是否识别出病症，是否提到了正确卖点
2. 沟通技巧（communicationSkills）：是否礼貌，是否有需求挖掘
3. 推销意识（salesAwareness）：是否尝试关联推销，是否处理了异议
4. 合规性（compliance）：是否有禁忌症提醒，如过敏询问

请返回JSON格式：
{
  "scores": {
    "professionalKnowledge": 分数,
    "communicationSkills": 分数,
    "salesAwareness": 分数,
    "compliance": 分数
  },
  "totalScore": 平均分,
  "advantages": ["优点1", "优点2"],
  "suggestions": ["改进建议1", "改进建议2"]
}`;

  const api_messages = [{ "role": "system", "content": system_prompt }];
  
  const content = await callVolcAPI(api_messages, env);
  console.log(`复盘结果: ${content.length > 100 ? content.substring(0, 100) + '...' : content}`);

  try {
    const result = JSON.parse(content);
    return result;
  } catch (e) {
    console.error(`解析复盘结果失败: ${e.message}`);
    return {
      "scores": {
        "professionalKnowledge": 50,
        "communicationSkills": 50,
        "salesAwareness": 50,
        "compliance": 50
      },
      "totalScore": 50,
      "advantages": ["无法解析AI回复"],
      "suggestions": ["请检查API配置"]
    };
  }
}

function buildSystemPrompt(practice_case, difficulty) {
  const difficultyConfig = getDifficultyConfig(difficulty);
  
  const base_prompt = `你是一位来药店咨询的顾客。请按照以下要求进行角色扮演：

## 核心规则
你是一个真实的顾客，会根据店员的服务质量做出自然的反应。你的目标是购买到合适的产品，而不是故意刁难店员。

## 回复格式（必须严格遵守）
你的每条回复必须包含两部分：
1. 顾客的真实回复内容（自然对话，20-100字）
2. 换行后添加元数据标记：[/METADATA]
3. 换行后添加JSON：{"trust_score": 数字, "current_stage": "阶段名称", "purchase_intent": 数字}

示例回复：
这个益生菌是饭前吃还是饭后吃啊？效果怎么样？
[/METADATA]
{"trust_score": 55, "current_stage": "interest", "purchase_intent": 40}

## 当前难度设置：${difficultyConfig.name}
${difficultyConfig.description}

## 顾客性格特点
${difficultyConfig.personality}

## 信任分数规则
- 初始值: ${difficultyConfig.initialTrust}
- 店员专业解答问题: +${difficultyConfig.trustGain}
- 店员态度友好热情: +5
- 店员推荐合适产品: +${difficultyConfig.trustGain}
- 店员解答疑虑消除担忧: +${difficultyConfig.trustGain}
- 店员强行推销: -${difficultyConfig.trustLoss}
- 店员态度敷衍: -${difficultyConfig.trustLoss}
- 店员推荐不相关产品: -10

## 购买意向规则
- 初始值: ${difficultyConfig.initialIntent}
- 信任分数每增加10分，购买意向+5
- 店员成功解答核心疑虑: +15
- 店员给出合理价格或优惠: +10
- 购买意向达到70以上时，顾客会表现出购买意愿
- 购买意向达到85以上时，顾客会决定购买

## 销售阶段
- initial: 初始接触，顾客表达需求
- interest: 产生兴趣，询问产品细节
- consideration: 考虑中，有疑虑需要解答
- decision: 准备购买，询问价格和使用方法
- purchase: 决定购买，完成交易

## 重要提示
1. 当购买意向(purchase_intent)达到85以上时，你应该主动表示愿意购买
2. 对话应该自然流畅，像真实的药店场景
3. 不要一直挑剔，顾客的目的是买到合适的产品
4. 如果店员服务好，应该给予正面反馈
5. 每次回复都要检查是否应该进入下一阶段或完成购买`;

  let case_info = "";
  if (practice_case) {
    case_info = `

## 当前案例信息
- 姓名: ${practice_case.姓名 || '顾客'}
- 年龄: ${practice_case.年龄 || 45}
- 性别: ${practice_case.性别 || '女'}
- BMI: ${practice_case.BMI || 24.5}
- 过敏史: ${practice_case.过敏史 || '无'}
- 现病史: ${practice_case.现病史 || ''}
- 目前用药: ${practice_case.目前用药 || ''}
- 饮食习惯: ${practice_case.饮食习惯 || ''}
- 销售目标: ${practice_case.销售目标 || ''}

请根据以上信息扮演这位顾客，你的主要需求是：${practice_case.现病史 || '咨询健康问题'}。`;
  }
  
  return base_prompt + case_info;
}

function getDifficultyConfig(difficulty) {
  const configs = {
    easy: {
      name: "简单",
      description: "顾客比较随和，容易沟通，对店员比较信任，问题较少，容易被说服购买。",
      personality: `- 性格温和，容易沟通
- 对店员比较信任，愿意听取建议
- 问题较少，关注点明确
- 对价格不太敏感
- 容易被专业解答说服
- 会主动表达购买意愿`,
      initialTrust: 50,
      initialIntent: 40,
      trustGain: 15,
      trustLoss: 5,
      purchaseThreshold: 70
    },
    medium: {
      name: "中等",
      description: "顾客有一定疑虑，需要店员耐心解答，但可以被说服，会提出一些合理问题。",
      personality: `- 性格正常，有一定主见
- 对产品功效有合理疑虑
- 会询问价格和性价比
- 需要店员耐心解答问题
- 会被专业知识和真诚态度打动
- 会货比三家，但最终会做出决定`,
      initialTrust: 35,
      initialIntent: 25,
      trustGain: 10,
      trustLoss: 10,
      purchaseThreshold: 80
    },
    hard: {
      name: "困难",
      description: "顾客比较挑剔，对价格敏感，疑虑较多，需要店员展现专业能力和耐心才能说服。",
      personality: `- 性格较为谨慎，不容易被说服
- 对价格非常敏感，会反复比价
- 对产品功效有较多疑虑
- 会提出尖锐问题
- 需要店员展现专业知识和耐心
- 只有在充分信任后才会购买`,
      initialTrust: 20,
      initialIntent: 15,
      trustGain: 8,
      trustLoss: 15,
      purchaseThreshold: 85
    }
  };
  
  return configs[difficulty] || configs.medium;
}