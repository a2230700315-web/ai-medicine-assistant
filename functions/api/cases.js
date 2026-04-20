const fs = require('fs');
const path = require('path');

// Cloudflare Pages 函数导出
module.exports = {
  async fetch(request, env) {
    // 只处理 GET 请求
    if (request.method !== 'GET') {
      return new Response(
        JSON.stringify({ error: 'Method Not Allowed' }),
        { status: 405, headers: { 'Content-Type': 'application/json' } }
      );
    }

    try {
      // 读取案例文件
      const casesPath = path.join('public', 'cases.json');
      const casesData = JSON.parse(fs.readFileSync(casesPath, 'utf8'));

      console.log("=== 收到案例列表请求 ===");
      console.log(`案例数量: ${casesData.length}`);

      return new Response(
        JSON.stringify(casesData),
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
};