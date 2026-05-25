#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复所有生成脚本的Unicode编码问题
全自动执行版本 - 无需人工干预
"""

import sys
import os
import subprocess
from pathlib import Path

# Unicode字符映射表
REPLACEMENTS = {
    '✓': '[OK]',
    '✗': '[ERROR]',
    '⚠': '[WARNING]',
    '🎉': '[SUCCESS]',
    '🌾': '[Wheat]',
    '🌽': '[Corn]',
    '🍚': '[Rice]',
    '✅': '[Check]',
    '📞': '[Phone]',
    '📧': '[Email]',
    '🕐': '[Time]',
    '📍': '[Location]',
    '🏭': '[Factory]',
    '💰': '[Money]',
    '🚚': '[Truck]',
    '🤝': '[Handshake]',
}

def fix_file(file_path):
    """修复单个文件的Unicode字符"""
    print(f"修复: {file_path}")
    
    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换Unicode字符
    for old, new in REPLACEMENTS.items():
        content = content.replace(old, new)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  [OK] 完成: {file_path}")
    return True

def main():
    """主函数 - 全自动执行"""
    base_dir = Path("F:\\feed-raw-material")
    
    # 需要修复的脚本列表
    scripts = [
        "generate_all.py",
        "generate_core_files.py",
        "generate_pages_files.py",
        "generate_automation_files.py",
        "generate_marketing_files.py",
        "generate_deployment_files.py"
    ]
    
    print("=" * 60)
    print("开始修复脚本Unicode编码问题...")
    print("=" * 60)
    print()
    
    # 修复所有脚本
    success_count = 0
    for script in scripts:
        script_path = base_dir / script
        if script_path.exists():
            if fix_file(script_path):
                success_count += 1
        else:
            print(f"[ERROR] 文件不存在: {script_path}")
    
    print()
    print("=" * 60)
    print(f"[SUCCESS] 修复完成！成功修复 {success_count}/{len(scripts)} 个脚本")
    print("=" * 60)
    print()
    print("提示: 现在可以执行 python generate_all.py 来生成所有文件")
    print()

if __name__ == "__main__":
    main()
