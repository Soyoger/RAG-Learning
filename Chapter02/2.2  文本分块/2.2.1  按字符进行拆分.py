#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 10:47
# @Author  : yongjie.su
# @File    : 2.2.1  按字符进行拆分.py
# @Software: PyCharm
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="------------\n\n",
    chunk_size=1024,
    chunk_overlap=100,
    length_function=len,
)

file_path = '../example_data/三国演义.txt'
with open(file_path, encoding='utf-8') as f:
    text = f.read()
partitions = text_splitter.split_text(text)
metadatas = []
for idx in range(len(partitions)):
    metadatas.append({"file_path": file_path, "chapter": idx + 1})
docs = text_splitter.create_documents(partitions, metadatas=metadatas)

print(docs)

# 指定加载器
# 指定加载器，整个文本内容
from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path)
documents = loader.load()
docs = partitions = text_splitter.split_documents(documents)
print(docs)

