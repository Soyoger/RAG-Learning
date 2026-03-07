#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/5 10:26
# @Author  : yongjie.su
# @File    : （4）Noise Sensitivity（噪音敏感度）.py
# @Software: PyCharm
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import NoiseSensitivity

sample = SingleTurnSample(
    user_input="印度人寿保险公司 (LIC) 为何闻名？",
    response="印度人寿保险公司（LIC）是印度最大的保险公司，以其庞大的投资组合而闻名。LIC 为国家的金融稳定做出了重要贡献。",
    reference="印度人寿保险公司 (LIC) 是印度最大的保险公司，于 1956 年通过保险业国有化成立。它以管理大量投资组合而闻名。",
    retrieved_contexts=[
        "印度人寿保险公司 (LIC) 于 1956 年印度保险业国有化后成立。",
        " LIC 是印度最大的保险公司，拥有庞大的保单持有人网络，在金融领域发挥着重要作用。",
        "作为印度最大的机构投资者，LIC 管理着大量的人寿基金，为国家的金融稳定做出了贡献。",
        "得益于金融、技术、制造等行业，印度经济是世界上增长最快的主要经济体之一。"
    ]
)

scorer = NoiseSensitivity()
await scorer.single_turn_ascore(sample)
