#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, session, jsonify
from utils.error.error import AdError, catch_err
from utils.base.auth import auth_required
from utils.base.base import get_request_params
from apps.item.form import EditItemForm
from apps.item.models import Item
from init import cache, db, item_bp as bp

# PUT
# 新建item
@bp.route('/item', methods=['PUT'])
@auth_required()
@catch_err
def add_item():

    request_data = request.get_json()

    # 数据验证
    form = EditItemForm.from_json(request_data)
    if not form.validate():
        raise AdError(-2000)

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
