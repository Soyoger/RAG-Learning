#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/4 13:33
# @Author  : yongjie.su
# @File    : RAGAS中的Prompt.py
# @Software: PyCharm
from ragas.prompt import PydanticPrompt
from pydantic import BaseModel, Field


class MyInput(BaseModel):
    question: str = Field(description="模型的输入")


class MyOutput(BaseModel):
    answer: str = Field(description="模型的输出")


class MyPrompt(PydanticPrompt[MyInput, MyInput]):
    instruction = "自然语言指令，描述大语言模型应执行的任务。"
    input_model = MyInput
    output_model = MyOutput
    examples = [
        (
            MyInput(question="北京在哪儿？"),
            MyOutput(answer="北京是中国的首都，位于中国华北地区。")
        )
    ]


if __name__ == "__main__":
    my_prompt = MyPrompt()
    print(my_prompt.to_string())
