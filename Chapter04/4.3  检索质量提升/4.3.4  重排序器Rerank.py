#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/11/30 11:18
# @Author  : yongjie.su
# @File    : 4.3.4  重排序器Rerank.py
# @Software: PyCharm

# 用户提问 question
question = "冬天怎么保护汽车电池？"
# 向量检索结果
answers = [
    '定期检查电池电量，保持充足电量。',
    '停车时避免长时间使用电子设备。',
    '为电池接线柱涂防腐脂以防氧化。',
    '每周至少短途行驶一次，充电维护。',
    '使用电池保温罩保护低温环境下的电池。',
    '检查电池连接是否松动并及时紧固。',
    '停车尽量选择车库或避风处。',
    '长时间不用车时，断开电池负极。',
    '确保充电系统工作正常，检测发电机。',
    '更换老化电池，确保冬季性能稳定。'
]
# 组成问题和答案对
pairs = [[question, answer] for answer in answers]


from FlagEmbedding import FlagReranker
# 构造一个FlagReranker实例，设置量化 use_fp16为true，可以加快计算速度
reranker = FlagReranker('bge-reranker-large', use_fp16=True)

# 计算多对文本间的相关性评分
scores = reranker.compute_score(sentence_pairs=pairs, normalize=True)
print(scores)

# 排序并记录对应的下标，按评分降序排列
sorted_scores_with_indices = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
print(f"排序后的结果：{sorted_scores_with_indices}")
# 获取TopK=3的文本n=内容
texts = []
top_k = 3
for score_indices in sorted_scores_with_indices[:top_k]:
    indice = score_indices[0]
    score = score_indices[1]
    text = answers[indice]
    texts.append(text)
print(f"Rerank之后的结果：{texts}")
