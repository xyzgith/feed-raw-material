#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成饲料原料营销系统页面文件
Task 12.2: 生成产品页、价格页、联系页
"""

import os
import sys
from pathlib import Path

def generate_products_page(base_dir):
    """生成产品中心页面"""
    content = """---
title: "产品中心 - 优质饲料原料供应商"
date: 2026-05-25T10:00:00+08:00
draft: false
---

# 产品中心

## [Corn] 优质玉米

### 产品规格
- **产地**：吉林长春、黑龙江哈尔滨、辽宁沈阳
- **水分**：≤14%
- **杂质**：≤1%
- **霉变率**：≤2%
- **破碎率**：≤5%
- **容重**：≥720g/L

### 产品特点
[Check] **黄金玉米带**：来自东北黄金玉米带，日照充足，品质优良  
[Check] **严格筛选**：先进筛选设备，去除杂质和霉变粒  
[Check] **新鲜度好**：当年新粮，存储条件优良  
[Check] **稳定供应**：年供应量10万吨以上

### 适用对象
- 饲料加工厂
- 养殖企业（猪、鸡、牛、羊）
- 粮食贸易商

### 包装与运输
- **包装**：散装、50kg/袋、1000kg/吨袋
- **运输**：汽运、火车、船运
- **交货地**：工厂仓库、港口、客户指定地点

---

## [Wheat] 精选小麦

### 产品规格
- **产地**：河南郑州、山东济南、河北石家庄
- **蛋白含量**：≥13%
- **水分**：≤12.5%
- **杂质**：≤1%
- **不完善粒**：≤6%

### 产品特点
[Check] **高蛋白**：蛋白含量≥13%，适合畜禽生长  
[Check] **新鲜度好**：当年新粮，存储条件优良  
[Check] **价格优势**：比市场均价低3-5%  
[Check] **质量检测**：每批货物附检测报告

### 适用对象
- 饲料加工厂
- 面粉加工厂
- 养殖企业

### 包装与运输
- **包装**：散装、25kg/袋、50kg/袋
- **运输**：汽运、火车
- **交货地**：工厂仓库、火车站、客户指定地点

---

## [Rice] 优质面粉

### 产品规格
- **类型**：饲料专用面粉
- **细度**：≥80目
- **蛋白含量**：≥12%
- **水分**：≤14%
- **灰分**：≤0.8%

### 产品特点
[Check] **精细加工**：专用饲料面粉，细度均匀  
[Check] **营养均衡**：添加维生素和矿物质，提高饲料转化率  
[Check] **发货快捷**：24小时内发货，全国配送  
[Check] **定制服务**：可根据客户需求定制配方

### 适用对象
- 饲料加工厂
- 养殖企业
- 宠物食品厂

### 包装与运输
- **包装**：25kg/袋、50kg/袋
- **运输**：汽运
- **交货地**：工厂仓库、物流园区

---

## 订购流程

1. **咨询产品信息**：电话/微信/网站联系我们
2. **确认产品规格**：选择产品类型、规格、数量
3. **确认价格**：根据当日市场价格确定成交价格
4. **签订合同**：签订正式购销合同
5. **安排发货**：按合同约定时间安排发货
6. **验收货物**：客户验收货物，确认质量
7. **结算付款**：按合同约定方式结算付款

## 联系方式

[Phone] **联系电话**：138-0000-0000  
[Email] **电子邮箱**：your-email@example.com
"""

    temp_file = "C:\\Users\\Administrator\\AppData\\Local\\Temp\\_tw_products.md.txt"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # 调用 write_file.py 写入目标文件
    import subprocess
    script_path = "D:\\qclaw\\resources\\openclaw\\config\\skills\\qclaw-text-file\\scripts\\write_file.py"
    target_path = str(Path(base_dir) / "content" / "products.md")

    result = subprocess.run([
        "python", script_path,
        "--path", target_path,
        "--content-file", temp_file
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"[OK] 生成产品中心页面: {target_path}")
    else:
        print(f"[ERROR] 生成产品中心页面失败: {result.stderr}")

    # 清理临时文件
    os.remove(temp_file)

def generate_price_page(base_dir):
    """生成价格中心页面"""
    content = """---
title: "价格中心 - 优质饲料原料供应商"
date: 2026-05-25T10:00:00+08:00
draft: false
---

# 价格中心

## 今日价格（2026-05-25）

