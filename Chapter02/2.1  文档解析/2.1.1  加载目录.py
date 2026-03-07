#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 17:09
# @Author  : yongjie.su
# @File    : 2.1.1  加载目录.py
# @Software: PyCharm
from langchain_community.document_loaders import DirectoryLoader

# 在底层，默认情况下使用 UnstructuredLoader
# pip3 install pdfminer.six  unstructured_inference==0.11.0 unstructured_pytesseract
loader = DirectoryLoader(path='../example_data/', glob="*.csv")
docs = loader.load()
print(docs)

# 显示进度条
loader = DirectoryLoader(path='../example_data/', glob="*.csv", show_progress=True)
docs = loader.load()
print(docs)

# 使用多线程
loader = DirectoryLoader(
    path='../example_data/',
    glob="*.csv",
    use_multithreading=True,
    max_concurrency=4
)
docs = loader.load()
print(docs)

# 指定加载器，整个文本内容
from langchain_community.document_loaders import TextLoader

loader = DirectoryLoader(path='../example_data/', glob="*.csv", loader_cls=TextLoader)
docs = loader.load()
print(docs)

# 自定义加载器，按照行加载
from custome_loader import CustomTextLoader

loader = DirectoryLoader(path='../example_data/', glob="*.csv", loader_cls=CustomTextLoader)
docs = loader.load()
print(docs)
