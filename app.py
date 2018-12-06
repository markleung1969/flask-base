# -*- coding: utf-8 -*-

from config import settings
from flask import Flask, request, json
import pymysql
import redis

app = Flask(__name__)
app.config.from_object(settings)

db = pymysql.connect(host=app.config['MYSQL']['host'],
                        port=app.config['MYSQL']['port'],
                        user=app.config['MYSQL']['user'],
                        password=app.config['MYSQL']['password'],
                        database=app.config['MYSQL']['database'])

pool = redis.ConnectionPool(host=app.config['REDIS']['host'],
                                    port=app.config['REDIS']['port'],
                                    db=app.config['REDIS']['db'])

cache = redis.Redis(connection_pool=pool) 

import apps.api.views
