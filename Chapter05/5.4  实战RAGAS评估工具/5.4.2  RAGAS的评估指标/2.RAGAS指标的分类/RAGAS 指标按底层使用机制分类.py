#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/4 23:04
# @Author  : yongjie.su
# @File    : RAGAS 指标按底层使用机制分类.py
# @Software: PyCharm
from ragas.metrics import FactualCorrectness
from ragas import MultiTurnSample, SingleTurnSample

from ragas.metrics import AgentGoalAccuracyWithReference

# 占位
evaluation_llm = None
scorer = FactualCorrectness(llm=evaluation_llm)

# 单轮
metric = FactualCorrectness()
# 占位
sample = SingleTurnSample()
await metric.single_turn_ascore(sample)

# 多轮
metric = AgentGoalAccuracyWithReference()
# 占位
sample = MultiTurnSample()
await metric.multi_turn_ascore(sample)
