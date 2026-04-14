# 本地Whisper语音识别配置指南

## 概述

本指南说明如何部署和使用本地Whisper语音识别服务，实现快速、准确、离线的语音识别功能。

## 技术方案

**Faster-Whisper** - OpenAI Whisper的优化版本
- ✅ 识别速度快（比原版快70倍）
- ✅ 支持中文识别
- ✅ 完全离线运行
- ✅ 隐私安全，数据不上传云端
- ✅ 免费开源

## 系统要求

### 硬件要求
- **CPU**: 4核心以上
- **内存**: 8GB以上
- **GPU**: 可选，NVIDIA显卡（推荐）
- **存储**: 10GB可用空间

### 软件要求
- **操作系统**: Windows 10/11, Linux, macOS
- **Python**: 3.10及以上
- **CUDA**: 11.8+（如使用GPU加速）

## 安装步骤

### 1. 创建Python虚拟环境

```bash
# 使用conda创建环境（推荐）
conda create --name whisper python=3.10
conda activate whisper

# 或使用venv
python -m venv whisper_env
whisper_env\Scripts\activate  # Windows
source whisper_env/bin/activate  # Linux/macOS
```

### 2. 安装依赖

```bash
# 安装PyTorch（根据你的系统选择）
# CPU版本
pip install torch torchaudio

# GPU版本（CUDA 11.8）
pip install torch==2.0.0 torchaudio==2.0.0 --index-url https://download.pytorch.org/whl/cu118

# 安装其他依赖
pip install faster-whisper flask flask-cors python-dotenv numpy soundfile
```

### 3. 下载模型

Faster-Whisper会自动下载模型，首次使用时会下载：
- **tiny**: ~39MB，最快但准确度较低
- **base**: ~74MB，平衡速度和准确度
- **small**: ~244MB，推荐使用，准确度高
- **medium**: ~769MB，准确度更高
- **large**: ~1550MB，最高准确度但速度较慢

## 配置说明

### 环境变量配置

创建 `.env` 文件：

```env
# Whisper模型大小 (tiny/base/small/medium/large)
WHISPER_MODEL_SIZE=small

# 识别语言 (zh/en/ja等)
WHISPER_LANGUAGE=zh

# 服务端口
PORT=5000
```

### 启动服务

```bash
# 激活环境
conda activate whisper

# 启动服务
python local_whisper_server.py
```

服务将在 `http://localhost:5000` 启动

## API接口说明

### GET /api/voice/status

检查服务状态

**响应示例：**
```json
{
  "model": "small",
  "device": "cuda",
  "language": "zh",
  "cuda_available": true,
  "status": "ready"
}
```

### POST /api/voice/transcribe

上传音频文件进行识别

**请求：**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (音频文件)

**响应示例：**
```json
{
  "text": "识别的文本内容",
  "status": "success",
  "language": "zh",
  "duration": 5.23,
  "segments": [
    {
      "start": 0.0,
      "end": 2.5,
      "text": "识别的第一段文本"
    }
  ]
}
```

### POST /api/voice/transcribe_base64

使用Base64编码的音频数据进行识别

**请求：**
```json
{
  "audio_data": "base64编码的音频数据"
}
```

**响应：** 同上

## 使用方式

### 方式一：使用测试页面

1. 启动本地Whisper服务：`python local_whisper_server.py`
2. 在浏览器中打开：`local_whisper_demo.html`
3. 点击圆形按钮开始录音
4. 再次点击按钮停止录音
5. 查看识别结果

### 方式二：API调用

```javascript
// 上传音频文件
const formData = new FormData();
formData.append('audio', audioBlob, 'recording.wav');

const response = await fetch('http://localhost:5000/api/voice/transcribe', {
    method: 'POST',
    body: formData
});

const result = await response.json();
console.log(result.text);
```

## 性能优化

### GPU加速

如果有NVIDIA显卡，安装CUDA版本：

```bash
pip install torch==2.0.0 torchaudio==2.0.0 --index-url https://download.pytorch.org/whl/cu118
```

### 模型选择

根据需求选择模型大小：

| 模型 | 大小 | 速度 | 准确度 | 推荐场景 |
|------|------|------|----------|----------|
| tiny | 39MB | 最快 | 较低 | 实时对话 |
| base | 74MB | 快 | 中等 | 日常使用 |
| small | 244MB | 中等 | 高 | **推荐** |
| medium | 769MB | 慢 | 很高 | 专业应用 |
| large | 1550MB | 最慢 | 最高 | 离线处理 |

## 故障排除

### 模型下载失败

- 检查网络连接
- 手动下载模型文件放到指定目录
- 使用镜像源：`HF_ENDPOINT=https://hf-mirror.com`

### CUDA错误

- 确认显卡驱动版本
- 检查CUDA版本匹配
- 尝试使用CPU版本

### 内存不足

- 使用更小的模型（tiny/base）
- 关闭其他占用内存的程序
- 增加系统虚拟内存

### 识别速度慢

- 使用GPU加速
- 选择更小的模型
- 减少音频长度

## 对比其他方案

| 特性 | 浏览器原生 | 豆包API | 本地Whisper |
|------|------------|----------|--------------|
| 速度 | 快 | 中等 | **快** |
| 准确度 | 中等 | 高 | **高** |
| 隐私性 | 低 | 中等 | **高** |
| 网络依赖 | 需要 | 需要 | **不需要** |
| 成本 | 免费 | 付费 | **免费** |
| 部署难度 | 无 | 中等 | **简单** |

## 总结

本地Whisper语音识别方案提供了：
- ✅ 快速识别（比浏览器原生更快）
- ✅ 高准确度（专业级识别效果）
- ✅ 完全离线（保护隐私）
- ✅ 免费使用（无API费用）
- ✅ 简单部署（一键启动）

适合需要快速、准确、隐私安全的语音识别应用场景。