#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
全局方法
"""
import random
from flask import jsonify
from functools import wraps

def random_str(length=32):
    str = ''
    seed = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    seed_length = len(seed)
    for i in range(length):
        str += seed[random.randint(0, seed_length-1)]
    return str

def get_request_params(params):
    """
    获取queryparams
    自动去除无值参数
    """
    formatted = {}
    for k, v in params.items():
        if v:
            formatted[k] = v
    return formatted

