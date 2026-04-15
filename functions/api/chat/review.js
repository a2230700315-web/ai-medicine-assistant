export async function onRequestPost(context) {
  const { request } = context;
  
  try {
    // 解析请求体
    const body = await request.json();
    
    // 获取环境变量
    const apiKey = context.env.VOLCANO_API_KEY;
    const endpointId = context.env.VOLCANO_ENDPOINT_ID;
    
    if (!apiKey || !endpointId) {
      return new Response(
        JSON.stringify({ error: 'API密钥未配置' }),
        { status: 500, headers: { 'Content-Type': 'application/json' } }
      );
    }
    
    // 构建系统提示
    const systemPrompt = `你是一位专业的药店销售培训师，请根据店员与顾客的对话进行评价。

对话内容：
${JSON.stringify(body.messages, null, 2)}

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
    
    // 构建请求参数
    const payload = {
      model: endpointId,
      messages: [
        { role: "system", content: systemPrompt }
      ],
      temperature: 0.5,
      max_tokens: 1000,
      stream: false
    };
    
    // 调用火山引擎API
    const response = await fetch('https://ark.cn-beijing.volces.com/api/v3/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });
    
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      return new Response(
        JSON.stringify({ 
          error: 'API调用失败',
          details: errorData
        }),
        { status: response.status, headers: { 'Content-Type': 'application/json' } }
      );
    }
    
    const data = await response.json();
    
    // 处理响应
    if (data.choices && data.choices.length > 0) {
      const content = data.choices[0].message.content;
      try {
        const result = JSON.parse(content);
        return new Response(
          JSON.stringify(result),
          { headers: { 'Content-Type': 'application/json' } }
        );
      } catch (e) {
        return new Response(
          JSON.stringify({
            scores: {
              professionalKnowledge: 50,
              communicationSkills: 50,
              salesAwareness: 50,
              compliance: 50
            },
            totalScore: 50,
            advantages: ["无法解析AI回复"],
            suggestions: ["请检查API配置"]
          }),
          { headers: { 'Content-Type': 'application/json' } }
        );
      }
    } else {
      return new Response(
        JSON.stringify({ error: 'API响应格式错误' }),
        { status: 500, headers: { 'Content-Type': 'application/json' } }
      );
    }
    
  } catch (error) {
    console.error('API转发错误:', error);
    return new Response(
      JSON.stringify({ error: '服务器内部错误' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}