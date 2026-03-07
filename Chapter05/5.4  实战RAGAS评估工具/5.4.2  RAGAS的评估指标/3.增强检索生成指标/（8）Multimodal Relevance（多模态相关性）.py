#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/5 11:01
# @Author  : yongjie.su
# @File    : （8）Multimodal Relevance（多模态相关性）.py
# @Software: PyCharm
from ragas import SingleTurnSample
from ragas.metrics import MultiModalRelevance

sample = SingleTurnSample(
    user_input="特斯拉Model X 怎么样？",
    response="猫很可爱。",
    # 上下文视觉
    retrieved_contexts=[
        "./images/tesla.jpg"
    ]
)
scorer = MultiModalRelevance()
await scorer.single_turn_ascore(sample)