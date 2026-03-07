#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/12/15 23:21
# @Author  : yongjie.su
# @File    : 精确度.py
# @Software: PyCharm
def calculate_precision(retrieved_docs: list, relevant_docs: list):
    """
    计算精确度

    参数:
    retrieved_docs (list): 检索到的文档列表
    relevant_docs (list): 相关文档列表

    返回:
    float: 精确度
    """
    # 计算检索到的相关文档数量
    relevant_retrieved_docs = [doc for doc in retrieved_docs if doc in relevant_docs]

    # 计算精确度
    precision = len(relevant_retrieved_docs) / len(retrieved_docs) if retrieved_docs else 0
    return precision


# 所有相关文档列表
retrieved_docs = ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
# 检索到的文档
relevant_docs = ['doc2', 'doc3', 'doc4', 'doc5', 'doc6']

# 计算精确度
precision = calculate_precision(retrieved_docs, relevant_docs)
print(f"精确度: {precision:.2f}")