| 产品 | 产地 | 价格（元/斤） | 库存（吨） | 涨跌 |
|------|------|---------------|------------|------|
| 玉米 | 吉林长春 | 2.45 | 500 | ↑ 0.02 |
| 玉米 | 黑龙江哈尔滨 | 2.43 | 300 | → 0.00 |
| 玉米 | 辽宁沈阳 | 2.46 | 200 | ↑ 0.01 |
| 小麦 | 河南郑州 | 2.38 | 300 | ↓ 0.01 |
| 小麦 | 山东济南 | 2.40 | 250 | → 0.00 |
| 小麦 | 河北石家庄 | 2.39 | 200 | ↑ 0.01 |
| 面粉 | 山东济南 | 2.65 | 150 | → 0.00 |
| 面粉 | 河南郑州 | 2.63 | 100 | ↓ 0.02 |

> 📌 **价格说明**：以上价格为出厂价，不含运费。实际成交价格根据采购量、交货地点、结算方式等因素可协商优惠。

## 价格走势分析

### 玉米价格走势（近30天）

- **最高价**：2.48元/斤（2026-05-20）
- **最低价**：2.42元/斤（2026-05-10）
- **平均价**：2.45元/斤
- **走势**：震荡上行，受产区天气影响，预计短期内价格维持高位

### 小麦价格走势（近30天）

- **最高价**：2.42元/斤（2026-05-18）
- **最低价**：2.36元/斤（2026-05-08）
- **平均价**：2.39元/斤
- **走势**：稳中偏弱，新麦即将上市，预计价格有一定下行压力

### 面粉价格走势（近30天）

- **最高价**：2.68元/斤（2026-05-15）
- **最低价**：2.62元/斤（2026-05-05）
- **平均价**：2.65元/斤
- **走势**：相对稳定，受小麦价格影响，预计随小麦价格波动

## 采购建议

### [Corn] 玉米采购建议
**建议采购时机**：近期价格震荡上行，建议适量采购，锁定成本。  
**推荐产地**：吉林长春（品质稳定）、黑龙江哈尔滨（价格优势）。  
**采购量建议**：月需求量100吨以下建议一次性采购；100吨以上可分批采购。

### [Wheat] 小麦采购建议
**建议采购时机**：新麦即将上市，价格有一定下行压力，建议观望为主，适量采购。  
**推荐产地**：河南郑州（品质优良）、河北石家庄（价格优势）。  
**采购量建议**：建议采购1-2个月用量，等待新麦上市后再补库。

### [Rice] 面粉采购建议
**建议采购时机**：价格相对稳定，可根据实际需求采购。  
**推荐产地**：山东济南（品质优良）、河南郑州（价格优势）。  
**采购量建议**：建议采购1个月用量，避免库存过多影响新鲜度。

## 价格对比（与市场均价）

| 产品 | 我们的价格 | 市场均价 | 差价 | 节省比例 |
|------|------------|----------|------|----------|
| 玉米（吉林） | 2.45 | 2.52 | -0.07 | 2.8% |
| 小麦（河南） | 2.38 | 2.45 | -0.07 | 2.9% |
| 面粉（山东） | 2.65 | 2.72 | -0.07 | 2.6% |

> [Money] **成本节省**：以月采购量100吨计算，使用我们的产品每月可节省成本约14000元。

## 价格更新

我们每日更新价格，确保您获取最新的市场信息。

[Phone] **获取最新报价**：请致电 138-0000-0000 或发送邮件至 your-email@example.com

---

## 价格说明

1. **价格有效性**：当日价格当日有效，次日价格以最新公布为准。
2. **价格构成**：以上价格为出厂价，不含运费、税费等其他费用。
3. **价格优惠**：大客户（月采购量≥500吨）享受专属优惠价格，具体请咨询业务员。
4. **价格调整**：遇市场剧烈波动，价格可能随时调整，请以当日电话咨询为准。

## 联系方式

[Phone] **联系电话**：138-0000-0000  
[Email] **电子邮箱**：your-email@example.com  
[Time] **工作时间**：周一至周五 9:00-18:00
"""

    temp_file = "C:\\Users\\Administrator\\AppData\\Local\\Temp\\_tw_price.md.txt"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # 调用 write_file.py 写入目标文件
    import subprocess
    script_path = "D:\\qclaw\\resources\\openclaw\\config\\skills\\qclaw-text-file\\scripts\\write_file.py"
    target_path = str(Path(base_dir) / "content" / "price.md")

    result = subprocess.run([
        "python", script_path,
        "--path", target_path,
        "--content-file", temp_file
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"[OK] 生成价格中心页面: {target_path}")
    else:
        print(f"[ERROR] 生成价格中心页面失败: {result.stderr}")

    # 清理临时文件
    os.remove(temp_file)

def generate_contact_page(base_dir):
    """生成联系我们页面"""
    content = """---
title: "联系我们 - 优质饲料原料供应商"
date: 2026-05-25T10:00:00+08:00
draft: false
---

