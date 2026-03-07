#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/11/24 23:23
# @Author  : yongjie.su
# @File    : 4.2.3  检索算法优化.py
# @Software: PyCharm
import numpy as np
import faiss

# 1. 创建随机向量数据集
num_vectors = 10000  # 向量数量
dim = 128            # 向量维度
vectors = np.random.random((num_vectors, dim)).astype('float32')

# 2. 创建并训练 IVF 索引
num_clusters = 100  # IVF 索引中的聚类数量
quantizer = faiss.IndexFlatL2(dim)  # 用于聚类的基础索引
index = faiss.IndexIVFFlat(quantizer, dim, num_clusters)  # IVF 索引

# 训练索引（聚类中心初始化）
index.train(vectors)

# 添加向量到索引
index.add(vectors)

# 3. 查询优化
index.nprobe = 10  # 搜索的簇数量（提高查询精度）
query_vector = np.random.random((1, dim)).astype('float32')  # 随机查询向量

# 检索前 5 个最近邻
distances, indices = index.search(query_vector, k=5)
print("查询结果（距离和索引）:")
for dist, idx in zip(distances[0], indices[0]):
    print(f"Index: {idx}, Distance: {dist}")

# 4. 使用产品量化（PQ）进一步优化
pq_index = faiss.IndexIVFPQ(quantizer, dim, num_clusters, 16, 8)  # 16 子向量，8 位量化
pq_index.train(vectors)
pq_index.add(vectors)

# 查询 PQ 索引
pq_index.nprobe = 10
pq_distances, pq_indices = pq_index.search(query_vector, k=5)
print("PQ 查询结果（距离和索引）:")
for dist, idx in zip(pq_distances[0], pq_indices[0]):
    print(f"Index: {idx}, Distance: {dist}")

# 5. 索引存储与加载
faiss.write_index(pq_index, 'optimized_index.faiss')
loaded_index = faiss.read_index('optimized_index.faiss')

# 验证一致性
loaded_distances, loaded_indices = loaded_index.search(query_vector, k=5)
assert np.array_equal(pq_indices, loaded_indices), "索引结果不一致！"
print("索引成功保存并加载。")
