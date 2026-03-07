#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/27 16:09
# @Author  : yongjie.su
# @File    : 2.1.2  加载CSV.py
# @Software: PyCharm
from langchain.document_loaders.csv_loader import CSVLoader

# CSV 加载器
loader = CSVLoader(file_path='../example_data/直播评论.csv')
data = loader.load()
print(data)

# 自定义CSV 解析和加载
csv_args = {
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['问题', '是否有效', '评判依据']
}
loader = CSVLoader(file_path='../example_data/直播评论.csv', csv_args=csv_args)
data = loader.load()
print(data)

# 指定用于标识文档来源的列
csv_args = {
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['问题', '是否有效', '评判依据']
}
loader = CSVLoader(file_path='../example_data/直播评论.csv', csv_args=csv_args, source_column="问题")
data = loader.load()
print(data)
