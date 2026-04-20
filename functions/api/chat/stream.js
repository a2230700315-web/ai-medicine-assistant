export async function onRequestPost(context) {
  console.log('API Request Received');
  
  const { request, env } = context;

  try {
    const body = await request.json();
    const messages = body.messages || [];
    const practice_case = body.practice_case;
    const request_type = body.type || "chat";

    console.log("=== 收到请求 ===");
    console.log(`请求数据: ${JSON.stringify(body)}`);
    console.log(`消息数量: ${messages.length}`);
    console.log(`案例信息: ${practice_case}`);
    console.log(`请求类型: ${request_type}`);

    let content;
    if (request_type === "review") {
      content = await handleReview(messages, practice_case, env);
    } else {
      content = await handleChat(messages, practice_case, env);
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

async function handleChat(messages, practice_case, env) {
  const system_prompt = buildSystemPrompt(practice_case);
  
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

function buildSystemPrompt(practice_case) {
  const base_prompt = `你是一位挑剔的顾客，正在药店咨询产品。请按照以下要求回复：

1. 回复格式要求：
   - 顾客的真实回复内容（至少20字）
   - [/METADATA]
   - {"trust_score": 数字(0-100), "current_stage": "阶段名称"}

2. 顾客性格特点：
   - 对价格敏感，会询问折扣
   - 对功效有疑虑，需要详细解释
   - 对品牌不太信任，更看重实际效果
   - 喜欢货比三家

3. 销售阶段：
   - initial: 初始接触，顾客还在观望
   - interest: 产生兴趣，开始询问细节
   - consideration: 考虑购买，但还有疑虑
   - decision: 准备购买，询问价格和优惠
   - purchase: 已经购买，询问使用方法

4. trust_score 规则：
   - 初始值: 30
   - 店员提到产品功效: +10
   - 店员解答疑虑: +15
   - 店员推荐合适产品: +20
   - 店员态度不好: -20
   - 店员强行推销: -15

请严格按照格式回复，不要遗漏任何部分。`;

  if (practice_case) {
    const case_info = `
当前案例信息：
- 姓名: ${practice_case.姓名 || '顾客'}
- 年龄: ${practice_case.年龄 || 45}
- BMI: ${practice_case.BMI || 24.5}
- 过敏史: ${practice_case.过敏史 || '无'}
- 现病史: ${practice_case.现病史 || ''}
- 目前用药: ${practice_case.目前用药 || ''}
- 饮食习惯: ${practice_case.饮食习惯 || ''}
- 销售目标: ${practice_case.销售目标 || ''}

请根据以上案例信息，扮演相应的顾客角色进行对话。`;
    return base_prompt + "\n\n" + case_info;
  }
  
  return base_prompt;
}