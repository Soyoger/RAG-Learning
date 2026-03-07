#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/5 10:14
# @Author  : yongjie.su
# @File    : （3）Context Entities Recall（上下文实体召回率）.py
# @Software: PyCharm
from ragas import SingleTurnSample
from ragas.metrics import ContextEntityRecall

sample = SingleTurnSample(
    reference="中国的首都是北京。",
    retrieved_contexts=["北京是中国的首都，位于中国华北地区。它是中国的政治、文化、国际交往和科技创新中心，也是全国重要的交通枢纽。"],
)

scorer = ContextEntityRecall()

await scorer.single_turn_ascore(sample)
