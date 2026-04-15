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
    
    // 构建请求参数
    const payload = {
      model: endpointId,
      messages: body.messages,
      temperature: body.temperature || 0.8,
      max_tokens: body.max_tokens || 500,
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
      return new Response(
        JSON.stringify({ content: data.choices[0].message.content }),
        { headers: { 'Content-Type': 'application/json' } }
      );
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

export async function onRequestGet(context) {
  return new Response(
    JSON.stringify({ message: 'API服务运行中' }),
    { headers: { 'Content-Type': 'application/json' } }
  );
}