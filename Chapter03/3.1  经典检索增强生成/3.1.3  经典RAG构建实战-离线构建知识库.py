#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/25 23:23
# @Author  : yongjie.su
# @File    : 3.1.3  经典RAG构建实战-离线构建知识库.py
# @Software: PyCharm
import pypdfium2
from typing import List
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS


def parse_pdf_file(file_name):
    docs = []
    pdf_reader = pypdfium2.PdfDocument(file_name, autoclose=True)
    try:
        for page_number, page in enumerate(pdf_reader):
            text_page = page.get_textpage()
            content = text_page.get_text_range()
            text_page.close()
            page.close()
            metadata = {"file_name": file_name, "page": page_number}
            doc = Document(page_content=content, metadata=metadata)
            docs.append(doc)
    finally:
        pdf_reader.close()
    return docs


def docs_splitter(docs: List[Document]):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=256,
        chunk_overlap=20,
        length_function=len,
    )

    split_docs = text_splitter.split_documents(docs)
    return split_docs


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


def persist_vec_db(docs, embedding, db_path="vec.db"):
    """
    使用通义千问批量写向量数据库的时候，batch_size=6
    :param docs:
    :param embedding:
    :param db_path:
    :return:
    """
    # 步长
    foot = 6
    vec_db = None
    for idx in range(0, len(docs), foot):
        sub_docs = docs[idx:idx + foot]
        if idx == 0:
            vec_db = FAISS.from_documents(sub_docs, embedding)
        else:
            temp_vec_db = FAISS.from_documents(sub_docs, embedding)
            vec_db.merge_from(temp_vec_db)
    vec_db.save_local(db_path)


if __name__ == "__main__":
    file_name = "2024年AI大模型训练数据白皮书.pdf"
    dash_scope_api_key = "sk-3a30xxx"
    # pdf 文件解析
    docs = parse_pdf_file(file_name)
    # 文档分块
    split_docs = docs_splitter(docs)
    # 词嵌入模型
    embedding = get_embedding_model(dash_scope_api_key)
    # 文档保存向量数据库
    persist_vec_db(split_docs, embedding, db_path="vec.db")
