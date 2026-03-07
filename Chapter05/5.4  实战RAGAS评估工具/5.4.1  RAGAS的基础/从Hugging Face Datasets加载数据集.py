#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/4 18:25
# @Author  : yongjie.su
# @File    : 从Hugging Face Datasets加载数据集.py
# @Software: PyCharm
from datasets import load_dataset
from ragas import EvaluationDataset

# 从Hugging Face Datasets加载数据集
dataset = load_dataset("explodinggradients/amnesty_qa", "english_v3", trust_remote_code=True)

eval_dataset = EvaluationDataset.from_hf_dataset(dataset["eval"])
print(eval_dataset.samples[0])
