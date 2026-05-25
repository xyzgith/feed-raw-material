#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成饲料原料营销系统部署脚本
Task 12.5: 生成部署脚本（deploy.bat、deploy.sh）
"""

import os
import sys
from pathlib import Path

def generate_windows_deploy_script(base_dir):
    """生成 Windows 部署脚本（deploy.bat）"""
    content = """@echo off
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
if not exist "themes\\ananke" (
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
"""

    temp_file = "C:\\Users\\Administrator\\AppData\\Local\\Temp\\_tw_deploy.bat.txt"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # 调用 write_file.py 写入目标文件
    import subprocess
    script_path = "D:\\qclaw\\resources\\openclaw\\config\\skills\\qclaw-text-file\\scripts\\write_file.py"
    target_path = str(Path(base_dir) / "deploy.bat")

    result = subprocess.run([
        "python", script_path,
        "--path", target_path,
        "--content-file", temp_file
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"[OK] 生成 Windows 部署脚本: {target_path}")
    else:
        print(f"[ERROR] 生成 Windows 部署脚本失败: {result.stderr}")

    # 清理临时文件
    os.remove(temp_file)

def generate_linux_mac_deploy_script(base_dir):
    """生成 Linux/Mac 部署脚本（deploy.sh）"""
    content = """#!/bin/bash

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
"""

    temp_file = "C:\\Users\\Administrator\\AppData\\Local\\Temp\\_tw_deploy.sh.txt"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # 调用 write_file.py 写入目标文件
    import subprocess
    script_path = "D:\\qclaw\\resources\\openclaw\\config\\skills\\qclaw-text-file\\scripts\\write_file.py"
    target_path = str(Path(base_dir) / "deploy.sh")

    result = subprocess.run([
        "python", script_path,
        "--path", target_path,
        "--content-file", temp_file
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"[OK] 生成 Linux/Mac 部署脚本: {target_path}")
        # 添加执行权限（Linux/Mac）
        if os.name != 'nt':  # 不是 Windows
            os.chmod(target_path, 0o755)
            print(f"[OK] 已添加执行权限: {target_path}")
    else:
        print(f"[ERROR] 生成 Linux/Mac 部署脚本失败: {result.stderr}")

    # 清理临时文件
    os.remove(temp_file)

def main():
    """主函数"""
    print("=" * 60)
    print("开始生成饲料原料营销系统部署脚本")
    print("=" * 60)

    # 获取 base 目录
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = "F:\\feed-raw-material"

    print(f"\n目标目录: {base_dir}\n")

    # 生成 Windows 部署脚本
    print("步骤 1/2: 生成 Windows 部署脚本")
    generate_windows_deploy_script(base_dir)

    # 生成 Linux/Mac 部署脚本
    print("\n步骤 2/2: 生成 Linux/Mac 部署脚本")
    generate_linux_mac_deploy_script(base_dir)

    print("\n" + "=" * 60)
    print("部署脚本生成完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
