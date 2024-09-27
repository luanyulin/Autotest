#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project:Autotest
@File   :logger.py
@IDE    :PyCharm
@Author :Mefine
@Date   :2024/9/25 14:25
'''
import sys

import logbook
from app import At
from .decorator import SingletonDecorator

@SingletonDecorator
class Log(object):
    handler = None

    def __init__(self, name='Autotest', filename=At.config['LOG_NAME']):
        """
        :param name:业务名称
        :param filename:文件名称
        """
        self.handler = logbook.FileHandler(filename=filename, encoding='utf-8')
        logbook.set_datetime_format('local')
        self.logger = logbook.Logger(name)
        self.handler.push_application()

    def info(self, *args, **kwargs):
        return self.logger.info(*args, **kwargs)

    def debug(self, *args, **kwargs):
        return self.logger.debug(*args, **kwargs)

    def warning(self, *args, **kwargs):
        return self.logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        return self.logger.error(*args, **kwargs)
