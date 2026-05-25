#!/bin/bash

echo "================================================"
echo "饲料原料营销系统 - Linux/Mac 部署脚本"
echo "================================================"

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "[错误] 未检测到 Python，请先安装 Python 3.8 或更高版本。"
    echo "下载地址: https://www.python.org/downloads/"
    exit 1
fi

if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

echo "[成功] 检测到 Python 已安装: $($PYTHON_CMD --version)"

# 检查 Git 是否安装
if ! command -v git &> /dev/null; then
    echo "[错误] 未检测到 Git，请先安装 Git。"
    echo "下载地址: https://git-scm.com/download/linux"
    exit 1
fi

echo "[成功] 检测到 Git 已安装: $(git --version)"

# 安装 Hugo（如果未安装）
if ! command -v hugo &> /dev/null; then
    echo "[信息] 正在安装 Hugo..."
    
    # 尝试使用包管理器安装
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y hugo
    elif command -v yum &> /dev/null; then
        sudo yum install -y hugo
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y hugo
    elif command -v brew &> /dev/null; then
        brew install hugo
    else
        echo "[警告] 无法自动安装 Hugo，请手动安装。"
        echo "下载地址: https://github.com/gohugoio/hugo/releases"
    fi
    
    if [ $? -ne 0 ]; then
        echo "[警告] 安装 Hugo 失败，请手动安装。"
    else
        echo "[成功] Hugo 安装完成"
    fi
else
    echo "[成功] 检测到 Hugo 已安装: $(hugo version)"
fi

# 初始化 Hugo 站点（如果未初始化）
if [ ! -f "config.toml" ] && [ ! -f "hugo.toml" ]; then
    echo "[信息] 正在初始化 Hugo 站点..."
    hugo new site .
    if [ $? -ne 0 ]; then
        echo "[错误] Hugo 站点初始化失败"
        exit 1
    fi
    echo "[成功] Hugo 站点初始化完成"
else
    echo "[成功] Hugo 站点已初始化"
fi

# 安装 Ananke 主题
if [ ! -d "themes/ananke" ]; then
    echo "[信息] 正在安装 Ananke 主题..."
    git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
    if [ $? -ne 0 ]; then
        echo "[警告] 安装 Ananke 主题失败，请手动安装。"
    else
        echo "[成功] Ananke 主题安装完成"
        echo 'theme = "ananke"' >> config.toml
    fi
else
    echo "[成功] Ananke 主题已安装"
fi

# 生成核心文件
echo "[信息] 正在生成核心文件..."
$PYTHON_CMD generate_core_files.py "$(pwd)"
if [ $? -ne 0 ]; then
    echo "[错误] 生成核心文件失败"
    exit 1
fi
echo "[成功] 核心文件生成完成"

# 生成页面文件
echo "[信息] 正在生成页面文件..."
$PYTHON_CMD generate_pages_files.py "$(pwd)"
if [ $? -ne 0 ]; then
    echo "[错误] 生成页面文件失败"
    exit 1
fi
echo "[成功] 页面文件生成完成"

# 生成自动化文件
echo "[信息] 正在生成自动化文件..."
$PYTHON_CMD generate_automation_files.py "$(pwd)"
if [ $? -ne 0 ]; then
    echo "[错误] 生成自动化文件失败"
    exit 1
fi
echo "[成功] 自动化文件生成完成"

# 生成营销文件
echo "[信息] 正在生成营销文件..."
$PYTHON_CMD generate_marketing_files.py "$(pwd)"
if [ $? -ne 0 ]; then
    echo "[错误] 生成营销文件失败"
    exit 1
fi
echo "[成功] 营销文件生成完成"

# 本地预览（可选）
read -p "是否立即本地预览网站？(Y/N): " preview
if [[ "$preview" =~ ^[Yy]$ ]]; then
    echo "[信息] 正在启动 Hugo 本地服务器..."
    echo "[提示] 请在浏览器中访问 http://localhost:1313"
    echo "[提示] 按 Ctrl+C 停止服务器"
    hugo server -D
fi

echo "================================================"
echo "部署脚本执行完成！"
echo "================================================"
