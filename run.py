#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project:Autotest
@File   :run.py
@IDE    :PyCharm
@Author :Mefine
@Date   :2024/9/25 14:07
'''
from datetime import datetime

from app import At
from app.utils.logger import Log
from app import dao
from app.controllers.auth.user import auth

# 注册蓝图
At.register_blueprint(auth)

@At.route('/')
def hello_world():
    log = Log('hello world专用')
    log.info('有人访问了该网站')
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now)
    return now

if __name__ == '__main__':
    At.run("0.0.0.0",threaded=True, port="7777")