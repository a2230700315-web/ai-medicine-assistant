@echo off
chcp 65001 >nul
echo ================================================
echo Vosk语音识别环境配置脚本
echo ================================================
echo.

echo [1/4] 检查Python环境...
python --version
if %errorlevel% neq 0 (
    echo 错误：未找到Python，请先安装Python 3.8或更高版本
    pause
    exit /b 1
)
echo Python环境检查通过
echo.

echo [2/4] 安装vosk库...
pip install vosk
if %errorlevel% neq 0 (
    echo 警告：vosk安装失败，请检查网络连接
)
echo vosk安装完成
echo.

echo [3/4] 安装sounddevice库...
pip install sounddevice
if %errorlevel% neq 0 (
    echo 警告：sounddevice安装失败，请检查网络连接
)
echo sounddevice安装完成
echo.

echo [4/4] 安装numpy库...
pip install numpy
if %errorlevel% neq 0 (
    echo 警告：numpy安装失败，请检查网络连接
)
echo numpy安装完成
echo.

echo [5/5] 安装websockets库...
pip install websockets
if %errorlevel% neq 0 (
    echo 警告：websockets安装失败，请检查网络连接
)
echo websockets安装完成
echo.

echo ================================================
echo 环境配置完成！
echo ================================================
echo.
echo 下一步：
echo 1. 下载Vosk中文模型（如果还没有）
echo 2. 运行 start_all.bat 启动服务
echo.
pause