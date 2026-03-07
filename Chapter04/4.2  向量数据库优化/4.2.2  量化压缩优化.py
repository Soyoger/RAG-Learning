#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/11/24 23:01
# @Author  : yongjie.su
# @File    : 4.2.2  量化压缩优化.py
# @Software: PyCharm
import faiss
import numpy as np

# 1. 生成随机向量数据
num_vectors = 10000  # 向量数量
dim = 128  # 向量维度
vectors = np.random.random((num_vectors, dim)).astype('float32')

# 2. 使用 FAISS 创建产品量化索引
num_clusters = 100  # IVF 聚类数量
quantizer = faiss.IndexFlatL2(dim)  # 用于初始聚类的索引
index = faiss.IndexIVFPQ(quantizer, dim, num_clusters, 16, 8)  # 16 子向量，8 位量化

# 训练产品量化索引
index.train(vectors)

# 添加向量到索引
index.add(vectors)

# 保存量化索引到文件
faiss.write_index(index, 'quantized_index.faiss')



# 量化后的存储大小对比
import os

original_size = os.path.getsize('vectors.parquet')
snappy_size = os.path.getsize('snappy_vectors.parquet')
quantized_size = os.path.getsize('quantized_index.faiss')


print(f"原始向量大小: {original_size / 1024:.2f} KB")
print(f"snappy压缩大小: {snappy_size / 1024:.2f} KB")
print(f"量化索引大小: {quantized_size / 1024:.2f} KB")