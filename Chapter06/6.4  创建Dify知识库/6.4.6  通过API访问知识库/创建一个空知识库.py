#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/12/8 11:13
# @Author  : yongjie.su
# @File    : 创建一个空知识库.py
# @Software: PyCharm
import requests

API_KEY = "dataset-0463xxx"
HOST = "http://43.130.48.238/v1"

create_url = f"{HOST}/datasets"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

body = {
    "name": "测试空知识库",
    "permission": "only_me"
}
# 创建空知识库
response = requests.post(create_url, headers=headers, json=body, timeout=60).json()
print(response)
