#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project:Autotest
@File   :__init__.py.py
@IDE    :PyCharm
@Author :Mefine
@Date   :2024/9/25 14:06
'''

from flask import Flask
from flask_cors import CORS

from config import Config

At = Flask(__name__)
CORS(At, supports_credentials=True)

At.config.from_object(Config)