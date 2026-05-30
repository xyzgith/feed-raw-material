@echo off
chcp 65001 >nul
title Feed Raw Material Webhook Service
echo ==========================================
echo   Feed Raw Material WeChat Webhook
echo ==========================================
echo.
echo [1/2] Starting Flask app on port 5000...
cd /d F:\feed-raw-material\static\wecom
set PYTHONIOENCODING=utf-8
start "Flask" /min python app.py
echo   Flask started in background
echo.
echo [2/2] Starting LocalTunnel public tunnel...
start "LocalTunnel" /min cmd /c "D:\qclaw\resources\openclaw\config\bin\npx.cmd localtunnel --port 5000 --subdomain feed-raw-material"
echo   LocalTunnel started in background
echo.
echo ==========================================
echo   Services started!
echo   Webhook URL: https://feed-raw-material.loca.lt/wecom/webhook
echo   Health Check: http://127.0.0.1:5000/health
echo ==========================================
echo.
echo Press any key to close this window (services keep running)...
pause >nul
