import { OpenAI } from 'openai';

export async function onRequestPost(context) {
  console.log('API Request Received');
  
  const { request, env } = context;
  
  const client = new OpenAI({
    apiKey: env.VOLC_API_KEY,
    baseURL: "https://ark.cn-beijing.volces.com/api/v3"
  });

  try {
    const body = await request.json();
    const messages = body.messages || [];
    const practice_case = body.practice_case;

    console.log("=== 收到复盘请求 ===");
    console.log(`消息数量: ${messages.length}`);

    const result = await handleReview(messages, practice_case, client, env);

    return new Response(
      JSON.stringify(result),
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

async function handleReview(messages, practice_case, client, env) {
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

  const response = await client.chat.completions.create({
    model: env.VOLC_ENDPOINT_ID,
    messages: [{ "role": "system", "content": system_prompt }],
    stream: false
  });

  const content = response.choices[0].message.content;
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