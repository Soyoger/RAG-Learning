#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/29 17:04
# @Author  : yongjie.su
# @File    : 2.1.4  加载JSON.py
# @Software: PyCharm
# pip3 install jq

import json
from pathlib import Path
from pprint import pprint

file_path = '../example_data/chat.json'
data = json.loads(Path(file_path).read_text())
pprint(data)

# 使用JSONLoader
from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path='../example_data/chat.json',
    jq_schema='.liveStreamQA[].answer'
)

data = loader.load()
pprint(data)


# 提取元数据，
# 默认元数据包含 source 和 seq_num 键。然而，JSON 数据中可能也包含这些键。
# 用户可以利用 metadata_func 重命名默认键并使用 JSON 数据中的键。

def metadata_func(record: dict, metadata: dict) -> dict:
    metadata["answer"] = record.get("answer")
    return metadata


loader = JSONLoader(
    file_path='../example_data/chat.json',
    jq_schema='.liveStreamQA[]',
    content_key='answer',
    metadata_func=metadata_func
)
data = loader.load()
pprint(data)
