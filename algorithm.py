#!/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2019 TehFront Inc. All rights reserved.
文件名称：algorithm.py
创 建 者：liujichao.ljc
邮    箱：liujichao.ljc@qq.com
创建日期：2019/12/6 17:10 
"""


def merge(intervals):
    """
    区间合并函数
    :param intervals:
    :return:
    """
    intervals.sort(key=lambda x: x.start)

    merged = []
    for interval in intervals:
        if not merged or merged[-1].end < interval.start:
            merged.append(interval)
        else:
            merged[-1].end = max(merged[-1].end, interval.end)

    return merged
