#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/4 17:55
# @Author  : yongjie.su
# @File    : 评估单轮样本.py
# @Software: PyCharm
from ragas import SingleTurnSample

# 用户问题
user_input = "中国的首都在哪儿?"
# 检索上下文
retrieved_contexts = ["北京是中国的首都，位于中国华北地区。它是中国的政治、文化、国际交往和科技创新中心，也是全国重要的交通枢纽。"]
# AI的回答
response = "中国的首都是北京。"
# 参考答案
reference = "北京"
# 评估标准：准确性、完整性和流畅性
rubric = {
    "accuracy": "Correct",
    "completeness": "High",
    "fluency": "Excellent"
}
# 创建 SingleTurnSample 实例
sample = SingleTurnSample(
    user_input=user_input,
    retrieved_contexts=retrieved_contexts,
    response=response,
    reference=reference,
    rubric=rubric
)
