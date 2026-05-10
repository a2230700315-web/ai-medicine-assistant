#!/bin/bash
# 后端重启脚本
# 用法：bash /www/wwwroot/deploy/restart_api.sh

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 重启后端服务..."

# 停止旧进程
pkill -f "uvicorn main:app" 2>/dev/null || true
sleep 2

# 启动新进程
cd /www/wwwroot/api
nohup python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 >> /www/wwwlogs/api.log 2>&1 &

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 后端重启完成，PID: $!"
