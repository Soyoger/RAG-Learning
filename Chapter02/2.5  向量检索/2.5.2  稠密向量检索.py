#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 22:09
# @Author  : yongjie.su
# @File    : 2.5.2  稠密向量检索.py
# @Software: PyCharm
from langchain_core.documents import Document
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS

dash_scope_api_key = "sk-3a30xxx"

embeddings = DashScopeEmbeddings(
    model="text-embedding-v3", dashscope_api_key=dash_scope_api_key
)

texts = [
    "我们发顺丰快递。",
    "我们的包裹是从北京发货的。",
    "我们的商品都是有正品保障的，支持七天无理由退换货。",
    "护手霜男女生都适用，适用效果非常好。"
]
docs = [Document(page_content=text, metadata={"index": idx}) for idx, text in enumerate(texts)]
db = FAISS.from_documents(docs, embeddings)

# 相似度检索
query = "发什么快递？"
docs = db.similarity_search(query, k=3)
print(docs)

# 返回得分
query = "发什么快递？"
docs = db.similarity_search_with_score(query, k=3)
print(docs)

# 过滤
query = "发什么快递？"
docs = db.similarity_search_with_score(query, k=3, filter=dict(index=0))
print(docs)
