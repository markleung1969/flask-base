#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms import Form, TextField, PasswordField, validators

class RegisterForm(Form):
    """
    用户注册表单验证
    """
    email = TextField('登陆邮箱', [
        validators.Email(message='请输入正确的邮箱地址')
    ])
    username = TextField('用户名', [
        validators.Length(min=2, max=20, message='请输入合法的用户名'),
    ])
    password = PasswordField('密码', [
        validators.Length(min=6, max=20, message='密码长度为6至20个字符'),
    ])
    confirm_password = PasswordField('确认密码', [
        validators.Length(min=6, max=20, message='密码长度为6至20个字符'),
    ])

class LoginForm(Form):
    email = TextField('登陆邮箱', [
        validators.Email(message='请输入正确的邮箱地址')
    ])
    password = PasswordField('密码', [
        validators.Length(min=6, max=20, message='密码长度为6至20个字符'),
    ])
