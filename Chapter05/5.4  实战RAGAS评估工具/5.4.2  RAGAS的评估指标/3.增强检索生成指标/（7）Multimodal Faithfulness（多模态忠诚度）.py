#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/5 10:51
# @Author  : yongjie.su
# @File    : （7）Multimodal Faithfulness（多模态忠诚度）.py
# @Software: PyCharm
from ragas import SingleTurnSample
from ragas.metrics import MultiModalFaithfulness

sample = SingleTurnSample(
    user_input="特斯拉Model X 怎么样？",
    response="猫很可爱。",
    # 上下文视觉
    retrieved_contexts=[
        "./images/tesla.jpg"
    ]
)
scorer = MultiModalFaithfulness()
await scorer.single_turn_ascore(sample)
