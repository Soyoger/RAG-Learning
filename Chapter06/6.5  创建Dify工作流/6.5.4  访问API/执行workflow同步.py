#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/12/8 19:51
# @Author  : yongjie.su
# @File    : 执行workflow同步.py
# @Software: PyCharm
import requests

api_key = "app-0fzG2CmvwHSYyetO7rQDZ66J"
url = 'http://43.130.48.238/v1/workflows/run'
question = "Java的浮点数类型怎么用更好"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
body = {
    "inputs": {"query": question},
    "user": "abc-123"
}

response = requests.post(url, json=body, headers=headers).json()
text = response.get('data', {}).get('outputs', {}).get('text')
print(f"问题：{question}, 答案：{''.join(text)}")