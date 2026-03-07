#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/30 10:16
# @Author  : yongjie.su
# @File    : ocr_demo.py
# @Software: PyCharm
from rapidocr_onnxruntime import RapidOCR

img = "../example_data/ocr_demo.png"
ocr = RapidOCR()
text = ""
result, _ = ocr(img)
if result:
    result = [text[1] for text in result]
    text += "\n".join(result)
print(text)