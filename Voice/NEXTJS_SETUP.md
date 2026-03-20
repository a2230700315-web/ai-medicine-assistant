# AI医药助教 - Next.js 15 配置说明

## 🌐 局域网访问配置

### 开发环境启动
```bash
npm run dev
```

**关键参数**：`-H 0.0.0.0` 允许从局域网任何设备访问

### 生产环境启动
```bash
npm run build
npm start
```

## 📱 移动端测试步骤

### 1. 获取本机IP地址
**Windows**:
```bash
ipconfig
```
查找 "IPv4 地址"，例如：`192.168.1.100`

**Mac/Linux**:
```bash
ifconfig | grep "inet "
```

### 2. 手机访问
- 确保手机和电脑在同一WiFi网络
- 在手机浏览器中输入：`http://192.168.1.100:3000`
- 替换 `192.168.1.100` 为你的实际IP地址

### 3. 端口说明
- **前端端口**：3000（Next.js开发服务器）
- **后端API端口**：8000（FastAPI）
- **WebSocket端口**：8765（Vosk实时识别）

## 🔧 配置文件说明

### next.config.js
```javascript
const nextConfig = {
  reactStrictMode: true,
  
  // CORS配置 - 允许跨域请求
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'Access-Control-Allow-Origin',
            value: '*',
          },
        ],
      },
    ]
  },

  // API代理 - 将前端请求转发到后端
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://localhost:8000/api/:path*',
      },
    ]
  },
}
```

### 环境变量配置 (.env.local)
```bash
# API服务地址
NEXT_PUBLIC_API_URL=http://192.168.1.100:8000

# WebSocket服务地址
NEXT_PUBLIC_WS_URL=ws://192.168.1.100:8765

# 豆包语音识别配置
VOLC_APP_KEY=your_app_key
VOLC_ACCESS_KEY=your_access_key
VOLC_RESOURCE_ID=your_resource_id
VOLC_SERVICE_TYPE=streaming
```

## 🚀 完整启动流程

### 方式1：仅启动前端（使用浏览器原生语音识别）
```bash
# 终端1：启动Next.js前端
npm run dev
```

### 方式2：启动前端+后端（使用豆包语音识别）
```bash
# 终端1：启动Next.js前端
npm run dev

# 终端2：启动FastAPI后端
pip install -r requirements.txt
python backend.py
```

### 方式3：启动前端+后端+Vosk（使用离线语音识别）
```bash
# 终端1：启动Next.js前端
npm run dev

# 终端2：启动FastAPI后端
python backend.py

# 终端3：启动Vosk WebSocket服务
python vosk_websocket_server.py
```

## 📋 网络配置检查清单

- [ ] 电脑和手机在同一WiFi网络
- [ ] 防火墙允许端口3000、8000、8765
- [ ] .env.local中配置了正确的IP地址
- [ ] 后端服务已启动（如使用豆包或Vosk）
- [ ] 手机浏览器支持Web Speech API（推荐Chrome）

## 🔒 防火墙配置

### Windows防火墙
1. 打开"Windows Defender 防火墙"
2. 点击"允许应用通过防火墙"
3. 勾选"Node.js"或手动添加端口3000、8000、8765

### Mac防火墙
1. 打开"系统偏好设置" > "安全性与隐私"
2. 点击"防火墙选项"
3. 添加Node.js应用或允许指定端口

## 📱 移动端浏览器兼容性

| 浏览器 | Web Speech API | WebSocket | 推荐度 |
|--------|---------------|-----------|--------|
| Chrome | ✅ 完全支持 | ✅ 完全支持 | ⭐⭐⭐⭐⭐ |
| Edge | ✅ 完全支持 | ✅ 完全支持 | ⭐⭐⭐⭐⭐ |
| Safari | ⚠️ 部分支持 | ✅ 完全支持 | ⭐⭐⭐ |
| Firefox | ⚠️ 部分支持 | ✅ 完全支持 | ⭐⭐⭐ |

## 🐛 常见问题

### 1. 手机无法访问
**解决方案**：
- 检查IP地址是否正确
- 确认防火墙设置
- 尝试关闭VPN或代理

### 2. 语音识别不工作
**解决方案**：
- 检查浏览器权限（麦克风）
- 使用Chrome浏览器
- 确认后端服务已启动

### 3. API请求失败
**解决方案**：
- 检查后端服务是否运行
- 确认.env.local中的API_URL配置
- 查看浏览器控制台错误信息

## 📊 性能优化建议

1. **生产环境构建**
   ```bash
   npm run build
   npm start
   ```

2. **启用CDN**（可选）
   - 静态资源上传到CDN
   - 配置next.config.js中的assetPrefix

3. **启用压缩**
   - Nginx配置gzip压缩
   - Next.js自动启用Brotli压缩

## 🎯 部署到生产环境

### Docker部署（推荐）
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

### Nginx反向代理
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```