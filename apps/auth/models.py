#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import session, json
from datetime import datetime, timedelta
from utils.base.base import random_str
from utils.base.auth import auth_required, get_password
from init import db
from utils.base.auth import get_password

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.Integer)
    username = db.Column(db.String(16))
    email = db.Column(db.String(32))
    password = db.Column(db.String(40))
    salt = db.Column(db.String(32))
    status = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)

    STATUS_INFO = {
        1 : '正常',
        2 : '停用',
    }
    
    GROUP_INFO = {
        1 : '普通用户',
        2 : '管理员',
    }

    def __init__(self, username, email, raw_password, status=1, group=1):
        self.username = username
        self.email = email
        self.status = status
        self.group = group
        self.create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        salt = random_str()
        self.salt = salt
        self.password = get_password(raw_password, salt) 

    def valid_password(self, raw_password):
        """
        验证用户密码
        """
        return self.password == get_password(raw_password, self.salt)

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'email' : self.email,
            'username' : self.username,
            'status' : self.status,
            'group' : self.group,
            'create_time' : self.create_time,
        }

    def __repr__(self):
        return "<User %s>"%self.email
