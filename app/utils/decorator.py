#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project:Autotest
@File   :decorator.py
@IDE    :PyCharm
@Author :Mefine
@Date   :2024/9/25 14:35
'''

"""
    这是一个装饰器方法文件
"""

class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance