#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project:Autotest
@File   :__init__.py.py
@IDE    :PyCharm
@Author :Mefine
@Date   :2024/9/26 20:15
'''

from flask_sqlalchemy import SQLAlchemy
from app import At

db = SQLAlchemy(At)
At.app_context().push()