#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 22:01
# @Author  : yongjie.su
# @File    : 2.5.1  稀疏向量检索.py
# @Software: PyCharm
from langchain_community.retrievers import BM25Retriever

texts = [
    "我们发顺丰快递。",
    "我们的包裹是从北京发货的。",
    "我们的商品都是有正品保障的，支持七天无理由退换货。",
    "护手霜男女生都适用，适用效果非常好。"
]

retriever = BM25Retriever.from_texts(texts)
result = retriever.invoke("我们发顺丰快递。")
print(result)
