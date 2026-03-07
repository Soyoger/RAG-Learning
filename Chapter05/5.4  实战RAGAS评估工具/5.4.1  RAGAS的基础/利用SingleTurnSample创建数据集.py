#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/4 18:22
# @Author  : yongjie.su
# @File    : 利用SingleTurnSample创建数据集.py
# @Software: PyCharm
from ragas import SingleTurnSample, EvaluationDataset

# 创建多个代表各个评估样本的SingleTurnSample实例
# Sample 1
sample1 = SingleTurnSample(
    user_input="中国的首都在哪儿?",
    retrieved_contexts=["北京是中国的首都，位于中国华北地区。它是中国的政治、文化、国际交往和科技创新中心，也是全国重要的交通枢纽。"],
    response="中国的首都是北京。",
    reference="北京",
)
# Sample 2
sample2 = SingleTurnSample(
    user_input="北京有什么好玩的地方？",
    retrieved_contexts=["北京有故宫、长城、天坛、颐和园等历史文化景点，还有胡同、王府井等现代商业区，兼具传统和现代魅力。"],
    response="北京有故宫、长城、天坛、颐和园等历史景点，还有胡同、王府井等现代文化体验。",
    reference="北京有故宫、长城、天坛等著名景点。",
)
# Sample 3
sample3 = SingleTurnSample(
    user_input="北京今天天气怎么样？",
    retrieved_contexts=["今天，北京多云转晴，气温30°C，微风。请注意，天气预报可能会有所变化，建议您在出行前查看最新的天气信息。"],
    response="今天，北京多云转晴，气温30°C，微风。",
    reference="北京今天多云转晴，气温30度。",
)
# 通过传递SingleTurnSample实例的列表来创建EvaluationDataset
dataset = EvaluationDataset(samples=[sample1, sample2, sample3])
