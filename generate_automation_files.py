#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成饲料原料营销系统自动化文件
Task 12.3: 生成 n8n 工作流、EDM模板、企业微信配置
"""

import os
import sys
import json
from pathlib import Path

def generate_n8n_workflow(base_dir):
    """生成 n8n 工作流配置文件"""
    print("[INFO] 生成 n8n 工作流配置...")
    
    # Webhook 接收工作流
    webhook_workflow = {
        "name": "企业微信消息接收",
        "nodes": [
            {
                "parameters": {
                    "httpMethod": "POST",
                    "path": "wecom-receive",
                    "options": {}
                },
                "id": "webhook-receive",
                "name": "Webhook - 接收企业微信消息",
                "type": "n8n-nodes-base.webhook",
                "typeVersion": 1,
                "position": [250, 300]
            },
            {
                "parameters": {
                    "jsCode": """// 提取用户ID和消息内容
const userId = $input.first().json.FromUserName;
const message = $input.first().json.Content;

return [
  {
    json: {
      userId: userId,
      message: message
    }
  }
];"""
                },
                "id": "extract-msg",
                "name": "提取消息内容",
                "type": "n8n-nodes-base.code",
                "typeVersion": 1,
                "position": [450, 300]
            },
            {
                "parameters": {
                    "jsCode": """// 关键词匹配自动回复
const message = $input.first().json.message;
const userId = $input.first().json.userId;

let reply = "";

if (message.includes("玉米价格")) {
  reply = "感谢咨询玉米价格！今日玉米（吉林长春）价格：2.45元/斤，库存500吨。如需报价单，请留下您的邮箱或微信号。";
} else if (message.includes("小麦价格")) {
  reply = "感谢咨询小麦价格！今日小麦（河南郑州）价格：2.38元/斤，库存300吨。如需报价单，请留下您的邮箱或微信号。";
} else if (message.includes("面粉价格")) {
  reply = "感谢咨询面粉价格！今日面粉（山东济南）价格：2.65元/斤，库存150吨。如需报价单，请留下您的邮箱或微信号。";
} else if (message.includes("联系方式")) {
  reply = "我们的联系方式：电话：138-0000-0000，邮箱：your-email@example.com，工作时间：周一至周五 9:00-18:00";
} else if (message.includes("公司地址")) {
  reply = "我们公司地址：中国某省某市某区某路123号。欢迎实地考察！";
} else if (message.includes("人工客服")) {
  reply = "已为您转接人工客服，请稍等...";
} else {
  reply = "感谢您的留言！我们会尽快回复您。\\n如需紧急咨询，请致电：138-0000-0000\\n或发送邮件至：your-email@example.com";
}

return [
  {
    json: {
      userId: userId,
      reply: reply
    }
  }
];"""
                },
                "id": "auto-reply",
                "name": "自动回复匹配",
                "type": "n8n-nodes-base.code",
                "typeVersion": 1,
                "position": [650, 300]
            },
            {
                "parameters": {
                    "method": "POST",
                    "url": "=https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={{$env.WECOM_ACCESS_TOKEN}}",
                    "jsonParameters": True,
                    "specifyBody": "json",
                    "bodyParametersJson": """={
  "touser": "={{$json.userId}}",
  "msgtype": "text",
  "agentid": {{$env.WECOM_AGENT_ID}},
  "text": {
    "content": "={{$json.reply}}"
  }
}"""
                },
                "id": "send-reply",
                "name": "发送回复消息",
                "type": "n8n-nodes-base.httpRequest",
                "typeVersion": 1,
                "position": [850, 300]
            }
        ],
        "connections": {
            "Webhook - 接收企业微信消息": {
                "main": [
                    [
                        {
                            "node": "提取消息内容",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            },
            "提取消息内容": {
                "main": [
                    [
                        {
                            "node": "自动回复匹配",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            },
            "自动回复匹配": {
                "main": [
                    [
                        {
                            "node": "发送回复消息",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            }
        }
    }
    
    # 写入文件
    target_path = Path(base_dir) / "n8n-workflows" / "wecom-auto-reply.json"
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(webhook_workflow, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] 生成 n8n 工作流: {target_path}")

def generate_edm_template(base_dir):
    """生成 EDM 邮件模板"""
    print("[INFO] 生成 EDM 邮件模板...")
    
    # EDM模板1：首次咨询回复
    edm_welcome = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>感谢咨询饲料原料</title>
</head>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px;">
        <h2 style="color: #333;">感谢咨询我们的饲料原料！</h2>
        
        <p>尊敬的客户，</p>
        
        <p>感谢您通过网站/企业微信咨询我们的饲料原料。我们是专业的饲料原料供应商，致力于为饲料加工企业提供优质、稳定的玉米、小麦、面粉等原料。</p>
        
        <h3 style="color: #555;">我们的优势：</h3>
        <ul>
            <li>✅ <strong>上市公司供应链</strong>：与上市饲料企业深度合作，货源稳定可靠</li>
            <li>✅ <strong>价格透明</strong>：每日更新市场价格，公开透明</li>
            <li>✅ <strong>质量保证</strong>：每批货物附检测报告，支持第三方复检</li>
            <li>✅ <strong>物流便捷</strong>：合作物流公司，全国主要城市直达</li>
        </ul>
        
        <h3 style="color: #555;">今日推荐（2026-05-25）：</h3>
        <table style="width: 100%; border-collapse: collapse;">
            <tr style="background-color: #e9ecef;">
                <th style="padding: 10px; border: 1px solid #dee2e6;">产品</th>
                <th style="padding: 10px; border: 1px solid #dee2e6;">产地</th>
                <th style="padding: 10px; border: 1px solid #dee2e6;">价格</th>
                <th style="padding: 10px; border: 1px solid #dee2e6;">库存</th>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #dee2e6;">玉米</td>
                <td style="padding: 10px; border: 1px solid #dee2e6;">吉林长春</td>
                <td style="padding: 10px; border: 1px solid #dee2e6;">2.45元/斤</td>
                <td style="padding: 10px; border: 1px solid #dee2e6;">500吨</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #dee2e6;">小麦</td>
                <td style="padding: 10px; border: 1px solid #dee2e6;">河南郑州</td>
                <td style="padding: 10px; border: 1px solid #dee2e6;">2.38元/斤</td>
                <td style="padding: 10px; border: 1px solid #dee2e6;">300吨</td>
            </tr>
        </table>
        
        <p style="margin-top: 20px;">如果您需要详细的报价单或样品，请回复此邮件或致电：138-0000-0000</p>
        
        <p>此致<br>饲料原料供应商团队</p>
        
        <hr style="margin-top: 30px;">
        <p style="font-size: 12px; color: #777;">本邮件为自动发送，请勿直接回复。如有疑问，请联系我们的客服团队。</p>
    </div>
</body>
</html>"""
    
    # 写入文件
    target_path = Path(base_dir) / "static" / "email" / "welcome.html"
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(edm_welcome)
    
    print(f"[OK] 生成 EDM 模板: {target_path}")

