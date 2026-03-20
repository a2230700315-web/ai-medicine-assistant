# 豆包语音识别配置指南

## 概述

本指南说明如何配置和使用豆包语音识别功能替代浏览器原生语音识别。

## 准备工作

### 1. 获取豆包API凭据

访问火山引擎控制台获取API密钥：

1. 访问：https://console.volcengine.com/
2. 注册/登录账号
3. 创建应用并获取以下信息：
   - **APP ID** (VOLC_APP_KEY)
   - **Access Key** (VOLC_ACCESS_KEY)
   - **Resource ID** (默认为 volc.lark.minutes)

### 2. 安装依赖

```bash
pip install fastapi uvicorn python-dotenv httpx
```

### 3. 配置环境变量

复制 `.env.example` 文件为 `.env`：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的API凭据：

```env
VOLC_APP_KEY=your_actual_app_key
VOLC_ACCESS_KEY=your_actual_access_key
VOLC_RESOURCE_ID=volc.lark.minutes
```

## 启动服务

### 启动后端API服务

```bash
python backend.py
```

服务将在 http://localhost:8000 启动

### 验证配置

访问 http://localhost:8000/api/voice/status 检查配置状态：

```json
{
  "app_key_configured": true,
  "access_key_configured": true,
  "resource_id": "volc.lark.minutes",
  "status": "ready"
}
```

## 使用方式

### 方式一：在React项目中使用

1. 引入豆包语音组件：

```jsx
import VoiceInputDoubao from './components/VoiceInputDoubao'
```

2. 在组件中使用：

```jsx
<VoiceInputDoubao 
  onTranscript={handleTranscript}
  disabled={isLoading}
/>
```

### 方式二：在HTML页面中使用

修改 `simple-demo.html`，将浏览器原生语音识别替换为豆包API调用。

## API接口说明

### POST /api/voice/transcribe

上传音频文件进行语音识别。

**请求：**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (音频文件)

**响应：**
```json
{
  "text": "识别的文本内容",
  "status": "success",
  "task_id": "任务ID"
}
```

### GET /api/voice/status

检查API配置状态。

**响应：**
```json
{
  "app_key_configured": true,
  "access_key_configured": true,
  "resource_id": "volc.lark.minutes",
  "status": "ready"
}
```

## 技术架构

```
前端 (React/HTML)
    ↓ 录音
    ↓ 上传音频
后端 (FastAPI)
    ↓ 调用豆包API
豆包语音识别服务
    ↓ 返回识别结果
前端显示
```

## 注意事项

1. **API配额**：豆包API有调用频率和配额限制
2. **网络要求**：需要稳定的网络连接访问豆包API
3. **音频格式**：支持WAV格式音频
4. **识别语言**：当前配置为中文 (zh_cn)
5. **隐私安全**：不要将.env文件提交到版本控制

## 故障排除

### 配置错误

- 检查.env文件是否存在
- 确认API凭据正确
- 验证网络连接

### 识别失败

- 检查API配额是否充足
- 查看后端日志获取详细错误
- 确认音频文件格式正确

### 无法访问麦克风

- 检查浏览器权限设置
- 确保使用HTTPS协议
- 尝试使用Chrome或Edge浏览器

## 参考文档

- 豆包语音识别API：https://www.volcengine.com/docs/6561/1798094
- FastAPI文档：https://fastapi.tiangolo.com/
- Web Speech API：https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API

## 对比

| 特性 | 浏览器原生 | 豆包API |
|------|------------|----------|
| 准确度 | 中等 | 高 |
| 网络依赖 | 需要 | 需要 |
| API成本 | 免费 | 按量付费 |
| 隐私性 | 发送到云端 | 发送到云端 |
| 配置复杂度 | 无 | 需要配置 |
| 识别速度 | 快 | 较快 |

## 总结

通过以上配置，即可使用豆包语音识别功能替代浏览器原生语音识别，获得更高的识别准确度和稳定性。