#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成饲料原料营销系统核心文件
Task 12.1: 生成 Hugo 配置、首页、关于页面
"""

import os
import sys
import json
from pathlib import Path

def create_directories(base_dir):
    """创建必要的目录结构"""
    directories = [
        "content",
        "static/email",
        "static/wecom",
        "static/crm",
        "static/video",
        "static/sales",
        "n8n-workflows"
    ]

    for dir_path in directories:
        full_path = Path(base_dir) / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"[OK] 创建目录: {full_path}")

def generate_hugo_config(base_dir):
    """生成 Hugo 配置文件"""
    content = """# Hugo 配置文件
baseURL = "https://yourusername.github.io/feed-raw-material/"
languageCode = "zh-cn"
title = "优质饲料原料供应商 - 玉米、小麦、面粉"
theme = "ananke"

[params]
  description = "专业供应优质玉米、小麦、面粉等饲料原料，长期稳定供货，价格优惠"
  author = "饲料原料供应商"
  author_email = "your-email@example.com"

[params.header]
  _merge = "shallow"
  navbar_background = "white"
  navbar_dark = false
  navbar_fixed = true

[params.sidebar]
  _merge = "shallow"
  show_toc = true

[markup.tableOfContents]
  startLevel = 2
  endLevel = 3
"""

    temp_file = "C:\\Users\\Administrator\\AppData\\Local\\Temp\\_tw_hugo.toml.txt"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # 调用 write_file.py 写入目标文件
    import subprocess
    script_path = "D:\\qclaw\\resources\\openclaw\\config\\skills\\qclaw-text-file\\scripts\\write_file.py"
    target_path = str(Path(base_dir) / "hugo.toml")

    result = subprocess.run([
        "python", script_path,
        "--path", target_path,
        "--content-file", temp_file
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"[OK] 生成 Hugo 配置文件: {target_path}")
    else:
        print(f"[ERROR] 生成 Hugo 配置文件失败: {result.stderr}")

    # 清理临时文件
    os.remove(temp_file)

def generate_homepage(base_dir):
    """生成首页"""
    content = """---
title: "优质饲料原料供应商 - 玉米、小麦、面粉"
date: 2026-05-25T10:00:00+08:00
draft: false
---

# [Wheat] 专业饲料原料供应商

## 产品优势

### [Corn] 优质玉米
- **产地直供**：来自东北黄金玉米带，品质优良
- **质量保证**：水分≤14%，杂质≤1%，霉变率≤2%
- **稳定供应**：年供应量10万吨以上，长期合作无忧

### [Wheat] 精选小麦
- **高蛋白**：蛋白含量≥13%，适合畜禽生长
- **新鲜度好**：当年新粮，存储条件优良
- **价格优势**：比市场均价低3-5%

### [Rice] 优质面粉
- **精细加工**：专用饲料面粉，细度均匀
- **营养均衡**：添加维生素和矿物质，提高饲料转化率
- **发货快捷**：24小时内发货，全国配送

## 合作优势

[Check] **上市公司供应链**：与上市饲料企业深度合作，货源稳定可靠  
[Check] **价格透明**：每日更新市场价格，公开透明  
[Check] **质量保证**：每批货物附检测报告，支持第三方复检  
[Check] **物流便捷**：合作物流公司，全国主要城市直达  
[Check] **长期合作**：支持月结、季结等灵活结算方式

## 今日推荐

**玉米（2026-05-25）**  
- 产地：吉林长春
- 价格：2.45元/斤
- 库存：500吨
- 备注：新粮上市，品质优良

**小麦（2026-05-25）**  
- 产地：河南郑州
- 价格：2.38元/斤
- 库存：300吨
- 备注：高蛋白小麦，适合猪饲料

## 联系我们

[Phone] **联系电话**：138-0000-0000  
[Email] **电子邮箱**：your-email@example.com  
[Time] **工作时间**：周一至周五 9:00-18:00

---

## 免费获取报价

填写下方表单，免费获取今日最优报价单！

<form name="contact" method="POST" data-netlify="true">
  <p>
    <label>姓名: <input type="text" name="name" required /></label>
  </p>
  <p>
    <label>电话: <input type="tel" name="phone" required /></label>
  </p>
  <p>
    <label>需求产品:
      <select name="product">
        <option value="玉米">玉米</option>
        <option value="小麦">小麦</option>
        <option value="面粉">面粉</option>
        <option value="其他">其他</option>
      </select>
    </label>
  </p>
  <p>
    <label>月需求量(吨): <input type="number" name="quantity" /></label>
  </p>
  <p>
    <button type="submit">获取报价</button>
  </p>
