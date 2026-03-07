#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 15:00
# @Author  : yongjie.su
# @File    : dashscope_embed.py
# @Software: PyCharm
from langchain_community.embeddings import DashScopeEmbeddings

dash_scope_api_key = "sk-3a30xxx"

embeddings = DashScopeEmbeddings(
    model="text-embedding-v3", dashscope_api_key=dash_scope_api_key
)

text = "这是一个测试内容！"

doc_results = embeddings.embed_documents([text])
print(doc_results)

query_result = embeddings.embed_query(text)
print(query_result)
