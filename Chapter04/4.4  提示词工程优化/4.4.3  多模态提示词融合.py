#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/11/30 22:54
# @Author  : yongjie.su
# @File    : 4.4.3  多模态提示词融合.py
# @Software: PyCharm
from langchain.prompts import PromptTemplate

template = """
    # 角色
    1. 你是一位AI问答助理。

    # 任务
    1. 确定用户提问的真实含义和意图。
    2. 结合文本上下文和图片上下文信息，给出专业、严谨的答案。
    3. 要求JSON格式输出结果。

    # 用户提问
    {question}

    # 上下文
    文本上下文：{text_context}
    图片上下文：{image_context}

    # 限制
    1. 只对合法的问题进行严谨的回答，拒绝回答任何违法违规的话题。
    2. 生成的答案严格限制不超过100字。
"""


def dynamic_prompt(user_query, text_context, image_context):
    """
    生成提示词
    :param user_query: 用户提问
    :param text_context: 文本上下文
    :param image_context: 图片上下文
    :return:
    """
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["question", "text_context", "image_context"]
    )
    prompt_format = prompt_template.format(
        question=user_query,
        text_context=text_context,
        image_context=image_context
    )
    return prompt_format


def get_text_context():
    """
    生成文本特征
    :return:
    """
    return "Mock：text_features"


def get_image_context():
    """
    生成图片特征
    :return:
    """
    return "Mock: image_features"


user_query = "什么是人工智能？"
text_context = get_text_context()
image_context = get_image_context()
prompt = dynamic_prompt(user_query, text_context, image_context)
print(prompt)
