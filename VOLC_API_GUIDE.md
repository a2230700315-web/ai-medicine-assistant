# 火山引擎（Ark/豆包）API 集成指南

## 概述

本项目已集成火山引擎（Ark/豆包）API，支持流式对话输出和实时情绪分析。

## 环境配置

### 1. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

编辑 `.env` 文件，填入您的火山引擎 API 凭证：

```env
VOLC_API_KEY=your_api_key_here
VOLC_ENDPOINT_ID=your_endpoint_id_here
```

### 3. 启动后端服务

```bash
python backend.py
```

服务将在 `http://localhost:8001` 启动。

## API 端点

### 流式对话

**端点**: `POST /chat/stream`

**请求体**:
```json
{
  "messages": [
    {"role": "user", "content": "用户消息"},
    {"role": "assistant", "content": "AI回复"}
  ],
  "practice_case": {
    "category": "高血糖",
    "现病史": "空腹血糖8.5mmol/L...",
    "目前用药": "二甲双胍缓释片...",
    ...
  },
  "temperature": 0.8,
  "max_tokens": 500
}
```

**响应**: SSE 流式输出，每个字符逐个返回。

### 复盘分析

**端点**: `POST /chat/review`

**请求体**:
```json
{
  "messages": [...],
  "practice_case": {...}
}
```

**响应**:
```json
{
  "totalScore": 85,
  "scores": {
    "professionalism": 25,
    "communication": 26,
    "sales": 22,
    "attitude": 12
  },
  "strengths": ["优点1", "优点2"],
  "improvements": ["改进建议1", "改进建议2"]
}
```

### 获取案例列表

**端点**: `GET /cases`

**响应**: 返回所有案例数据。

## 前端特性

### 1. 流式输出
- 实时显示 AI 回复
- 打字机效果
- 加载动画

### 2. 顾客满意度进度条
- 根据对话动态更新
- 颜色变化：红→橙→黄→绿→翠绿
- 实时反馈顾客信任度

### 3. 销售阶段追踪
- 初次接触
- 询问了解
- 提出异议
- 考虑评估
- 决定购买
- 拒绝购买

### 4. 元数据解析
- 自动解析 `[METADATA]...[/METADATA]` 标签
- 提取 `trust_score` 和 `current_stage`
- 更新 UI 显示

## 使用流程

1. **启动后端**: `python backend.py`
2. **启动前端**: `npm run dev`
3. **选择案例**: 在左侧选择一个案例
4. **开始对话**: 点击"开始模拟练习"
5. **实时交互**: 观察顾客满意度和销售阶段变化
6. **复盘分析**: 对话结束后查看评分和建议

## 注意事项

1. 确保 `.env` 文件中的 API Key 和 Endpoint ID 正确
2. 后端服务必须在 `http://localhost:8000` 运行
3. 前端会自动连接到后端 API
4. 流式输出需要浏览器支持 SSE (Server-Sent Events)

## 故障排除

### 连接失败
- 检查后端是否正在运行
- 检查 `.env` 配置是否正确
- 查看浏览器控制台错误信息

### 流式输出中断
- 检查网络连接
- 查看后端日志
- 确认 API 配额充足

### 元数据解析失败
- 检查 AI 返回格式
- 查看浏览器控制台
- 确认后端 prompt 配置
