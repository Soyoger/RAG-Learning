#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 12:33
# @Author  : yongjie.su
# @File    : 2.3.1  文本嵌入的定义.py
# @Software: PyCharm

from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(openai_api_key="...")

embeddings = embeddings_model.embed_documents(
    [
        "您好呀",
        "这是测试数据"
    ]
)

embedded_query = embeddings_model.embed_query("这是一条查询测试？")
