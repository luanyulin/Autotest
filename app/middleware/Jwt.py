#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project:Autotest
@File   :Jwt.py
@IDE    :PyCharm
@Author :Mefine
@Date   :2024/9/27 11:00
"""

import hashlib
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import ExpiredSignatureError

EXPIRED_HOUR = 3

class UserToken(object):
    key = 'AtToken'
    salt = 'At'

    @staticmethod
    def get_token(data):
        # 用户信息压缩成一串字符串，并附带3小时的过期时间
        new_data = dict({"exp":datetime.utcnow() + timedelta(hours=EXPIRED_HOUR)}, **data)
        # return jwt.encode(new_data, key=UserToken.key).decode('utf-8')
        return jwt.encode(new_data, key=UserToken.key)

    @staticmethod
    def parse_token(token):
        try:
            return jwt.decode(token, key=UserToken.key)
        except ExpiredSignatureError:
            raise Exception('token已过期，请重新登录')

    @staticmethod
    def add_salt(password):
        # 用md5码存储用户密码
        m = hashlib.md5()
        m.update(f'{password}{UserToken.salt}'.encode("utf-8"))
        return m.hexdigest()