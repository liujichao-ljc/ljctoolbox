#!/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2019 TehFront inc. All rights reserved.
文件名称：timebox.py
创 建 者：liujichao.ljc
邮    箱：liujichao.ljc@qq.com
创建日期：2019/12/24 15:14 
"""

import time


def early_time(t):
    remain = int(t) % 86400
    remain_section = remain - 16 * 3600
    return int(t) - remain_section if remain_section >= 0 else int(t) - remain - 8 * 3600


def begin_of_day(t):
    """返回一天的凌晨"""
    return early_time(t)


def end_of_day(t):
    """返回一天的最后一刻时间"""
    return early_time(t) + + 24*3600 - 1


def from_unix_stamp(t, format="%Y%m%d"):
    """给定时戳，获取日期"""
    return time.strftime(format, time.localtime(t)) if t is not None else t


def to_unix_stamp(s, format="%Y-%m-%d %H:%M:%S"):
    """把字符串转换成时戳"""
    return int(time.mktime(time.strptime(s, format))) if s is not None and len(s) > 0 else s
