#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2025/1/4 23:38
# @Author  : yongjie.su
# @File    : （1）上下文精度.py
# @Software: PyCharm
import numpy as np
from loguru import logger


def _calculate_average_precision(
) -> float:
    score = np.nan
    # verdict_list = [1 if ver.verdict else 0 for ver in verifications]
    verdict_list = [1, 1, 0, 1, 0]
    denominator = sum(verdict_list) + 1e-10

    precision_all_k = []
    for i in range(len(verdict_list)):
        precision_k = (sum(verdict_list[: i + 1]) / (i + 1)) * verdict_list[i]
        print(
            f"i={i}， "
            f"sum(verdict_list[: i + 1])={sum(verdict_list[: i + 1])}， "
            f"{sum(verdict_list[: i + 1])}/{(i + 1)} * {verdict_list[i]}={precision_k}")
        precision_all_k.append(precision_k)

    numerator = sum(precision_all_k)
    score = numerator / denominator
    print(f"score={numerator}/{denominator}={score}")
    if np.isnan(score):
        logger.warning(
            "Invalid response format. Expected a list of dictionaries with keys 'verdict'"
        )
    return score


_calculate_average_precision()
