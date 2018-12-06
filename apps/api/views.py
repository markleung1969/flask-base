# -*- coding: utf-8 -*-

from flask import request, session, jsonify
from utils.error.error import MkError, catch_err
from utils.base.auth import auth_required
from utils.base.base import get_request_params
from app import cache, db, app

@app.route('/test', methods=['GET'])
@catch_err
def test_api():
    resp = {
        'c' : 0,
        'm' : 'dont go gentle into that night',
        'd' : {}
    }
    return jsonify(resp)

# 登陆接口
"""
@bp.route('/register', methods=['POST'])
@catch_err
def register():
    request_data = request.get_json()

    # 表单验证
    form = RegisterForm.from_json(request_data)
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



# 登陆接口
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

# POST
# 新建item
@app.route('api/item', methods=['POST'])
@auth_required()
@catch_err
def add_item():

    request_data = request.get_json()

    # 数据验证
    form = EditItemForm.from_json(request_data)
    if not form.validate():
        raise MkError(-2000)

    item = Item(name=request_data['name'],
            description=request_data['description'])

    db.session.add(item)
    db.session.commit()

    resp = {
        'c' : 0,
        'm' : 'ok',
        'd' : {},
    }
    return jsonify(resp)

# POST
# 修改item
@bp.route('/item/<id>', methods=['POST'])
@auth_required()
@catch_err
def edit_item(id):

    request_data = request.get_json()

    # 数据验证
    form = EditItemForm.from_json(request_data)
    if not form.validate():
        raise AdError(-2000)

    item = Item.query.filter_by(id=id).first()
    if not item:
        raise AdError(-3000)

    item.name = request_data['name']
    item.description = request_data['description']

    db.session.add(item)
    db.session.commit()

    resp = {
        'c' : 0,
        'm' : 'ok',
        'd' : {},
    }
    return jsonify(resp)

# GET 
# 通过id获取item信息
@bp.route('/item/<id>', methods=['GET'])
@auth_required()
@catch_err
def get_item_info(id):
    item = Item.query.filter_by(id=id).first()
    if not item:
        raise AdError(-3001)
    resp = {
        'c' : 0,
        'm' : 'ok',
        'd' : item.serialize,
    }
    return jsonify(resp)

# GET
# 获取app列表
# @todo 暂时没有加上请求参数
@bp.route('/item', methods=['GET'])
@auth_required()
@catch_err
def get_list():

    items = Item.query.all()

    results= [x.serialize for x in items]

    resp = {
        'c' : 0,
        'm' : 'ok',
        'd' : results,
    }
    return jsonify(resp)
"""
