#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/3/16 10:31
# @Author  : yongjie.su
# @File    : 快速创建一个搜索Agent.py
# @Software: PyCharm
from agents import Agent, WebSearchTool, Runner

# 定义一个Web搜索Agent
web_search = WebSearchTool()
agent = Agent(
    name="搜索助手",
    tools=[web_search],
    model="gpt-4-turbo"
)
response = Runner.run_sync(agent, "OpenAI的Agent SDK怎么使用？")
print(response.final_output)
