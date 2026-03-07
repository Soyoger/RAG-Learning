#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 14:28
# @Author  : yongjie.su
# @File    : openai_embed.py
# @Software: PyCharm
import os
from langchain_openai import OpenAIEmbeddings

os.environ['OPENAI_API_KEY'] = ""

embeddings = OpenAIEmbeddings()

text = "这是一个测试内容！"
# 嵌入文本列表
doc_result = embeddings.embed_documents([text])
print(doc_result)
# 嵌入单个文本
query_result = embeddings.embed_query(text)
print(query_result)
