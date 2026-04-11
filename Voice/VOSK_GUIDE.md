# Vosk实时语音识别配置指南

## 概述

Vosk是一个开源的离线语音识别工具包，提供真正的流式实时识别能力。本指南说明如何部署和使用Vosk实时语音识别系统，实现零延迟的语音转文字功能。

## 技术特点

**Vosk + WebSocket实时识别**
- ✅ 真正的流式实时识别，每检测到一个字就立即输出
- ✅ 零延迟，所见即所得，无需等待完整句子
- ✅ 使用vosk-model-small-cn模型，内存占用<100MB
- ✅ 完全离线运行，保护隐私安全
- ✅ 底层直接捕获麦克风流，跳过浏览器中间层

## 系统要求

### 硬件要求
- **CPU**: 双核心以上
- **内存**: 2GB以上（模型占用<100MB）
- **麦克风**: 标准音频输入设备
- **存储**: 500MB可用空间

### 软件要求
- **操作系统**: Windows 10/11, Linux, macOS
- **Python**: 3.8及以上
- **音频驱动**: 支持标准音频输入

## 安装步骤

### 1. 安装Python依赖

```bash
# 创建虚拟环境（推荐）
conda create --name vosk python=3.9
conda activate vosk

# 或使用venv
python -m venv vosk_env
vosk_env\Scripts\activate  # Windows
source vosk_env/bin/activate  # Linux/macOS

# 安装依赖包
pip install -r requirements_vosk.txt
```

### 2. 下载Vosk中文模型

#### 方法一：自动下载（推荐）

首次运行时会自动下载模型到当前目录。

#### 方法二：手动下载

访问Vosk模型官网下载：
- https://alphacephei.com/vosk/models

推荐下载：
- **vosk-model-small-cn-0.22** (~50MB) - 小型中文模型
- **vosk-model-cn-0.22** (~1.2GB) - 完整中文模型

解压后重命名为 `vosk-model-small-cn` 并放在项目目录下。

### 3. 安装音频驱动

#### Windows
```bash
# 安装PyAudio（需要PortAudio）
pip install pipwin
pipwin install pyaudio
```

#### Linux
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

#### macOS
```bash
brew install portaudio
pip install pyaudio
```

## 配置说明

### 环境变量配置

创建 `.env` 文件：

```env
# Vosk模型路径
VOSK_MODEL_PATH=vosk-model-small-cn

# WebSocket服务器配置
WS_HOST=0.0.0.0
WS_PORT=8765

# 音频配置
SAMPLE_RATE=16000
CHUNK_DURATION=0.1

# 识别参数
SILENCE_THRESHOLD=0.01
MIN_SPEECH_DURATION=0.3
```

## 使用方式

### 方式一：直接使用音频处理器

```bash
# 运行音频处理器
python audio_processor.py
```

功能：
- 直接从麦克风捕获音频
- 实时语音识别
- 控制台输出识别结果

### 方式二：使用WebSocket服务器（推荐）

```bash
# 启动WebSocket服务器
python vosk_websocket_server.py
```

服务器将在 `ws://localhost:8765` 启动

### 方式三：使用Web界面

1. 启动WebSocket服务器：`python vosk_websocket_server.py`
2. 在浏览器中打开：`vosk_realtime_demo.html`
3. 点击"开始识别"按钮
4. 开始说话，实时查看识别结果

## API接口说明

### WebSocket消息格式

#### 客户端发送消息

**开始识别：**
```json
{
  "action": "start"
}
```

**停止识别：**
```json
{
  "action": "stop"
}
```

**查询状态：**
```json
{
  "action": "status"
}
```

#### 服务器发送消息

**连接确认：**
```json
{
  "type": "connected",
  "message": "Vosk实时语音识别服务已连接",
  "timestamp": "14:30:25.123"
}
```

**部分识别结果：**
```json
{
  "type": "partial",
  "text": "你好",
  "timestamp": "14:30:26.456"
}
```

**最终识别结果：**
```json
{
  "type": "final",
  "text": "你好，我是AI助手",
  "timestamp": "14:30:27.789",
  "duration": 1.5
}
```

**状态更新：**
```json
{
  "type": "status",
  "is_running": true,
  "memory_mb": 45.2,
  "clients_count": 1,
  "timestamp": "14:30:28.012"
}
```

## 性能优化

### 模型选择

