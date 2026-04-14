# 药房健康顾问培训平台

基于 React + FastAPI + 火山引擎的 AI 模拟销售培训系统，专为药店店员设计。

## 功能特性

### 核心功能
- 🎯 **模拟对话系统** - AI 扮演挑剔顾客，提供真实销售场景
- 📊 **实战考评系统** - 4维度评分（专业知识、沟通技巧、推销意识、合规性）
- 📈 **能力雷达图** - ECharts 可视化展示能力评估
- 🏆 **勋章系统** - 5个等级成就激励
- 💾 **本地进度存储** - 自动保存学习进度
- 📚 **知识库集成** - RAG 技术提供实时反馈

### 考试模式
- 🎓 **练习模式** - 显示案例档案和知识助手
- 📝 **考试模式** - 隐藏所有提示，检验真实能力

### 案例管理
- 📋 **6大病症分类** - 高血糖、高血压、高血脂、高尿酸、中医内科、消化内科
- 👥 **100+ 模拟案例** - 涵盖不同年龄、症状和需求
- 🎯 **销售目标导向** - 每个案例都有明确的销售目标

## 技术栈

### 前端
- React 18
- Tailwind CSS
- Vite
- ECharts (雷达图)
- Lucide React (图标)

### 后端
- FastAPI
- Uvicorn
- 火山引擎 (Ark/豆包)
- SSE (Server-Sent Events) 流式响应

### 部署
- Vercel (前端 + 后端)

## 快速开始

### 本地开发

#### 1. 克隆项目
```bash
git clone <repository-url>
cd AI医药助教
```

#### 2. 安装依赖

**前端依赖：**
```bash
npm install
```

**后端依赖：**
```bash
pip install -r requirements.txt
```

#### 3. 配置环境变量

复制 `.env.example` 为 `.env` 并填入真实密钥：

```bash
cp .env.example .env
```

编辑 `.env` 文件：
```
VOLC_API_KEY=your_api_key_here
VOLC_ENDPOINT_ID=your_endpoint_id_here
```

#### 4. 启动服务

**启动前端：**
```bash
npm run dev
```

**启动后端：**
```bash
python backend.py
```

#### 5. 访问应用

- 前端: http://localhost:3000
- 后端 API: http://localhost:8001

## Vercel 部署

详细的部署指南请参考 [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md)

### 快速部署

1. **准备环境变量**
   - 在 Vercel 项目设置中添加 `VOLC_API_KEY` 和 `VOLC_ENDPOINT_ID`

2. **部署项目**
   ```bash
   # 安装 Vercel CLI
   npm i -g vercel
   
   # 登录并部署
   vercel login
   vercel --prod
   ```

3. **验证部署**
   - 访问: `https://your-project.vercel.app/`
   - API: `https://your-project.vercel.app/api/`

## 项目结构

```
AI医药助教/
├── api/
│   └── index.py              # Vercel Python 入口
├── public/
│   └── cases.json           # 案例数据
├── knowledge/
│   └── industry_standard.json # 知识库
├── src/
│   ├── components/           # React 组件
│   │   ├── Dashboard.jsx
│   │   ├── ChatInterface.jsx
│   │   ├── KnowledgeAssistant.jsx
│   │   ├── CaseCategorySelector.jsx
│   │   ├── CaseList.jsx
│   │   ├── CaseDetail.jsx
│   │   └── ReviewModal.jsx
│   └── utils/
│       └── progressStorage.js
├── backend.py               # FastAPI 后端
├── vercel.json            # Vercel 配置
├── requirements.txt        # Python 依赖
├── package.json          # 前端依赖
├── .env.example        # 环境变量模板
└── .gitignore         # Git 忽略文件
```

## API 接口

### 获取案例列表
```http
GET /api/cases
```

### 流式对话
```http
POST /api/chat/stream
Content-Type: application/json

{
  "messages": [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "您好"}
  ],
  "practice_case": {
    "name": "张伟",
    "age": 45,
    "现病史": "..."
  },
  "temperature": 0.8,
  "max_tokens": 500
}
```

### 复盘分析
```http
POST /api/chat/review
Content-Type: application/json

{
  "messages": [...],
  "practice_case": {...}
}
```

## 勋章系统

| 分数 | 勋章 | 标题 |
|------|------|------|
| 90-100 | 🏆 | 金牌药师 |
| 80-89 | 🥈 | 银牌药师 |
| 70-79 | ⭐ | 销售之星 |
| 60-69 | ✅ | 合格药师 |
| <60 | 📚 | 继续努力 |

## 评分维度

### 专业知识 (25分)
- 病症识别准确性
- 产品知识掌握程度
- 联合用药合理性

### 沟通技巧 (25分)
- 礼仪和态度
- 需求挖掘能力
- 异议处理技巧

### 推销意识 (25分)
- 关联推销主动性
- 机会把握能力
- 促成技巧运用

### 合规性 (25分)
- 禁忌症询问
- 用药安全提醒
- 职业道德规范

## 常见问题

### Q: 如何获取火山引擎 API 密钥？
A: 访问 [火山引擎控制台](https://console.volcengine.com/ark) 创建应用并获取 API 密钥。

### Q: 本地开发时 API 请求失败？
A: 检查 `.env` 文件是否正确配置，确保 `VOLC_API_KEY` 和 `VOLC_ENDPOINT_ID` 已填入。

### Q: 部署到 Vercel 后 API 无法访问？
A: 在 Vercel 项目设置中添加环境变量，并重新部署项目。

### Q: 如何添加新的案例？
A: 编辑 `public/cases.json` 文件，按照现有格式添加新案例。

### Q: 如何修改知识库？
A: 编辑 `knowledge/industry_standard.json` 文件，添加或修改销售知识。

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 联系方式

如有问题，请通过以下方式联系：
- 提交 GitHub Issue
- 发送邮件至项目维护者

---

**祝您学习愉快，早日成为金牌药师！** 🏆
# ai-medicine-assistant
