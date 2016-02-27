#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from flask import request, session, jsonify, make_response
from functools import wraps
from init import db

def get_password(raw_password, salt):
    return hashlib.sha1(raw_password + salt).hexdigest()

def make_unauth_response():
    re = make_response(jsonify({'c':1, 'm': '没有权限','d':{}}), 403)
    return re

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
                re = make_response(jsonify({'c': 1, 'm': '没有登陆','d':{}}), 401)
                return re
            return old_handler(*args, **kwargs)
        return new_handler
    return _auth_required
