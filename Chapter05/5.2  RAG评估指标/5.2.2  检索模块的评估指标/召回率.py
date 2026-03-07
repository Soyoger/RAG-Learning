#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/12/16 23:29
# @Author  : yongjie.su
# @File    : 召回率.py
# @Software: PyCharm

def calculate_recall(retrieved_docs: list, relevant_docs: list):
    """
    计算召回率

    参数:
    retrieved_docs (list): 检索到的文档列表
    relevant_docs (list): 相关文档列表

    返回:
    float: 召回率
    """
    # 计算检索到的相关文档数量
    relevant_retrieved_docs = [doc for doc in retrieved_docs if doc in relevant_docs]

    # 计算召回率
    recall = len(relevant_retrieved_docs) / len(relevant_docs) if relevant_docs else 0
    return recall


# 所有相关文档列表
retrieved_docs = ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
# 检索到的文档列表
relevant_docs = ['doc2', 'doc3', 'doc4', 'doc5', 'doc6']

# 计算召回率
recall = calculate_recall(retrieved_docs, relevant_docs)
print(f"召回率: {recall:.2f}")
