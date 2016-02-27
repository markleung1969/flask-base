#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import config.setting
from utils.error.error_code import ERR
from flask import request, jsonify, make_response, json
from functools import wraps

class AdError(Exception):

    def __init__(self, err_code, payload={}):
        Exception.__init__(self)
        self.code = err_code
        self.msg = ERR[err_code]
        self.payload = payload

def catch_err(old_handler):
    """
    捕获接口错误信息 
    处理接口请求的log
    """
    @wraps(old_handler)
    def new_handler(*args, **kwargs):
        logger = logging.getLogger('adgear-dashboard')
        try:
            return old_handler(*args, **kwargs)
        except AdError as e:
            re = {
                'c' : e.code,
                'm' : e.msg,
                'd' : e.payload,
            }
            return jsonify(re)
        except Exception as e:
            re = make_response(jsonify({'c': -5000, 'm':'内部错误'}), 500)
            return re
    return new_handler
