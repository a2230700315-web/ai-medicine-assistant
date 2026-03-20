# Vercel 部署指南

## 项目结构

```
AI医药助教/
├── api/
│   └── index.py          # Vercel Python 入口文件
├── public/
│   └── cases.json        # 案例数据
├── knowledge/
│   └── industry_standard.json  # 知识库
├── src/
│   └── components/       # React 组件
├── backend.py            # FastAPI 后端
├── vercel.json          # Vercel 配置
├── requirements.txt      # Python 依赖
├── package.json        # 前端依赖
└── .env.example       # 环境变量示例
```

## 部署步骤

### 1. 准备环境变量

在 Vercel 项目设置中添加以下环境变量：

- `VOLC_API_KEY`: 火山引擎 API 密钥
- `VOLC_ENDPOINT_ID`: 火山引擎端点 ID

### 2. 部署到 Vercel

#### 方法一：通过 Vercel CLI

```bash
# 安装 Vercel CLI
npm i -g vercel

# 登录 Vercel
vercel login

# 部署项目
vercel

# 生产环境部署
vercel --prod
```

#### 方法二：通过 GitHub 集成

1. 将代码推送到 GitHub 仓库
2. 在 Vercel 控制台点击 "New Project"
3. 导入 GitHub 仓库
4. 配置环境变量
5. 点击 "Deploy"

### 3. 配置说明

#### vercel.json 配置

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    },
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "dist"
      }
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/index.py"
    },
    {
      "src": "/(.*)",
      "dest": "/dist/$1"
    }
  ]
}
```

- `/api/*` 路由请求到 Python 后端
- 其他路由请求到前端静态文件

#### requirements.txt

确保包含所有 Python 依赖：

```
fastapi==0.104.1
uvicorn==0.24.0
python-dotenv==1.0.0
pydantic==2.5.0
pydantic-settings==2.1.0
sse-starlette==1.8.2
httpx==0.25.2
```

### 4. 环境变量管理

#### 本地开发

创建 `.env` 文件：

```
VOLC_API_KEY=your_api_key_here
VOLC_ENDPOINT_ID=your_endpoint_id_here
```

#### Vercel 生产环境

在 Vercel 项目设置中添加环境变量：
1. 进入项目设置
2. 选择 "Environment Variables"
3. 添加 `VOLC_API_KEY` 和 `VOLC_ENDPOINT_ID`
4. 重新部署项目

### 5. API 路由

后端 API 路由：

- `GET /api/` - 根路径
- `GET /api/cases` - 获取案例列表
- `POST /api/chat/stream` - 流式对话
- `POST /api/chat/review` - 复盘分析

前端调用示例：

```javascript
// 流式对话
const response = await fetch('/api/chat/stream', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ messages, practice_case })
})

// 复盘分析
const response = await fetch('/api/chat/review', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ messages, practice_case })
})
```

### 6. 常见问题

#### Q: API 请求失败

A: 检查环境变量是否正确配置，确保 `VOLC_API_KEY` 和 `VOLC_ENDPOINT_ID` 已在 Vercel 中设置。

#### Q: 静态文件 404

A: 确保 `vercel.json` 中的路由配置正确，前端构建输出目录为 `dist`。

#### Q: Python 后端无法启动

A: 检查 `api/index.py` 文件是否正确导入 `backend.py` 中的 `app` 实例。

### 7. 部署验证

部署完成后，访问以下地址验证：

- 前端: `https://your-project.vercel.app/`
- API: `https://your-project.vercel.app/api/`

### 8. 性能优化

- 启用 Vercel Edge Functions 加速 API 响应
- 配置 CDN 缓存静态资源
- 使用 Vercel Analytics 监控性能

## 技术栈

- **前端**: React + Tailwind CSS + Vite
- **后端**: FastAPI + Uvicorn
- **AI**: 火山引擎 (Ark/豆包)
- **部署**: Vercel
- **数据库**: JSON 文件存储

## 支持

如有问题，请查看：
- [Vercel Python 文档](https://vercel.com/docs/concepts/functions/serverless-functions)
- [FastAPI 文档](https://fastapi.tiangolo.com/)
