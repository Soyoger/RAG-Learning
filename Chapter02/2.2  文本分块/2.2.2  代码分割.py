#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 11:12
# @Author  : yongjie.su
# @File    : 2.2.2  代码分割.py
# @Software: PyCharm
from langchain.text_splitter import Language

languages = [e.value for e in Language]
print(languages)

from langchain.text_splitter import RecursiveCharacterTextSplitter

python_code = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
python_docs = python_splitter.create_documents([python_code])
print(python_docs)
