#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/11/25 23:10
# @Author  : yongjie.su
# @File    : 4.3.1  文本分块优化.py
# @Software: PyCharm
from langchain_community.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

model_name = "bge-large-zh-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=model_name)


def semantic_chunking(texts, threshold=0.7):
    """
    基于语义的分块方法
    :param texts: 输入文本
    :param threshold: 相似性阈值，决定分块语义差异
    :return: 分块后的文本列表
    """
    chunks, current_chunk = [], [texts[0]]
    current_embedding = embeddings.embed_query(current_chunk[0])

    for chunk in texts[1:]:
        chunk_embedding = embeddings.embed_query(chunk)
        similarity = cosine_similarity([current_embedding], [chunk_embedding])
        similarity = similarity[0][0]
        # 如果语义相似性低，开启新块
        if similarity < threshold:
            chunks.append(" ".join(current_chunk))
            current_chunk = [chunk]
            current_embedding = chunk_embedding
        else:
            current_chunk.append(chunk)
            # current_embedding = cosine_similarity([current_embedding], [chunk_embedding])
    if current_chunk:
        # 添加最后的块
        chunks.append(" ".join(current_chunk))
    return chunks


# 示例文本
texts = [
    "这个礼物真好看，我太喜欢了。",
    "我太喜欢了,这个漂亮的礼物了。",
    "这个礼物一般般。",
    "今天的天气真好。",
    "这几天天气真好。",
]

chunks = semantic_chunking(texts, threshold=0.75)
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: {chunk}")
