#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project:Autotest
@File   :__init__.py.py
@IDE    :PyCharm
@Author :Mefine
@Date   :2024/9/26 20:31
'''

from app.models import db
from app.models.user import User

db.create_all()