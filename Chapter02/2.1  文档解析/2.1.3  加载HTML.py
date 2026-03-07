#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/29 16:24
# @Author  : yongjie.su
# @File    : 2.1.3  加载HTML.py
# @Software: PyCharm
from langchain_community.document_loaders import UnstructuredHTMLLoader

loader = UnstructuredHTMLLoader("../example_data/rag_introduce.html")
page = loader.load()
print(page)

# 使用 BeautifulSoup4 加载 HTML
from langchain_community.document_loaders import BSHTMLLoader

loader = BSHTMLLoader("../example_data/rag_introduce.html")
page = loader.load()
print(page)
