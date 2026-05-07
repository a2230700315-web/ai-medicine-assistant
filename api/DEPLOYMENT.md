# 阿里云服务器部署指南

本文档介绍如何将药店AI培训系统后端部署到阿里云轻量应用服务器。

## 架构概览

```
┌─────────────────┐     ┌─────────────────┐
│  Cloudflare     │     │   阿里云服务器    │
│  Pages (前端)   │────▶│  FastAPI (后端)  │
│                 │     │                 │
│  - React SPA    │     │  - API 接口     │
│  - 静态资源     │     │  - SQLite 数据库 │
└─────────────────┘     └─────────────────┘
```

## 一、服务器准备

### 1.1 购买阿里云轻量应用服务器

- **推荐配置**：2核4G内存，带宽3Mbps以上
- **操作系统**：Ubuntu 22.04 或 CentOS 8
- **地域**：选择离用户最近的区域

### 1.2 连接服务器

```bash
ssh root@your_server_ip
```

### 1.3 更新系统

```bash
# Ubuntu
apt-get update && apt-get upgrade -y

# CentOS
yum update -y
```

## 二、安装依赖

### 2.1 安装 Python 3

```bash
# Ubuntu
apt-get install -y python3 python3-pip python3-venv

# CentOS
yum install -y python3 python3-pip
```

### 2.2 安装 Nginx

```bash
# Ubuntu
apt-get install -y nginx

# CentOS
yum install -y nginx
```

## 三、部署后端应用

### 3.1 创建应用目录

```bash
mkdir -p /opt/pharmacy-api
cd /opt/pharmacy-api
```

### 3.2 上传代码

方式一：使用 SCP 上传
```bash
# 在本地执行
scp -r api/* root@your_server_ip:/opt/pharmacy-api/
```

方式二：使用 Git 克隆
```bash
cd /opt
git clone https://github.com/your-repo/ai-medicine-assistant.git pharmacy-api
cd pharmacy-api/api
```

### 3.3 创建虚拟环境

```bash
cd /opt/pharmacy-api
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3.4 初始化数据库

```bash
python init_db.py
```

### 3.5 配置环境变量

编辑 `/opt/pharmacy-api/.env` 文件：
```bash
VOLC_API_KEY=your_volc_api_key
VOLC_ENDPOINT_ID=your_volc_endpoint_id
```

## 四、配置 Systemd 服务

### 4.1 创建服务文件

创建 `/etc/systemd/system/pharmacy-api.service`：

```ini
[Unit]
Description=Pharmacy AI Training API
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/pharmacy-api
Environment="PATH=/opt/pharmacy-api/venv/bin"
EnvironmentFile=/opt/pharmacy-api/.env
ExecStart=/opt/pharmacy-api/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### 4.2 启动服务

```bash
systemctl daemon-reload
systemctl enable pharmacy-api
systemctl start pharmacy-api
systemctl status pharmacy-api
```

### 4.3 查看日志

```bash
journalctl -u pharmacy-api -f
```

## 五、配置 Nginx 反向代理

### 5.1 创建 Nginx 配置

创建 `/etc/nginx/sites-available/pharmacy-api`：

```nginx
server {
    listen 80;
    server_name your-domain.com;  # 替换为你的域名或服务器IP
    
    # API 代理
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
        
        # 超时设置
        proxy_read_timeout 300s;
        proxy_connect_timeout 75s;
    }
    
    # 健康检查
    location /health {
        proxy_pass http://127.0.0.1:8000/health;
        access_log off;
    }
}
```

### 5.2 启用配置

```bash
# Ubuntu
ln -s /etc/nginx/sites-available/pharmacy-api /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx

# CentOS
cp /etc/nginx/sites-available/pharmacy-api /etc/nginx/conf.d/pharmacy-api.conf
nginx -t
systemctl restart nginx
```

### 5.3 开放防火墙端口

```bash
# Ubuntu (ufw)
ufw allow 80
ufw allow 443

# CentOS (firewalld)
firewall-cmd --permanent --add-port=80/tcp
firewall-cmd --permanent --add-port=443/tcp
firewall-cmd --reload
```

## 六、配置 HTTPS（可选但推荐）

### 6.1 安装 Certbot

```bash
# Ubuntu
apt-get install -y certbot python3-certbot-nginx

# CentOS
yum install -y certbot python3-certbot-nginx
```

### 6.2 申请 SSL 证书

```bash
certbot --nginx -d your-domain.com
```

## 七、前端配置

### 7.1 设置环境变量

在 Cloudflare Pages 设置环境变量：

| 变量名 | 值 |
|--------|-----|
| `VITE_API_BASE_URL` | `https://your-domain.com` 或 `http://your-server-ip` |

### 7.2 重新部署前端

Cloudflare Pages 会自动检测到环境变量变化并重新部署。

## 八、验证部署

### 8.1 测试 API

```bash
# 健康检查
curl http://your-server-ip/health

# 测试聊天接口
curl -X POST http://your-server-ip/api/chat/stream \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"你好"}],"difficulty":"medium"}'
```

### 8.2 检查服务状态

```bash
systemctl status pharmacy-api
systemctl status nginx
```

## 九、常用运维命令

### 服务管理

```bash
# 重启 API 服务
systemctl restart pharmacy-api

# 停止服务
systemctl stop pharmacy-api

# 查看日志
journalctl -u pharmacy-api -f --lines 100
```

### 数据库管理

```bash
# 备份数据库
cp /opt/pharmacy-api/pharmacy.db /opt/pharmacy-api/pharmacy.db.backup

# 查看数据库
sqlite3 /opt/pharmacy-api/pharmacy.db ".tables"
```

### 更新部署

```bash
cd /opt/pharmacy-api
git pull
source venv/bin/activate
pip install -r requirements.txt
systemctl restart pharmacy-api
```

## 十、故障排查

### API 无法访问

1. 检查服务状态：`systemctl status pharmacy-api`
2. 检查端口占用：`netstat -tlnp | grep 8000`
3. 检查防火墙：`ufw status` 或 `firewall-cmd --list-all`

### 502 Bad Gateway

1. 检查 API 服务是否运行
2. 检查 Nginx 配置：`nginx -t`
3. 查看 Nginx 错误日志：`tail -f /var/log/nginx/error.log`

### API 调用超时

1. 检查火山引擎 API 配置
2. 增加超时时间（在 Nginx 配置中）
3. 查看服务日志排查问题

## 十一、安全建议

1. **定期更新系统**：`apt-get update && apt-get upgrade`
2. **配置防火墙**：只开放必要端口
3. **使用 HTTPS**：配置 SSL 证书
4. **定期备份数据库**：设置定时备份任务
5. **监控服务状态**：使用监控工具或脚本

## 文件结构

```
api/
├── main.py              # FastAPI 主应用
├── init_db.py           # 数据库初始化脚本
├── requirements.txt     # Python 依赖
├── pharmacy.db          # SQLite 数据库（运行后生成）
├── .env                 # 环境变量（需创建）
├── .env.example         # 环境变量示例
└── deploy/
    ├── deploy.sh        # 部署脚本
    ├── pharmacy-api.service  # Systemd 服务配置
    └── nginx.conf       # Nginx 配置示例
```
