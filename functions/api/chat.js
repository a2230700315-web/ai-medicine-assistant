// 处理 CORS 预检
function handleCORS(request) {
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
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
  response.headers.set('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
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
    const apiKey = context.env.VOLC_API_KEY;
    const endpointId = context.env.VOLC_ENDPOINT_ID;
    
    if (!apiKey || !endpointId) {
      console.log('环境变量配置检查:');
      console.log('VOLC_API_KEY:', apiKey ? '已配置' : '未配置');
      console.log('VOLC_ENDPOINT_ID:', endpointId ? '已配置' : '未配置');
      const response = new Response(
        JSON.stringify({ error: 'API密钥未配置' }),
        { status: 500, headers: { 'Content-Type': 'application/json' } }
      );
      return addCorsHeaders(response);
    }
    
    // 构建系统提示
    const systemPrompt = {
      role: "system",
      content: `你是一位模拟顾客，正在与药店店员进行对话。

你的任务：
1. 严格扮演顾客角色，不要切换到店员角色
2. 根据提供的案例信息，表达你的症状和需求
3. 对店员的建议提出合理的问题和异议
4. 表现出真实顾客的犹豫和疑虑
5. 不要主动提供专业的药品知识
6. 保持对话自然，像真实顾客一样交流

记住：你是顾客，不是药店店员！`
    };
    
    // 构建请求参数
    const payload = {
      model: endpointId,
      messages: [systemPrompt, ...body.messages],
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

export async function onRequestGet(context) {
  const { request } = context;
  
  // 处理 CORS 预检
  const corsResponse = handleCORS(request);
  if (corsResponse) {
    return corsResponse;
  }
  
  const response = new Response(
    JSON.stringify({ message: 'API服务运行中' }),
    { headers: { 'Content-Type': 'application/json' } }
  );
  return addCorsHeaders(response);
}