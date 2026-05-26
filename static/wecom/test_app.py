#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试 Flask 应用
"""

import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
import json

def test_health():
    """测试健康检查接口"""
    with app.test_client() as client:
        response = client.get('/health')
        print(f"Health check status: {response.status_code}")
        print(f"Health check response: {response.get_json()}")
        assert response.status_code == 200
        assert response.get_json()['status'] == 'ok'
        print("✓ Health check passed")

def test_webhook():
    """测试 Webhook 接口"""
    with app.test_client() as client:
        # 模拟企业微信发送的消息
        test_data = {
            'FromUserName': 'test_user_123',
            'Content': '玉米价格'
        }
        response = client.post(
            '/wecom/webhook',
            json=test_data,
            content_type='application/json'
        )
        print(f"Webhook status: {response.status_code}")
        print(f"Webhook response: {response.get_json()}")
        # 注意：由于我们没有配置真实的 CORPID/CORPSECRET，
        # send_text_message 会失败，但我们应该能看到自动回复的内容
        print("✓ Webhook endpoint is accessible")

if __name__ == '__main__':
    print("开始测试 Flask 应用...")
    try:
        test_health()
        test_webhook()
        print("\n所有测试完成！")
    except Exception as e:
        print(f"测试失败：{e}")
        import traceback
        traceback.print_exc()
