#!/bin/bash

set -e

echo "=========================================="
echo "药店AI培训系统 - 阿里云服务器部署脚本"
echo "=========================================="

APP_DIR="/opt/pharmacy-api"
SERVICE_NAME="pharmacy-api"

echo ""
echo "[1/6] 安装系统依赖..."
apt-get update
apt-get install -y python3 python3-pip python3-venv nginx

echo ""
echo "[2/6] 创建应用目录..."
mkdir -p $APP_DIR

echo ""
echo "[3/6] 复制应用文件..."
cp -r ../main.py $APP_DIR/
cp -r ../init_db.py $APP_DIR/
cp -r ../requirements.txt $APP_DIR/
cp -r ../index.py $APP_DIR/ 2>/dev/null || true

echo ""
echo "[4/6] 创建虚拟环境并安装依赖..."
cd $APP_DIR
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "[5/6] 初始化数据库..."
python init_db.py

echo ""
echo "[6/6] 配置 Systemd 服务..."
cp pharmacy-api.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable pharmacy-api
systemctl start pharmacy-api

echo ""
echo "=========================================="
echo "部署完成！"
echo "=========================================="
echo ""
echo "API 服务已启动在: http://$(curl -s ifconfig.me):8000"
echo ""
echo "常用命令："
echo "  查看状态: systemctl status pharmacy-api"
echo "  重启服务: systemctl restart pharmacy-api"
echo "  查看日志: journalctl -u pharmacy-api -f"
echo ""
echo "Nginx 配置文件: api/deploy/nginx.conf"
echo "请将 nginx.conf 复制到 /etc/nginx/sites-available/ 并启用"
echo ""
