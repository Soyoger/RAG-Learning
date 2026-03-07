#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/4 23:38
# @Author  : yongjie.su
# @File    : （1）上下文精度.py
# @Software: PyCharm
# 基于LLM的上下文精度
# 无参考的上下文精度
from ragas import SingleTurnSample
from ragas.metrics import LLMContextPrecisionWithoutReference

context_precision = LLMContextPrecisionWithoutReference()

sample = SingleTurnSample(
    user_input="中国的首都在哪儿?",
    response="中国的首都是北京。",
    retrieved_contexts=["北京是中国的首都，位于中国华北地区。它是中国的政治、文化、国际交往和科技创新中心，也是全国重要的交通枢纽。"],
)
await context_precision.single_turn_ascore(sample)

# 参考上下文精度
from ragas import SingleTurnSample
from ragas.metrics import LLMContextPrecisionWithReference

context_precision = LLMContextPrecisionWithReference()

sample = SingleTurnSample(
    user_input="中国的首都在哪儿?",
    reference="北京",
    retrieved_contexts=["北京是中国的首都，位于中国华北地区。它是中国的政治、文化、国际交往和科技创新中心，也是全国重要的交通枢纽。"],
)

await context_precision.single_turn_ascore(sample)

# 非基于LLM的上下文精度
from ragas import SingleTurnSample
from ragas.metrics import NonLLMContextPrecisionWithReference

# 参考上下文的上下文精度
context_precision = NonLLMContextPrecisionWithReference()

sample = SingleTurnSample(
    retrieved_contexts=["中国的首都在哪儿?"],
    reference_contexts=["中国的首都是北京。",
                        "北京是中国的首都，位于中国华北地区。它是中国的政治、文化、国际交往和科技创新中心，也是全国重要的交通枢纽。"]
)

await context_precision.single_turn_ascore(sample)
