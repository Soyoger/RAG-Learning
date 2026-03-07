#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/10/25 11:26
# @Author  : yongjie.su
# @File    : 4.1.1  源数据清洗.py
# @Software: PyCharm
import hashlib


def get_md5(data: str):
    """
    计算hash值
    :param data: 文本内容
    :return:
    """
    if not data:
        return None
    return hashlib.md5(data.encode('utf8')).hexdigest()


if __name__ == '__main__':
    print(get_md5("测试内容"))
