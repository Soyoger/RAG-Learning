#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 13:49
# @Author  : yongjie.su
# @File    : 2.2.5  按标记进行分割.py
# @Software: PyCharm
# pip3 install tiktoken
from langchain.text_splitter import CharacterTextSplitter

file_path = '../example_data/三国演义.txt'
with open(file_path, encoding='utf-8') as f:
    text = f.read()

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=128, chunk_overlap=0
)
texts = text_splitter.split_text(text)
print(texts)


from langchain.text_splitter import TokenTextSplitter

text_splitter = TokenTextSplitter(chunk_size=10, chunk_overlap=0)

texts = text_splitter.split_text(text)
print(texts[0])