# 联系我们

## 联系方式

[Phone] **联系电话**：138-0000-0000  
[Email] **电子邮箱**：your-email@example.com  
[Location] **公司地址**：中国某省某市某区某路123号  
[Time] **工作时间**：周一至周五 9:00-18:00

## 在线留言

如果您有任何疑问或需求，请填写下方表单，我们会尽快与您联系！

<form name="contact" method="POST" data-netlify="true">
  <p>
    <label>姓名: <input type="text" name="name" required /></label>
  </p>
  <p>
    <label>电话: <input type="tel" name="phone" required /></label>
  </p>
  <p>
    <label>电子邮箱: <input type="email" name="email" /></label>
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
    <label>留言内容: <textarea name="message" rows="5" cols="50"></textarea></label>
  </p>
  <p>
    <button type="submit">提交留言</button>
  </p>
</form>

## 常见问题

### Q1:  minimum order quantity (MOQ) 是多少？
A: 玉米和小麦的 MOQ 为 30 吨，面粉的 MOQ 为 5 吨。具体可根据客户需求协商。

### Q2: 可以送货上门吗？
A: 可以。我们根据客户位置和订单量安排物流，全国主要城市均可送达。

### Q3: 如何保证产品质量？
A: 每批货物都附有权威检测机构的检测报告。我们也支持客户指定第三方检测机构进行复检。

### Q4: 付款方式有哪些？
A: 我们支持多种付款方式：预付、货到付款、月结、季结等。长期合作客户可享受更灵活的结算方式。

### Q5: 价格会变动吗？
A: 我们的价格根据市场行情每日更新。长期合作客户可享受价格保护政策，具体请咨询业务员。

### Q6: 可以提供样品吗？
A: 可以。我们提供免费样品（运费自理），样品重量一般为 1-5kg。

### Q7: 运输过程中出现问题怎么办？
A: 我们为每批货物购买运输保险。如在运输过程中出现问题，我们会协助客户向物流公司和保险公司索赔。

### Q8: 可以定制产品规格吗？
A: 可以。我们根据客户需求定制产品规格（如蛋白含量、水分、杂质等），具体请咨询业务员。

## 业务范围

我们的业务覆盖全国主要省市，包括但不限于：

- **华北地区**：北京、天津、河北、山西、内蒙古
- **东北地区**：辽宁、吉林、黑龙江
- **华东地区**：上海、江苏、浙江、安徽、福建、江西、山东
- **中南地区**：河南、湖北、湖南、广东、广西、海南
- **西南地区**：重庆、四川、贵州、云南、西藏
- **西北地区**：陕西、甘肃、青海、宁夏、新疆

## 合作客户

我们已与多家知名饲料企业建立长期合作关系，包括但不限于：

- 某上市饲料企业（年采购量 5 万吨）
- 某大型养殖企业（年采购量 3 万吨）
- 某粮食贸易商（年采购量 2 万吨）

## 立即咨询

如果您有任何疑问或需求，请随时联系我们！我们将竭诚为您服务。

[Phone] **联系电话**：138-0000-0000  
[Email] **电子邮箱**：your-email@example.com  
[Time] **工作时间**：周一至周五 9:00-18:00
"""

    temp_file = "C:\\Users\\Administrator\\AppData\\Local\\Temp\\_tw_contact.md.txt"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # 调用 write_file.py 写入目标文件
    import subprocess
    script_path = "D:\\qclaw\\resources\\openclaw\\config\\skills\\qclaw-text-file\\scripts\\write_file.py"
    target_path = str(Path(base_dir) / "content" / "contact.md")

    result = subprocess.run([
        "python", script_path,
        "--path", target_path,
        "--content-file", temp_file
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"[OK] 生成联系我们页面: {target_path}")
    else:
        print(f"[ERROR] 生成联系我们页面失败: {result.stderr}")

    # 清理临时文件
    os.remove(temp_file)

def main():
    """主函数"""
    print("=" * 60)
    print("开始生成饲料原料营销系统页面文件")
    print("=" * 60)

    # 获取 base 目录
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = "F:\\feed-raw-material"

    print(f"\n目标目录: {base_dir}\n")

    # 生成产品中心页面
    print("步骤 1/3: 生成产品中心页面")
    generate_products_page(base_dir)

    # 生成价格中心页面
    print("\n步骤 2/3: 生成价格中心页面")
    generate_price_page(base_dir)

    # 生成联系我们页面
    print("\n步骤 3/3: 生成联系我们页面")
    generate_contact_page(base_dir)

    print("\n" + "=" * 60)
    print("页面文件生成完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
