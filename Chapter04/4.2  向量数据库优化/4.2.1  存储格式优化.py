#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/11/24 22:34
# @Author  : yongjie.su
# @File    : 4.2.1  存储格式优化.py
# @Software: PyCharm
import os
import numpy as np
import pandas as pd

# 1. 生成随机向量数据
num_vectors = 10000  # 向量数量
dim = 128  # 向量维度
vectors = np.random.random((num_vectors, dim)).astype('float32')

# 2. 将向量数据转换为 DataFrame
vector_df = pd.DataFrame(vectors, columns=[f"dim_{i}" for i in range(dim)])

# 3. 将 DataFrame 写入 Parquet 文件
parquet_file = "vectors.parquet"
vector_df.to_parquet(parquet_file, engine="pyarrow", index=False)
print(f"向量数据已存储为 {parquet_file}")

# 4. 从 Parquet 文件读取数据
loaded_df = pd.read_parquet(parquet_file)
# 转换回 NumPy 数组
loaded_vectors = loaded_df.values

# 验证数据一致性
print("数据是否一致:", np.allclose(vectors, loaded_vectors))

# 5. 检查存储文件的大小
file_size = os.path.getsize(parquet_file)
print(f"Parquet 文件大小: {file_size / 1024:.2f} KB")

# 分块存储
import random

vector_df['category'] = [random.choice(['p1', 'p2', 'p3']) for _ in range(10000)]
vector_df.to_parquet("partitioned_vectors/", engine="pyarrow", partition_cols=["category"])

# 向量压缩
snappy_parquet_file = "snappy_vectors.parquet"
vector_df.to_parquet(snappy_parquet_file, engine="pyarrow", compression="snappy", index=False)
print(f"向量数据已存储为 {snappy_parquet_file}")