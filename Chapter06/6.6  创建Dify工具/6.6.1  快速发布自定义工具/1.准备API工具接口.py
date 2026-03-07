#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/12/8 22:59
# @Author  : yongjie.su
# @File    : 1.准备API工具接口.py
# @Software: PyCharm
from flask import Flask, request, jsonify

app = Flask(__name__)

# 共享密钥
SECRET_KEY = "5tf6B4chG9ueQf1t"


def get_mock_answer(question: str):
    # 简单的逻辑示例：根据问题mock生成回答
    if not question:
        answer = "请提供一个问题。"
    else:
        answer = f"这是mock答案。"
    return answer


@app.route('/get/answer', methods=['GET'])
def get_answer():
    # 校验密钥
    secret = request.args.get('secret', default='', type=str)
    if secret != SECRET_KEY:
        # 返回 401 Unauthorized 错误
        return jsonify({
            "error": "Unauthorized access. Invalid secret key."
        }), 401

    # 获取问题
    question = request.args.get('question', default='', type=str)
    answer = get_mock_answer(question)
    # 返回 JSON 响应
    return jsonify({
        "question": question,
        "answer": answer
    })


if __name__ == '__main__':
    app.run(debug=True)
