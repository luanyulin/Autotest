#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project:Autotest
@File   :user.py
@IDE    :PyCharm
@Author :Mefine
@Date   :2024/9/26 20:17
'''
from email.policy import default

from app.models import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.INT, primary_key=True)
    username = db.Column(db.String(16), unique=True, index=True)
    name = db.Column(db.String(16), index=True)
    password = db.Column(db.String(32), unique=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    role = db.Column(db.INT, default=0, comment='0: 普通用户 1:组长 2:超级管理员')
    create_at = db.Column(db.DATETIME, nullable=False)
    update_at = db.Column(db.DATETIME, nullable=False)
    deleted_at = db.Column(db.DATETIME)
    last_login_at = db.Column(db.DATETIME)

    def __init__(self,username,name,password,email):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.create_at = datetime.now()
        self.update_at = datetime.now()
        self.role = 0

    def __repr__(self):
        return '<User %r>' % self.username