#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 19:28
# @Author  : yongjie.su
# @File    : multi_rag.py
# @Software: PyCharm
import os
import glob

image_dir = "data/images/"


def get_images():
    images = glob.glob(image_dir + "*.jpg")
    return images


image_paths = get_images()

import numpy as np
import torch
from transformers import AutoModel

MODEL_NAME = "BAAI/BGE-VL-base"  # or "BAAI/BGE-VL-base"

model = AutoModel.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True)
model.set_processor(MODEL_NAME)
model.eval()

with torch.no_grad():
    embeddings = model.encode(image_paths).to('cpu')

embeddings = np.array(embeddings).astype(np.float32)

import faiss

dim = embeddings.shape[1]
index = faiss.index_factory(dim, "Flat", faiss.METRIC_L2)

index.add(embeddings)

queries = [
    "找到有长颈鹿的图片"
]

k = 1

with torch.no_grad():
    queries_vec = model.encode(
        text=queries,
    ).to('cpu')

D, I = index.search(queries_vec, k=k)

print(D, I)
