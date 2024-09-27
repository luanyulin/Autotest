#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project:Autotest
@File   :config.py
@IDE    :PyCharm
@Author :Mefine
@Date   :2024/9/25 14:17
'''
import os

class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs','Autotest.log')
    JSON_AS_ASCII = False   # Flask jsonify编码问题

    # MYSQL连接信息
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PWD = 'root123'
    DBNAME = 'autotest'

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = ('mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
                               MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME))

    SQLALCHEMY_TRACK_MODIFICATIONS = False