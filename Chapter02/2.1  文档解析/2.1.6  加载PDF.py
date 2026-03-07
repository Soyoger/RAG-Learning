#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/29 23:42
# @Author  : yongjie.su
# @File    : 2.1.6  加载PDF.py
# @Software: PyCharm
# pip3 install pypdf
from langchain_community.document_loaders import PyPDFLoader

# extract_images  pip3 install rapidocr-onnxruntime

loader = PyPDFLoader("../example_data/2024年AI大模型训练数据白皮书.pdf")
pages = loader.load_and_split()
print(pages[0])

# 解析图片
loader = PyPDFLoader("../example_data/2024年AI大模型训练数据白皮书.pdf", extract_images=True)
pages = loader.load_and_split()
print(pages[0])

# 使用PDFMiner
from langchain_community.document_loaders import PDFMinerLoader

loader = PDFMinerLoader("../example_data/2024年AI大模型训练数据白皮书.pdf")
pages = loader.load()
print(pages[0])