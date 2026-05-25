#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
饲料原料营销系统 - 一键生成所有文件
Task 12.6: 主调度脚本
"""

import os
import sys
import subprocess
from pathlib import Path

# 设置标准输出编码为UTF-8
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer)

def check_dependencies():
    """检查依赖项"""
    print("=" * 60)
    print("步骤 0/6: 检查依赖项")
    print("=" * 60)

    # 检查 Python
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        print(f"[OK] Python: {result.stdout.strip()}")
    except Exception as e:
        print(f"[ERROR] Python 检查失败: {e}")
        return False

    # 检查 Git
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        print(f"[OK] Git: {result.stdout.strip()}")
    except Exception as e:
        print(f"[ERROR] Git 检查失败: {e}")
        print("  请安装 Git: https://git-scm.com/download/")
        return False

    # 检查 Hugo
    try:
        result = subprocess.run(["hugo", "version"], capture_output=True, text=True)
        print(f"[OK] Hugo: {result.stdout.strip()}")
    except Exception as e:
        print(f"[WARNING] Hugo 检查失败: {e}")
        print("  将尝试在部署时自动安装 Hugo")
        print("  或手动安装: https://gohugo.io/install/")

    print("\n依赖项检查完成！\n")
    return True

def create_directory_structure(base_dir):
    """创建目录结构"""
    print("=" * 60)
    print("步骤 1/6: 创建目录结构")
    print("=" * 60)

    directories = [
        "content",
        "static/email",
        "static/wecom",
        "static/crm",
        "static/video",
        "static/sales",
        "n8n-workflows",
        "themes"
    ]

    for dir_path in directories:
        full_path = Path(base_dir) / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"[OK] {full_path}")

    print("\n目录结构创建完成！\n")

def run_script(script_name, base_dir):
    """运行生成脚本"""
    script_path = Path(base_dir) / script_name

    if not script_path.exists():
        print(f"[ERROR] 脚本不存在: {script_path}")
        return False

    try:
        result = subprocess.run(
            [sys.executable, str(script_path), str(base_dir)],
            capture_output=True,
            text=True,
            cwd=base_dir
        )

        if result.returncode == 0:
            print(f"[OK] {script_name} 执行成功")
            # 打印脚本输出（如果有）
            if result.stdout.strip():
                for line in result.stdout.strip().split('\n'):
                    if line.strip():
                        print(f"  {line}")
            return True
        else:
            print(f"[ERROR] {script_name} 执行失败")
            print(f"  错误: {result.stderr}")
            return False
    except Exception as e:
        print(f"[ERROR] {script_name} 执行异常: {e}")
        return False

def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("饲料原料营销系统 - 一键生成所有文件")
    print("=" * 60 + "\n")

    # 获取 base 目录
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = "F:\\feed-raw-material"

    print(f"目标目录: {base_dir}\n")

    # 检查依赖项
    if not check_dependencies():
        print("依赖项检查失败，请安装缺少的软件后重试。")
        sys.exit(1)

    # 创建目录结构
    create_directory_structure(base_dir)

    # 步骤 2/6: 生成核心文件
    print("=" * 60)
    print("步骤 2/6: 生成核心文件")
    print("=" * 60)
    if not run_script("generate_core_files.py", base_dir):
        print("生成核心文件失败，终止执行。")
        sys.exit(1)
    print()

    # 步骤 3/6: 生成页面文件
    print("=" * 60)
    print("步骤 3/6: 生成页面文件")
    print("=" * 60)
    if not run_script("generate_pages_files.py", base_dir):
        print("生成页面文件失败，终止执行。")
        sys.exit(1)
    print()

    # 步骤 4/6: 生成自动化文件
    print("=" * 60)
    print("步骤 4/6: 生成自动化文件")
    print("=" * 60)
    if not run_script("generate_automation_files.py", base_dir):
        print("生成自动化文件失败，终止执行。")
        sys.exit(1)
    print()

    # 步骤 5/6: 生成营销文件
    print("=" * 60)
    print("步骤 5/6: 生成营销文件")
    print("=" * 60)
    if not run_script("generate_marketing_files.py", base_dir):
        print("生成营销文件失败，终止执行。")
        sys.exit(1)
    print()

    # 步骤 6/6: 生成部署脚本
    print("=" * 60)
    print("步骤 6/6: 生成部署脚本")
    print("=" * 60)
    if not run_script("generate_deployment_files.py", base_dir):
        print("生成部署脚本文件失败，终止执行。")
        sys.exit(1)
    print()

    # 完成
    print("=" * 60)
    print("[SUCCESS] 所有文件生成完成！")
    print("=" * 60)

    print("\n下一步：")
    print("1. 检查生成的文件：")
    print(f"   {base_dir}")
    print("\n2. 本地预览网站：")
    print(f"   cd {base_dir}")
    print("   hugo server -D")
    print("   然后访问: http://localhost:1313")
    print("\n3. 部署到 GitHub Pages：")
    print(f"   cd {base_dir}")
    print("   .\\deploy.bat  (Windows)")
    print("   bash deploy.sh  (Linux/Mac)")
    print("\n4. 配置自动化营销：")
    print("   - 导入 n8n 工作流")
    print("   - 配置企业微信机器人")
    print("   - 设置 Bitrix24 CRM")
    print("\n详细说明请查看生成的文件。\n")

if __name__ == "__main__":
    main()
