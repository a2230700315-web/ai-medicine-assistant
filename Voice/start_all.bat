@echo off
chcp 65001 >nul
echo ================================================
echo Vosk实时语音识别服务启动脚本
echo ================================================
echo.

echo 检查Vosk模型...
if not exist "vosk-model-small-cn" (
    echo 警告：未找到Vosk中文模型
    echo.
    echo 请先下载模型：
    echo 1. 访问 https://alphacephei.com/vosk/models
    echo 2. 下载 vosk-model-small-cn-0.22.zip
    echo 3. 解压到项目目录
    echo 4. 重命名文件夹为 vosk-model-small-cn
    echo.
    pause
    exit /b 1
)
echo Vosk模型检查通过
echo.

echo [1/2] 启动WebSocket服务器...
start "Vosk WebSocket服务器" python vosk_websocket_server.py
echo WebSocket服务器已启动（端口8765）
echo.

echo 等待服务器启动...
timeout /t 3 /nobreak >nul

echo [2/2] 打开Web测试界面...
start vosk_realtime_demo.html
echo Web测试界面已打开
echo.

echo ================================================
echo 服务启动完成！
echo ================================================
echo.
echo 说明：
echo - WebSocket服务器运行在后台窗口
echo - Web界面已打开，可以开始测试语音识别
echo - 关闭此窗口不会停止服务
echo - 要停止服务，请关闭WebSocket服务器窗口
echo.
pause