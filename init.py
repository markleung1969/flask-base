#! /usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import logging
from config import settings
from flask import Flask, Blueprint, request, json
from werkzeug.contrib.cache import RedisCache
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
import wtforms_json


app = Flask(__name__)
app.config.from_object(settings)

db = SQLAlchemy(app, session_options=settings.SESSION_OPTIONS)

# redis配置
cache = RedisCache(host=settings.REDIS['host'], port=settings.REDIS['port'], db=settings.REDIS['db'])

wtforms_json.init()

# 开进程发邮件
mail = Mail(app)
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg);

# 蓝图用于写接口前缀
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
item_bp = Blueprint('item', __name__, url_prefix='/api/item')

import apps.auth.views
import apps.item.views

# 注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(item_bp)
