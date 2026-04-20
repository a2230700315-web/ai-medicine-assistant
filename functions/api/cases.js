export async function onRequestGet(context) {
  console.log('API Request Received');
  
  const { env } = context;
  
  try {
    const casesData = await env.ASSETS.fetch(new Request('/cases.json'));
    const cases = await casesData.json();

    console.log("=== 收到案例列表请求 ===");
    console.log(`案例数量: ${cases.length}`);

    return new Response(
      JSON.stringify(cases),
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