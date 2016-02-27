#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, session, jsonify
from datetime import datetime
from apps.auth.models import User
from utils.error.error import AdError, catch_err
from utils.base.base import random_str
from utils.base.auth import auth_required, get_password
from apps.auth.form import LoginForm, RegisterForm
from init import app, db
from init import auth_bp as bp

# 用户登陆接口
@bp.route('/login', methods=['POST'])
@catch_err
def login():

    request_data = request.get_json()

    # 表单验证
    form = LoginForm.from_json(request_data)
    if not form.validate():
        raise AdError(-2000)

    email = request_data['email']
    password = request_data['password']

    user = User.query.filter_by(email = email).first()
    if user is None:
        raise AdError(-1000)
    if not user.valid_password(password):
        raise AdError(-1001)
    if user.status == 2:
        raise AdError(-1004)

    session["user_id"] = int(user.id)
    session["email"] = user.email
    session["username"] = user.username
    session["group"] = user.group
    session["status"] = user.status

    resp = {
        'c' : 0,
        'm' : '登陆成功',
        'd' : {
            'user_id' : user.id,
            'email' : user.email,
            'username' : user.username,
            'group' : user.group,
            'status' : user.status
        }
    }
    return jsonify(resp)

# get
# /logout
@bp.route('/logout', methods=['GET'])
@auth_required()
@catch_err
def logout():
    session.clear()
    resp = {
        'c' : 0,
        'm' : '退出成功',
        'd' : {}
    }
    return jsonify(resp)

# post
# /register
@bp.route('/register', methods=['POST'])
@catch_err
def register():

    request_data = request.get_json()

    # 表单验证
    form = RegisterForm.from_json(request_data)
    if not form.validate():
        raise AdError(-2000)

    username = request_data['username']
    email = request_data['email']
    raw_password = request_data['password']
    confirm_password = request_data['confirm_password']

    if raw_password != confirm_password:
        raise AdError(-1003)

    if User.query.filter_by(email = email).first():
        raise AdError(-1002)

    user = User(username, email, raw_password)
    db.session.add(user)
    db.session.commit()

    resp = {
        'c' : 0,
        'm' : '注册成功',
        'd' : {},
    }
    return jsonify(resp)

# GET
# /getUserInfo
@bp.route('/getAuthInfo', methods=['GET'])
@auth_required()
@catch_err
def auth_get_info():

    user_id = session.get('user_id')
    username = session.get('username')
    email = session.get('email')
    status = session.get('status')
    group = session.get('group')

    resp = {
        'c' : 0,
        'm' : '登陆成功',
        'd' : {
            'user_id' : user_id,
            'email' : email,
            'username' : username,
            'group' : group,
            'status' : status,
        }
    }
    return jsonify(resp)

# get
# /test
@app.route('/test', methods=['GET'])
@catch_err
def test_api():
    resp = {
        'c' : 0,
        'm' : 'dont go gentle into that night',
        'd' : {}
    }
    return jsonify(resp)
