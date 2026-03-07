#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 13:42
# @Author  : yongjie.su
# @File    : 2.2.4  递归按字符分割.py
# @Software: PyCharm
from langchain.text_splitter import RecursiveCharacterTextSplitter

file_path = '../example_data/三国演义.txt'
with open(file_path, encoding='utf-8') as f:
    text = f.read()

separators = ["------------\n\n", "\n\n", "\n", " "]
text_splitter = RecursiveCharacterTextSplitter(
    separators=separators,
    chunk_size=256,
    chunk_overlap=30,
    length_function=len,
)
texts = text_splitter.create_documents([text])
print(texts)