</form>
"""

    temp_file = "C:\\Users\\Administrator\\AppData\\Local\\Temp\\_tw_index.md.txt"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # 调用 write_file.py 写入目标文件
    import subprocess
    script_path = "D:\\qclaw\\resources\\openclaw\\config\\skills\\qclaw-text-file\\scripts\\write_file.py"
    target_path = str(Path(base_dir) / "content" / "_index.md")

    result = subprocess.run([
        "python", script_path,
        "--path", target_path,
        "--content-file", temp_file
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"[OK] 生成首页: {target_path}")
    else:
        print(f"[ERROR] 生成首页失败: {result.stderr}")

    # 清理临时文件
    os.remove(temp_file)

def generate_about_page(base_dir):
    """生成关于我们页面"""
    content = """---
title: "关于我们 - 优质饲料原料供应商"
date: 2026-05-25T10:00:00+08:00
draft: false
---

# 关于我们

## 公司简介

我们是一家专业的饲料原料供应商，致力于为饲料加工企业提供优质、稳定的玉米、小麦、面粉等原料。公司与多家上市饲料企业建立长期合作关系，凭借优质的货源和专业的服务，赢得了广大客户的信赖。

## 核心优势

### [Factory] 优质货源
- 与东北、华北等主要产区建立直采合作
- 严格质量控制体系，每批货物附检测报告
- 年供应量超过10万吨，保障长期稳定供货

### [Money] 价格优势
- 厂家直供，减少中间环节
- 每日更新市场价格，公开透明
- 大客户享受专属优惠价格

### [Truck] 物流保障
- 合作多家专业物流企业
- 全国主要城市直达配送
- 24小时内发货，及时送达

### [Handshake] 诚信经营
- 与上市饲料企业深度合作
- 支持月结、季结等灵活结算方式
- 客户满意度98%以上

## 合作流程

1. **咨询沟通**：客户通过网站、电话或微信联系我们
2. **需求确认**：了解客户具体需求（产品、数量、交货地点等）
3. **报价确认**：根据当日市场价格提供最优报价
4. **合同签订**：签订正式购销合同
5. **安排发货**：按合同约定时间安排发货
6. **售后服务**：跟踪货物送达情况，处理售后问题

## 联系方式

[Phone] **联系电话**：138-0000-0000  
[Email] **电子邮箱**：your-email@example.com  
[Location] **公司地址**：中国某省某市某区某路123号  
[Time] **工作时间**：周一至周五 9:00-18:00

## 客户见证

> "与该公司合作三年，货源稳定，质量可靠，价格公道，是值得信赖的合作伙伴。"  
> —— 某大型饲料企业采购经理

> "售后服务很好，出现问题能及时解决，合作很愉快。"  
> —— 某养殖企业负责人

---

## 立即咨询

如果您有任何疑问或需求，请随时联系我们！我们将竭诚为您服务。
"""

    temp_file = "C:\\Users\\Administrator\\AppData\\Local\\Temp\\_tw_about.md.txt"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # 调用 write_file.py 写入目标文件
    import subprocess
    script_path = "D:\\qclaw\\resources\\openclaw\\config\\skills\\qclaw-text-file\\scripts\\write_file.py"
    target_path = str(Path(base_dir) / "content" / "about.md")

    result = subprocess.run([
        "python", script_path,
        "--path", target_path,
        "--content-file", temp_file
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"[OK] 生成关于我们页面: {target_path}")
    else:
        print(f"[ERROR] 生成关于我们页面失败: {result.stderr}")

    # 清理临时文件
    os.remove(temp_file)

def main():
    """主函数"""
    print("=" * 60)
    print("开始生成饲料原料营销系统核心文件")
    print("=" * 60)

    # 获取 base 目录
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = "F:\\feed-raw-material"

    print(f"\n目标目录: {base_dir}\n")

    # 创建目录结构
    print("步骤 1/4: 创建目录结构")
    create_directories(base_dir)

    # 生成 Hugo 配置
    print("\n步骤 2/4: 生成 Hugo 配置文件")
    generate_hugo_config(base_dir)

    # 生成首页
    print("\n步骤 3/4: 生成首页")
    generate_homepage(base_dir)

    # 生成关于我们页面
    print("\n步骤 4/4: 生成关于我们页面")
    generate_about_page(base_dir)

    print("\n" + "=" * 60)
    print("核心文件生成完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
