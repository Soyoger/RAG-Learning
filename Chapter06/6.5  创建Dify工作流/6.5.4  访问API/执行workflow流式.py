#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/12/8 19:51
# @Author  : yongjie.su
# @File    : 执行workflow同步.py
# @Software: PyCharm
import json
import requests

api_key = "app-0fzG2CmvwHSYyetO7rQDZ66J"
url = 'http://43.130.48.238/v1/workflows/run'
question = "帮我介绍一下Dify中的工作流"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
body = {
    "inputs": {"query": question},
    "response_mode": "streaming",
    "user": "abc-123"
}

response = requests.post(url, headers=headers, json=body, stream=True)
for chunk in response.iter_content(chunk_size=512):
    if not chunk:
        continue
    chunk = str(chunk, encoding='utf-8')
    if 'data:' in chunk:
        chunk = chunk.replace('data: ', '')
        if "text_chunk" not in chunk:
            continue
        data = json.loads(chunk)
        event = data.get('event')
        if not event or event != 'text_chunk':
            continue
        print(data.get('data', {}).get('text'))
