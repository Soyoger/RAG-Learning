#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 11:59
# @Author  : yongjie.su
# @File    : 2.2.3  按MarkDown标题分割.py
# @Software: PyCharm
from langchain.text_splitter import MarkdownHeaderTextSplitter

markdown_path = "../example_data/generation_prompt.md"
with open(markdown_path, encoding='utf-8') as f:
    markdown_document = f.read()

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_header_splits = markdown_splitter.split_text(markdown_document)
for split in md_header_splits:
    print(split)
