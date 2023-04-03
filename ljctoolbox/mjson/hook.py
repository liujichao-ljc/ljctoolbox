#!/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2019 TehFront Inc. All rights reserved.
文件名称：hook.py
创 建 者：liujichao.ljc
邮    箱：liujichao.ljc@qq.com
创建日期：2020/1/2 16:14 
"""


def byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            byteify(key, ignore_dicts=True): byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data
