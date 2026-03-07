#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/5 10:38
# @Author  : yongjie.su
# @File    : （5）Response Relevancy（响应相关性）.py
# @Software: PyCharm
from ragas import SingleTurnSample
from ragas.metrics import ResponseRelevancy

sample = SingleTurnSample(
    user_input="中国的首都在哪儿?",
    response="中国的首都是北京。",
    retrieved_contexts=["北京是中国的首都，位于中国华北地区。它是中国的政治、文化、国际交往和科技创新中心，也是全国重要的交通枢纽。"],
)

scorer = ResponseRelevancy()
await scorer.single_turn_ascore(sample)
