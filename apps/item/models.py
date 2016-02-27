#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import session, json
from init import cache, db

class Item(db.Model):

    __tablename__='items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    description = db.Column(db.String(256))

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    @property
    def serialize(self):
        resp = {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
        }
        return resp

    def __repr__(self):
        return "<Item %s>"%self.name

