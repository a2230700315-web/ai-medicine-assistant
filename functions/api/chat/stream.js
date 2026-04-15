// 处理 CORS 预检
function handleCORS(request) {
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        'Access-Control-Max-Age': '86400'
      }
    });
  }
  return null;
}

// 添加 CORS 头的辅助函数
function addCorsHeaders(response) {
  response.headers.set('Access-Control-Allow-Origin', '*');
  response.headers.set('Access-Control-Allow-Methods', 'POST, OPTIONS');
  response.headers.set('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  return response;
}

export async function onRequestPost(context) {
  const { request } = context;
  
  // 处理 CORS 预检
  const corsResponse = handleCORS(request);
  if (corsResponse) {
    return corsResponse;
  }
  
  try {
    // 解析请求体
    const body = await request.json();
    
    // 获取环境变量
    const apiKey = context.env.VOLCANO_API_KEY;
    const endpointId = context.env.VOLCANO_ENDPOINT_ID;
    
    if (!apiKey || !endpointId) {
      const response = new Response(
        JSON.stringify({ error: 'API密钥未配置' }),
        { status: 500, headers: { 'Content-Type': 'application/json' } }
      );
      return addCorsHeaders(response);
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
      const errorResponse = new Response(
        JSON.stringify({ 
          error: 'API调用失败',
          details: errorData
        }),
        { status: response.status, headers: { 'Content-Type': 'application/json' } }
      );
      return addCorsHeaders(errorResponse);
    }
    
    const data = await response.json();
    
    // 处理响应
    if (data.choices && data.choices.length > 0) {
      const successResponse = new Response(
        JSON.stringify({ content: data.choices[0].message.content }),
        { headers: { 'Content-Type': 'application/json' } }
      );
      return addCorsHeaders(successResponse);
    } else {
      const errorResponse = new Response(
        JSON.stringify({ error: 'API响应格式错误' }),
        { status: 500, headers: { 'Content-Type': 'application/json' } }
      );
      return addCorsHeaders(errorResponse);
    }
    
  } catch (error) {
    console.error('API转发错误:', error);
    const errorResponse = new Response(
      JSON.stringify({ error: '服务器内部错误' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
    return addCorsHeaders(errorResponse);
  }
}