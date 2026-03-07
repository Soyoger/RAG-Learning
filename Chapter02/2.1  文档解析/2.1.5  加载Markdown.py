#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/29 18:12
# @Author  : yongjie.su
# @File    : 2.1.5  加载Markdown.py
# @Software: PyCharm
# pip3 install unstructured markdown
from langchain_community.document_loaders import UnstructuredMarkdownLoader

markdown_path = "../example_data/generation_prompt.md"
loader = UnstructuredMarkdownLoader(markdown_path)
data = loader.load()
print(data)

# 保留元素
loader = UnstructuredMarkdownLoader(markdown_path, mode="elements")
data = loader.load()
print(data)
