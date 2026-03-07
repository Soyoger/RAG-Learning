#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 18:02
# @Author  : yongjie.su
# @File    : 2.4.2  Faiss.py
# @Software: PyCharm
from langchain_core.documents import Document
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS

dash_scope_api_key = "sk-3a30xxx"

embeddings = DashScopeEmbeddings(
    model="text-embedding-v3", dashscope_api_key=dash_scope_api_key
)

texts = [
    "发什么快递？",
    "快递包邮哦"
]
docs = [Document(page_content=text, metadata={"index": idx}) for idx, text in enumerate(texts)]
db = FAISS.from_documents(docs, embeddings)
# 打印出向量数据库的内容
print(db.docstore._dict)

# 本地保存
db.save_local("faiss_index")
# 本地加载
new_db = FAISS.load_local("faiss_index", embeddings)

texts_2 = [
    "如何下单呢？",
    "有什么优惠吗？"
]
docs_2 = [Document(page_content=text, metadata={"index": idx}) for idx, text in enumerate(texts_2)]
db_2 = FAISS.from_documents(docs_2, embeddings)

# 合并
db.merge_from(db_2)
print(db.docstore._dict)
