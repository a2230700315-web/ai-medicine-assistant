// Cloudflare Pages 根路径函数
module.exports = {
  async fetch(request, env) {
    return new Response(
      JSON.stringify({ message: "AI药店培训助手API服务运行中" }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );
  }
};