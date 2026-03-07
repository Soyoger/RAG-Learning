#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/4 17:58
# @Author  : yongjie.su
# @File    : 评估多轮样本.py
# @Software: PyCharm
from ragas.messages import HumanMessage, AIMessage, ToolMessage, ToolCall
from ragas import MultiTurnSample

# 用户消息
user_message = HumanMessage(content="北京今天的天气怎么样？")
# AI 的初始响应
ai_initial_response = AIMessage(
    content="让我帮你查看一下今天北京的天气。",
    tool_calls=[ToolCall(name="WeatherAPI", args={"location": "北京"})]
)
# 工具的响应
tool_response = ToolMessage(content="今天北京天气多云转晴，气温30度。")
# AI 的最终回答
ai_final_response = AIMessage(
    content="北京今天天气多云转晴，气温30度。")
# 将上述消息按照时间顺序组织成一个列表，代表完整的对话流。
conversation = [
    user_message,
    ai_initial_response,
    tool_response,
    ai_final_response
]
# 定义参考响应
reference_response = "定义参考响应，作为对话评估的基准。这是一个目标或期望的答案，通常由人工标注者提供，用于评估系统的实际输出是否符合预期。"
# 实例化一个 MultiTurnSample 对象，用于封装多轮对话和参考响应。
sample = MultiTurnSample(
    user_input=conversation,
    reference=reference_response,
)
