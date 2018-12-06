# -*- coding: utf-8 -*-

import hashlib
from flask import request, session, jsonify, make_response
from utils.error.error import MkError
from functools import wraps

def get_password(raw_password, salt):
    return hashlib.sha1(raw_password + salt).hexdigest()

def make_unauth_response():
    e = MkError(-5002) 
    re = {
        'c' : e.code,
        'm' : e.msg,
        'd' : e.payload,
    }
    return jsonify(re)

def auth_required():
    """
    检查用户权限装饰器
    permission_code 为空时 只检查是否登陆
    role_group 为1时 拥有全部权限
    """
    def _auth_required(old_handler):
        @wraps(old_handler)
        def new_handler(*args, **kwargs):
            user_id = session.get('user_id')
            if not user_id:
                e = MkError(-5003) 
                re = {
                    'c' : e.code,
                    'm' : e.msg,
                    'd' : e.payload,
                }
                return jsonify(re)
            return old_handler(*args, **kwargs)
        return new_handler
    return _auth_required
