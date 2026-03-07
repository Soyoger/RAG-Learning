#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/12/8 11:43
# @Author  : yongjie.su
# @File    : 获取知识库列表.py
# @Software: PyCharm
import requests

API_KEY = "dataset-0463xxx"
HOST = "http://43.130.48.238/v1"

create_url = f"{HOST}/datasets"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

params = {
    "page": 1,
    "limit": 10
}

# 获取知识库列表
response = requests.get(create_url, params=params, headers=headers, timeout=60).json()
print(response)
