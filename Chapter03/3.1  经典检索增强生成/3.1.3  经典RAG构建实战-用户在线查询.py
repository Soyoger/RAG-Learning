#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/26 10:51
# @Author  : yongjie.su
# @File    : 3.1.3  经典RAG构建实战-用户在线查询.py.py
# @Software: PyCharm
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings


def get_embedding_model(dash_scope_api_key=None):
    """
    通义千问的embedding模型：embedding
    :param dash_scope_api_key:
    :return:
    """
    if dash_scope_api_key is None:
        return None
    embeddings = DashScopeEmbeddings(
        model="text-embedding-v3",
        dashscope_api_key=dash_scope_api_key
    )
    return embeddings


template = """
# 角色
你是一位资深AI智能助理，能够热情、真诚的回答用户的问题。

# 技能
精通中文，有良好的中文表达能力；掌握Markdown语法，能够准确识别和处理相关信息。

# 任务
根据用户输入的问题{question}，结合知识库检索的上下文信息{context}，对用户问题进行回答。

# 限制
输出字数不超过200字。
只输出与该问题相关的信息，其他信息自动忽略。

"""


def generate_text(prompt, model="qwen-long", top_p=0.8, temperature=0.1, api_key=None):
    chat = ChatTongyi(
        model=model, top_p=top_p, temperature=temperature, dashscope_api_key=api_key
    )
    text = chat.invoke(prompt)
    return text.content


if __name__ == "__main__":
    dash_scope_api_key = "sk-3a30xxx"
    # 词嵌入模型
    embeddings = get_embedding_model(dash_scope_api_key)
    vec_db = FAISS.load_local("vec.db", embeddings=embeddings)
    top_k = 5
    while True:
        prompt = PromptTemplate.from_template(template)
        question = input("请输入问题: ")
        if question == "stop":
            break
        top_k_contents = vec_db.similarity_search_with_score(question, k=top_k)
        context = "\n".join([top_k_content[0].page_content for top_k_content in top_k_contents])
        prompt = prompt.format_prompt(question=question, context=context)
        text = generate_text(prompt, api_key=dash_scope_api_key)
        print(text)
