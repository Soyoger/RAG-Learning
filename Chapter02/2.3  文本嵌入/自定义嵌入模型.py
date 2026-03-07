#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 17:08
# @Author  : yongjie.su
# @File    : 自定义嵌入模型.py
# @Software: PyCharm
from langchain_core.embeddings import Embeddings
from pydantic import BaseModel


class CustomEmbeddings(BaseModel, Embeddings):
    def embed_documents(self, texts):
        # 实现你自己的文档嵌入逻辑
        pass

    def embed_query(self, text):
        # 实现你自己的查询嵌入逻辑
        pass