def generate_wecom_script(base_dir):
    """生成企业微信自动回复脚本"""
    print("[INFO] 生成企业微信自动回复脚本...")
    
    wecom_script = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
企业微信自动回复脚本
"""

import requests
import json

# 企业微信配置
CORPID = "YOUR_CORPID"
CORPSECRET = "YOUR_CORPSECRET"
AGENTID = "YOUR_AGENTID"

def get_access_token():
    """获取 access_token"""
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORPID}&corpsecret={CORPSECRET}"
    response = requests.get(url)
    data = response.json()
    if data["errcode"] == 0:
        return data["access_token"]
    else:
        print(f"获取 access_token 失败：{data}")
        return None

def send_text_message(userid, content):
    """发送文本消息"""
    access_token = get_access_token()
    if not access_token:
        return False

    url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
    data = {
        "touser": userid,
        "msgtype": "text",
        "agentid": AGENTID,
        "text": {
            "content": content
        }
    }

    response = requests.post(url, json=data)
    result = response.json()
    if result["errcode"] == 0:
        print(f"消息发送成功：{userid}")
        return True
    else:
        print(f"消息发送失败：{result}")
        return False

def auto_reply(userid, message):
    """自动回复"""
    # 关键词匹配
    if "玉米价格" in message:
        reply = "感谢咨询玉米价格！今日玉米（吉林长春）价格：2.45元/斤，库存500吨。如需报价单，请留下您的邮箱或微信号。"
    elif "小麦价格" in message:
        reply = "感谢咨询小麦价格！今日小麦（河南郑州）价格：2.38元/斤，库存300吨。如需报价单，请留下您的邮箱或微信号。"
    elif "面粉价格" in message:
        reply = "感谢咨询面粉价格！今日面粉（山东济南）价格：2.65元/斤，库存150吨。如需报价单，请留下您的邮箱或微信号。"
    elif "联系方式" in message:
        reply = "我们的联系方式：电话：138-0000-0000，邮箱：your-email@example.com，工作时间：周一至周五 9:00-18:00"
    elif "公司地址" in message:
        reply = "我们公司地址：中国某省某市某区某路123号。欢迎实地考察！"
    elif "人工客服" in message:
        reply = "已为您转接人工客服，请稍等..."
    else:
        reply = "感谢您的留言！我们会尽快回复您。\\n如需紧急咨询，请致电：138-0000-0000\\n或发送邮件至：your-email@example.com"

    # 发送回复
    send_text_message(userid, reply)

if __name__ == "__main__":
    # 示例：自动回复
    auto_reply("USERID", "玉米价格")
'''
    
    # 写入文件
    target_path = Path(base_dir) / "static" / "wecom" / "auto_reply.py"
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(wecom_script)
    
    print(f"[OK] 生成企业微信脚本: {target_path}")

def main():
    """主函数"""
    print("=" * 60)
    print("开始生成饲料原料营销系统自动化文件")
    print("=" * 60)

    # 获取 base 目录
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = "F:\\feed-raw-material"

    print(f"\\n目标目录: {base_dir}\\n")

    # 生成 n8n 工作流
    print("步骤 1/3: 生成 n8n 工作流")
    generate_n8n_workflow(base_dir)
    print()

    # 生成 EDM 模板
    print("步骤 2/3: 生成 EDM 邮件模板")
    generate_edm_template(base_dir)
    print()

    # 生成企业微信脚本
    print("步骤 3/3: 生成企业微信自动回复脚本")
    generate_wecom_script(base_dir)
    print()

    print("=" * 60)
    print("[SUCCESS] 自动化文件生成完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
