#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/3/2 11:37
# @Author  : yongjie.su
# @File    : 2.中文CLIP动手实践.py
# @Software: PyCharm
import torch
from modelscope.utils.constant import Tasks
from modelscope.pipelines import pipeline
from modelscope.preprocessors.image import load_image

# 载入base规模CLIP模型
pipeline = pipeline(
    task=Tasks.multi_modal_embedding,
    model='damo/multi-modal_clip-vit-base-patch16_zh'
)
# 准备文本query和多张候选图片
input_text = "过年喜庆对联"
input_imgs = [
    load_image('https://yangan2.oss-cn-beijing.aliyuncs.com/过年对联.jpeg'),
    # 支持示例图片url/本地图片路径 返回PIL.Image
    load_image('https://yangan2.oss-cn-beijing.aliyuncs.com/圣诞装饰.png'),
    load_image('https://yangan2.oss-cn-beijing.aliyuncs.com/过年喜庆.jpeg'),
    load_image('https://yangan2.oss-cn-beijing.aliyuncs.com/对联.jpeg')
]

# 提取图片特征，支持一张图片(PIL.Image)或多张图片(List[PIL.Image])输入，输出归一化特征向量
img_embedding = pipeline.forward({'img': input_imgs})['img_embedding']  # 2D Tensor, [图片数, 特征维度]

# 提取文本特征，支持一条文本(str)或多条文本(List[str])输入，输出归一化特征向量
text_embedding = pipeline.forward({'text': input_text})['text_embedding']  # 2D Tensor, [文本数, 特征维度]

# 计算图文相似度
with torch.no_grad():
    # 计算内积得到logit，考虑模型temperature（0.01）
    logits_per_text = (text_embedding / pipeline.model.temperature) @ img_embedding.t()
    # 根据logit计算概率分布
    probs = logits_per_text.softmax(dim=-1).cpu().numpy()

# 打印结果
print("图文相似概率分布:", probs.tolist())
