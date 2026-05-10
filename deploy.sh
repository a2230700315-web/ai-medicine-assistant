#!/bin/bash
# 前端自动部署脚本
# 用法：bash /www/wwwroot/deploy/deploy.sh

set -e

REPO_DIR="/www/wwwroot/deploy/ai-medicine-assistant"
WEB_DIR="/www/wwwroot/a1sc.cn"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 开始部署..."

cd "$REPO_DIR"

echo "拉取最新代码..."
git pull origin main

echo "安装依赖..."
npm install --legacy-peer-deps

echo "打包前端..."
npm run build

echo "更新静态文件..."
# 保留 .well-known 目录（SSL验证用）
rsync -av --delete --exclude='.well-known' dist/ "$WEB_DIR/"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 前端部署完成！"
