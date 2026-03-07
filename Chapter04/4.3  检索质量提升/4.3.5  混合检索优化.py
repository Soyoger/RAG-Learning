#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/11/30 18:42
# @Author  : yongjie.su
# @File    : 4.3.5  混合检索优化.py
# @Software: PyCharm

def reciprocal_rank_fusion(datasets, doc, k=60):
    """
    RRF 算法
    datasets = {
    "query1": ['doc1', 'doc2', 'doc3'],
    "query2": ['doc2', 'doc3', 'doc4'],
    }
    :param datasets: 文本内容合集
    :param doc: 具体每个文本内容
    :param k: 平滑参数，默认值60
    :return:
    """
    queries = list(datasets.keys())

    def result_func(q):
        return datasets[q]

    def rank_func(results, d):
        return results.index(d) + 1

    rank_score = 0.0
    for q in queries:
        results = result_func(q)
        if doc in results:
            rank = rank_func(results, doc)
            rank_score += 1.0 / (k + rank)
    return rank_score


# 假设案例

# 稀疏检索结果
kw_responses = ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
# 密集检索结果
vec_responses = ['doc2', 'doc3', 'doc5', 'doc6', 'doc7']
# 平滑参数，默认60
k = 60
# 合并数据集
datasets = {
    "kw": kw_responses,
    "vec": vec_responses
}
# 获取所有文本内容
docs = []
for key, values in datasets.items():
    docs.extend(values)
# 进行RRF融合
scores = {}
for doc in docs:
    score = reciprocal_rank_fusion(datasets, doc, k=60)
    scores[doc] = score
# 进行排序
sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
print(sorted_scores)
# 获取融合后结果的Top-K=5的结果
hit_texts = []
top_k = 5
for sorted_score in sorted_scores[:top_k]:
    hit_text = sorted_score[0] if sorted_score else None
    hit_texts.append(hit_text)
print(hit_texts)
