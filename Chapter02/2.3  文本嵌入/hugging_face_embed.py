#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 15:18
# @Author  : yongjie.su
# @File    : hugging_face_embed.py
# @Software: PyCharm
from langchain_community.embeddings import HuggingFaceEmbeddings

model_name = "bge-large-zh-v1.5"

embeddings = HuggingFaceEmbeddings(model_name=model_name)

text = "这是一个测试内容！"

doc_results = embeddings.embed_documents([text])
print(doc_results)

query_result = embeddings.embed_query(text)
print(query_result)
