@echo off
chcp 65001 > nul
echo ================================================
echo 饲料原料营销系统 - Windows 部署脚本
echo ================================================

:: 检查 Python 是否安装
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Python，请先安装 Python 3.8 或更高版本。
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo [成功] 检测到 Python 已安装

:: 检查 Git 是否安装
git --version > nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Git，请先安装 Git。
    echo 下载地址: https://git-scm.com/download/win
    pause
    exit /b 1
)
echo [成功] 检测到 Git 已安装

:: 安装 Hugo（如果未安装）
where hugo > nul 2>&1
if %errorlevel% neq 0 (
    echo [信息] 正在安装 Hugo...
    choco install hugo -y
    if %errorlevel% neq 0 (
        echo [警告] 使用 Chocolatey 安装 Hugo 失败，请手动安装。
        echo 下载地址: https://github.com/gohugoio/hugo/releases
    ) else (
        echo [成功] Hugo 安装完成
    )
) else (
    echo [成功] 检测到 Hugo 已安装
)

:: 初始化 Hugo 站点（如果未初始化）
if not exist "config.toml" (
    echo [信息] 正在初始化 Hugo 站点...
    hugo new site .
    if %errorlevel% neq 0 (
        echo [错误] Hugo 站点初始化失败
        pause
        exit /b 1
    )
    echo [成功] Hugo 站点初始化完成
) else (
    echo [成功] Hugo 站点已初始化
)

:: 安装 Ananke 主题
if not exist "themes\ananke" (
    echo [信息] 正在安装 Ananke 主题...
    git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
    if %errorlevel% neq 0 (
        echo [警告] 安装 Ananke 主题失败，请手动安装。
    ) else (
        echo [成功] Ananke 主题安装完成
        echo theme = "ananke" >> config.toml
    )
) else (
    echo [成功] Ananke 主题已安装
)

:: 生成核心文件
echo [信息] 正在生成核心文件...
python generate_core_files.py "%cd%"
if %errorlevel% neq 0 (
    echo [错误] 生成核心文件失败
    pause
    exit /b 1
)
echo [成功] 核心文件生成完成

:: 生成页面文件
echo [信息] 正在生成页面文件...
python generate_pages_files.py "%cd%"
if %errorlevel% neq 0 (
    echo [错误] 生成页面文件失败
    pause
    exit /b 1
)
echo [成功] 页面文件生成完成

:: 生成自动化文件
echo [信息] 正在生成自动化文件...
python generate_automation_files.py "%cd%"
if %errorlevel% neq 0 (
    echo [错误] 生成自动化文件失败
    pause
    exit /b 1
)
echo [成功] 自动化文件生成完成

:: 生成营销文件
echo [信息] 正在生成营销文件...
python generate_marketing_files.py "%cd%"
if %errorlevel% neq 0 (
    echo [错误] 生成营销文件失败
    pause
    exit /b 1
)
echo [成功] 营销文件生成完成

:: 本地预览（可选）
set /p preview="是否立即本地预览网站？(Y/N): "
if /i "%preview%"=="Y" (
    echo [信息] 正在启动 Hugo 本地服务器...
    echo [提示] 请在浏览器中访问 http://localhost:1313
    echo [提示] 按 Ctrl+C 停止服务器
    hugo server -D
)

echo ================================================
echo 部署脚本执行完成！
echo ================================================
pause