| 模型 | 大小 | 内存占用 | 速度 | 准确度 | 推荐场景 |
|------|------|----------|------|----------|----------|
| vosk-model-small-cn | ~50MB | ~50MB | 极快 | 中等 | **实时对话** |
| vosk-model-cn | ~1.2GB | ~500MB | 快 | 高 | 专业应用 |

### 音频参数优化

```python
# 在audio_processor.py中调整参数
SAMPLE_RATE = 16000        # 采样率（越高越准确但占用更多资源）
CHUNK_DURATION = 0.1       # 音频块大小（越小越实时）
SILENCE_THRESHOLD = 0.01  # 静音阈值
MIN_SPEECH_DURATION = 0.3  # 最小语音持续时间
```

### 内存优化

- 使用small模型，内存占用<100MB
- 及时清理音频缓冲区
- 限制历史记录数量

## 故障排除

### 麦克风无法访问

**问题：** 无法捕获音频输入

**解决方案：**
```bash
# 检查音频设备
python -c "import sounddevice as sd; print(sd.query_devices())"

# 指定音频设备
sd.InputStream(device=1, ...)  # 使用设备ID
```

### 模型加载失败

**问题：** 无法加载Vosk模型

**解决方案：**
- 检查模型路径是否正确
- 确保模型文件完整
- 尝试重新下载模型

### WebSocket连接失败

**问题：** 无法连接到WebSocket服务器

**解决方案：**
- 确认服务器已启动
- 检查端口是否被占用
- 检查防火墙设置

### 识别准确度低

**问题：** 识别结果不准确

**解决方案：**
- 使用更大的模型（vosk-model-cn）
- 调整音频采样率
- 改善录音环境（减少噪音）
- 确保麦克风质量

### 内存占用过高

**问题：** 内存使用超过100MB

**解决方案：**
- 使用small模型
- 清理音频缓冲区
- 限制并发连接数

## 对比其他方案

| 特性 | 浏览器Web Speech API | 豆包API | Vosk实时 |
|------|---------------------|---------|----------|
| 识别速度 | 慢（有延迟） | 中等 | **极快（零延迟）** |
| 准确度 | 中等 | 高 | **高** |
| 隐私性 | 低 | 中等 | **高** |
| 网络依赖 | 需要 | 需要 | **不需要** |
| 成本 | 免费 | 付费 | **免费** |
| 实时性 | 差 | 中等 | **优秀** |
| 内存占用 | 低 | 中等 | **<100MB** |
| 部署难度 | 无 | 中等 | **简单** |

## 技术架构

### 音频处理流程

```
麦克风 → sounddevice → 音频回调 → 语音检测 → 
Vosk识别 → 结果输出 → WebSocket广播 → Web界面显示
```

### 实时识别机制

1. **音频捕获**：使用sounddevice直接从底层捕获麦克风流
2. **语音检测**：实时检测语音开始和结束
3. **流式识别**：Vosk支持部分结果实时输出
4. **结果广播**：通过WebSocket实时推送到所有连接的客户端

### 内存管理

- 音频缓冲区：动态管理，及时清理
- 模型加载：单例模式，避免重复加载
- 历史记录：限制数量，自动清理

## 示例代码

### JavaScript客户端示例

```javascript
const ws = new WebSocket('ws://localhost:8765');

ws.onopen = function() {
    // 开始识别
    ws.send(JSON.stringify({ action: 'start' }));
};

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    
    if (data.type === 'partial') {
        console.log('实时识别:', data.text);
    } else if (data.type === 'final') {
        console.log('最终结果:', data.text);
    }
};

// 停止识别
ws.send(JSON.stringify({ action: 'stop' }));
```

### Python客户端示例

```python
import asyncio
import websockets
import json

async def vosk_client():
    async with websockets.connect('ws://localhost:8765') as ws:
        # 开始识别
        await ws.send(json.dumps({ 'action': 'start' }))
        
        # 接收识别结果
        async for message in ws:
            data = json.loads(message)
            
            if data['type'] == 'partial':
                print(f"实时识别: {data['text']}")
            elif data['type'] == 'final':
                print(f"最终结果: {data['text']}")

asyncio.run(vosk_client())
```

## 总结

Vosk实时语音识别方案提供了：
- ✅ 真正的流式实时识别（零延迟）
- ✅ 所见即所得（每字即出）
- ✅ 低内存占用（<100MB）
- ✅ 完全离线运行
- ✅ 免费开源使用
- ✅ 简单部署配置

特别适合需要实时、快速、准确的语音识别应用场景，如实时字幕、语音助手、会议记录等。