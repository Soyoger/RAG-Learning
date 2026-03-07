#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/3/1 21:39
# @Author  : yongjie.su
# @File    : 2.Qwen2.5-VL模型权重下载.py
# @Software: PyCharm
# pip install modelscope
# modelscope download --model="Qwen/Qwen2.5-VL-7B-Instruct" --local_dir ./model-dir
from modelscope import snapshot_download

model_dir = snapshot_download("Qwen/Qwen2.5-VL-7B-Instruct", local_dir="model-dir")
