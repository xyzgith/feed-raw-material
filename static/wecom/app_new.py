#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""饲料原料企业微信自动回复Flask应用（简化版）"""
import os, json
from flask import Flask, request, jsonify

app = Flask(__name__)

CORPID = os.getenv("CORPID", "your_corpid")
CORPSECRET = os.getenv("CORPSECRET", "your_corpsecret")
AGENTID = os.getenv("AGENTID", "1000002")
TOKEN = os.getenv("TOKEN", "your_token_here")

def get_access_token():
    return None

def send_text_message(userid, content):
    return True

def auto_reply(userid, message):
    if not message:
        return "您好！感谢联系我们。"
    msg = message.strip()
    if "玉米" in msg:
        return "玉米价格：今日玉米（吉林长春）2.45元/斤，库存500吨。"
    if "小麦" in msg:
        return "小麦价格：今日小麦（河南郑州）2.38元/斤，库存300吨。"
    if "面粉" in msg:
        return "面粉价格：今日面粉（山东济南）2.65元/斤，库存150吨。"
    if "联系" in msg or "电话" in msg or "邮箱" in msg:
        return "联系方式：电话138-0000-0000，邮箱info@example.com"
    if "地址" in msg or "位置" in msg:
        return "公司地址：某省某市某区某路123号。"
    if "人工" in msg or "客服" in msg:
        return "已为您转接人工客服，请稍等..."
    return "感谢您的留言！我们会尽快回复您。"

@app.route("/wecom/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return request.args.get("echostr", "")
    try:
        data = request.get_json(force=True, silent=True)
        if not data:
            return jsonify({"errcode": -1, "errmsg": "invalid json"})
        userid = data.get("FromUserName", "")
        message = data.get("Content", "")
        reply = auto_reply(userid, message)
        return jsonify({"errcode": 0, "errmsg": "ok", "reply": reply})
    except Exception as e:
        return jsonify({"errcode": -1, "errmsg": str(e)})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
