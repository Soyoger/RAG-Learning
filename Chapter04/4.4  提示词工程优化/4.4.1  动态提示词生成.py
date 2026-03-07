#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/11/30 22:11
# @Author  : yongjie.su
# @File    : 4.4.1  动态提示词生成.py
# @Software: PyCharm
from langchain.prompts import PromptTemplate

prompt_template = """
    # 角色
    1. 你是一位AI问答助理。

    # 任务
    1. 确定用户提问的真实含义和意图。
    2. 结合上下文信息，给出专业、严谨的答案。
    3. 要求JSON格式输出结果。
    
    # 用户提问
    {question}

    # 上下文
    {context}

    # 限制
    1. 只对合法的问题进行严谨的回答，拒绝回答任何违法违规的话题。
    2. 生成的答案严格限制不超过100字。
"""


def dynamic_prompt(user_query, context):
    prompt = PromptTemplate(template=prompt_template, input_variables=["question", "context"])
    return prompt.format(question=user_query, context=context)


user_query = "什么是人工智能？"
answers = [
    "人工智能的英文全称是：Artificial Intelligence。",
    "人工智能简称：AI。",
    "一种由计算机科学和工程学发展而来的技术，旨在模拟和扩展人类的智能行为。",
    "具有学习、推理、感知和决策能力的算法和系统，能够完成通常需要人类智能的任务。",
    "具有很大的优势，如提高效率、降低成本、增强数据洞察力。"
]
context = "\n".join(answers)
prompt = dynamic_prompt(user_query, context)
print(prompt)
