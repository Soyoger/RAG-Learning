#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/4 18:30
# @Author  : yongjie.su
# @File    : 5.4.3  实战RAGAS的评估.py
# @Software: PyCharm
# 第一步：从Hugging Face Datasets加载评估数据集。
from datasets import load_dataset

dataset = load_dataset(
    "explodinggradients/amnesty_qa",
    "english_v3",
    trust_remote_code=True
)
# 第二步：将数据集加载到Ragas EvaluationDataset对象中。
from ragas import EvaluationDataset

eval_dataset = EvaluationDataset.from_hf_dataset(dataset["eval"])
# 第三步：定义词嵌入模型。
from langchain_community.embeddings import HuggingFaceEmbeddings
from ragas.embeddings import LangchainEmbeddingsWrapper

model_name = "sentence-transformers/bge-large-zh-v1.5"

embeddings = HuggingFaceEmbeddings(model_name=model_name)
evaluator_embeddings = LangchainEmbeddingsWrapper(embeddings)

# 第四步：选择评估LLM。
from langchain_community.chat_models import ChatTongyi
from ragas.llms import LangchainLLMWrapper


def get_llm_instance(api_key=None, model="qwen-long", top_p=0.8, temperature=0.1):
    if api_key is None:
        raise ValueError("大模型api_key为空！")
    llm = ChatTongyi(
        dashscope_api_key=api_key,
        model=model,
        top_p=top_p,
        temperature=temperature
    )
    return llm


# 设置通义千问api_key
dash_scope_api_key = "sk-3a30xxx"
llm_instance = get_llm_instance(api_key=dash_scope_api_key)

evaluator_llm = LangchainLLMWrapper(llm_instance)
# 第五步：定义评估指标。
from ragas.metrics import LLMContextRecall, Faithfulness, FactualCorrectness, SemanticSimilarity

metrics = [
    LLMContextRecall(llm=evaluator_llm),
    FactualCorrectness(llm=evaluator_llm),
    Faithfulness(llm=evaluator_llm),
    SemanticSimilarity(embeddings=evaluator_embeddings)
]
# 第6步：执行评估
from ragas import evaluate
results = evaluate(dataset=eval_dataset, metrics=metrics)

# 第7步：保存并分析结果。
df = results.to_pandas()
df.to_csv("evaluate.csv", index=False, header=True)
print(df.head())
