# 语音输入功能演示

这是一个基于 React 的语音输入演示项目，使用浏览器原生的 Web Speech API 实现语音识别功能。

## 功能特性

- 实时语音识别（中文）
- 录音状态可视化
- 语音转文字输入
- 简洁的聊天界面

## 技术栈

- React 18
- Vite
- Web Speech API
- Lucide React（图标库）

## 安装和运行

1. 安装依赖：
```bash
npm install
```

2. 启动开发服务器：
```bash
npm run dev
```

3. 在浏览器中打开显示的地址（通常是 http://localhost:3001）

## 使用说明

1. 点击蓝色麦克风按钮开始录音
2. 说话时会实时显示识别结果
3. 再次点击按钮停止录音并提交
4. 支持中文语音识别
5. 需要浏览器支持 Web Speech API（推荐使用 Chrome）

## 浏览器兼容性

- Chrome/Edge: 完全支持
- Firefox: 部分支持
- Safari: 部分支持
- 其他浏览器: 可能不支持

## 注意事项

- 需要麦克风权限
- 首次使用时浏览器会请求麦克风权限
- 语音识别需要网络连接
- 识别准确度取决于语音清晰度和环境噪音

## 集成到现有项目

可以将 `src/components/VoiceInput.jsx` 组件复制到你的项目中，并在需要的地方引入使用：

```jsx
import VoiceInput from './components/VoiceInput'

function YourComponent() {
  const handleTranscript = (text, isInterim, isFinal) => {
    console.log('识别结果:', text)
    if (isFinal) {
      // 处理最终识别结果
    }
  }

  return (
    <VoiceInput onTranscript={handleTranscript} disabled={false} />
  )
}
```

## 后续集成豆包 API

当前使用浏览器原生语音识别。如需集成豆包语音识别 API，需要：

1. 获取豆包 API 凭证
2. 实现音频录制和上传功能
3. 调用豆包语音识别接口
4. 处理识别结果

参考文档：https://www.volcengine.com/docs/6561/1798094