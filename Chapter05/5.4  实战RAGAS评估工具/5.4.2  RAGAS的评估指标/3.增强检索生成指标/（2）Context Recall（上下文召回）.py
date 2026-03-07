#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/5 01:23
# @Author  : yongjie.su
# @File    : （2）Context Recall（上下文召回）.py
# @Software: PyCharm
# 基于LLM的上下文回忆
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import LLMContextRecall

sample = SingleTurnSample(
    user_input="中国的首都在哪儿?",
    response="中国的首都是北京。",
    reference="北京",
    retrieved_contexts=["北京是中国的首都，位于中国华北地区。它是中国的政治、文化、国际交往和科技创新中心，也是全国重要的交通枢纽。"],
)

context_recall = LLMContextRecall()
await context_recall.single_turn_ascore(sample)

# 非基于LLM的上下文回忆
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import NonLLMContextRecall

sample = SingleTurnSample(
    retrieved_contexts=["北京是中国的首都，位于中国华北地区。它是中国的政治、文化、国际交往和科技创新中心，也是全国重要的交通枢纽。"],
    reference_contexts=["中国的首都是北京。",
                        "北京是中国的首都，位于中国华北地区。它是中国的政治、文化、国际交往和科技创新中心，也是全国重要的交通枢纽。"])

context_recall = NonLLMContextRecall()
await context_recall.single_turn_ascore(sample)
