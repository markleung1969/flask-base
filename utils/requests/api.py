#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    封装adcloud接口请求以及处理
    POST和PUT以JSON字符串的形式请求接口
    结果以dict形式返回
"""
import requests
from flask import json 
from utils.error.error import AdError

def post(api_addr, data={}):
    resp = requests.post(api_addr, json=data)
    resp = resp.json()
    if resp['c'] != 0:
        raise AdError(-5001)
    return resp

def put(api_addr, data={}):
    resp = requests.put(api_addr, json=data)
    resp = resp.json()
    if resp['c'] != 0:
        raise AdError(-5001)
    return resp

def get(api_addr, data={}):
    resp = requests.get(api_addr, params=data)
    resp = resp.json()
    if resp['c'] != 0:
        raise AdError(-5001)
    return resp
