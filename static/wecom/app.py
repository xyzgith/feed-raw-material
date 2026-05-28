#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
企业微信自动回复 Web 服务
使用 Flask 提供 Webhook 接口
"""

from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# 企业微信配置（从环境变量读取）
CORPID = os.environ.get('CORPID', '')
CORPSECRET = os.environ.get('CORPSECRET', '')
AGENTID = os.environ.get('AGENTID', '')
TOKEN = os.environ.get('TOKEN', 'your-verify-token')

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
    """自动回复（改进版：更健壮的关键词匹配）"""
    # 清理消息：去除前后空格
    message_clean = message.strip()
    
    # 关键词匹配（使用更健壮的检查）
    if "玉米价格" in message_clean or "玉米" in message_clean:
        reply = "感谢咨询玉米价格！今日玉米（吉林长春）价格：2.45元/斤，库存500吨。如需报价单，请留下您的邮箱或微信号。"
    elif "小麦价格" in message_clean or "小麦" in message_clean:
        reply = "感谢咨询小麦价格！今日小麦（河南郑州）价格：2.38元/斤，库存300吨。如需报价单，请留下您的邮箱或微信号。"
    elif "面粉价格" in message_clean or "面粉" in message_clean:
        reply = "感谢咨询面粉价格！今日面粉（山东济南）价格：2.65元/斤，库存150吨。如需报价单，请留下您的邮箱或微信号。"
    elif "联系方式" in message_clean:
        reply = "我们的联系方式：电话：138-0000-0000，邮箱：your-email@example.com，工作时间：周一至周五 9:00-18:00"
    elif "公司地址" in message_clean:
        reply = "我们公司地址：中国某省某市某区某路123号。欢迎实地考察！"
    elif "人工客服" in message_clean:
        reply = "已为您转接人工客服，请稍等..."
    else:
        reply = "感谢您的留言！我们会尽快回复您。\n如需紧急咨询，请致电：138-0000-0000\n或发送邮件至：your-email@example.com"

    # 发送回复
    send_text_message(userid, reply)
    return reply

@app.route('/wecom/webhook', methods=['GET', 'POST'])
def webhook():
    """接收企业微信消息的 Webhook 接口（支持GET验证和POST接收消息）"""
    # 处理 GET 请求（企业微信 URL 验证）
    if request.method == 'GET':
        # 企业微信验证请求
        echostr = request.args.get('echostr', '')
        
        # 注意：生产环境应验证签名（这里简化）
        # 验证签名需要：token, timestamp, nonce, <SECRET_REMOVED>
        # 详见：https://developer.work.weixin.qq.com/document/path/90930
        
        print(f"收到验证请求，echostr: {echostr}")
        return echostr  # 返回 echostr 完成验证
    
    # 处理 POST 请求（接收消息）
    try:
        data = request.json
        userid = data.get('FromUserName', '')
        message = data.get('Content', '')
        
        print(f"收到消息：userid={userid}, message='{message}' (原始)")
        print(f"消息长度：{len(message)}")
        print(f"消息字节：{message.encode('utf-8', errors='replace').hex()}")
        
        # 自动回复
        reply = auto_reply(userid, message)
        
        return jsonify({
            "errcode": 0,
            "errmsg": "ok",
            "reply": reply
        })
    except Exception as e:
        print(f"处理 Webhook 失败：{e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "errcode": -1,
            "errmsg": str(e)
        })

@app.route('/health', methods=['GET'])
def health():
    """健康检查接口"""
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
