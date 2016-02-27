#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms import Form, TextField, PasswordField, validators

class EditItemForm(Form):
    name = TextField('名称', [
        validators.Required(),
        validators.Length(max=64)
    ])
    description = TextField('描述', [
        validators.Required(),
        validators.Length(max=128)
    ])
