#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/3/15 23:51
# @Author  : yongjie.su
# @File    : 2.LangChain中ReAct的实现.py
# @Software: PyCharm
from langchain_core.messages import HumanMessage
from langchain_core.tools import BaseTool
from langgraph.prebuilt import create_react_agent
from langchain_community.chat_models import ChatTongyi


# 自定义工具类
class MyCustomTool(BaseTool):
    name: str = "自定义工具"
    description: str = "自定义工具描述"

    def _run(self, query: str) -> str:
        # 工具的自定义实现
        return query

    async def _arun(self, query: str) -> str:
        # 工具的自定义异步实现方法
        result = await self._run(query)
        return result


# 创建工具
search = MyCustomTool()
tools = [search]
# 创建通义千问大模型
dash_scope_api_key = "sk-3a30xxx"
model = ChatTongyi(
    model="qwen-long",
    top_p=0.8,
    temperature=0.8,
    dashscope_api_key=dash_scope_api_key
)
# 创建Agent
agent = create_react_agent(model, tools)
messages = {
    "messages": [
        HumanMessage(content="介绍一下Agent"),
        HumanMessage(content="Agent的应用有哪些？")
    ]
}
# 执行
for chunk in agent.stream(messages):
    print(chunk)
