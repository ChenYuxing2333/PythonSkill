#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 23:21
# @Author  : Jason Chan
# @Site    : 
# @File    : 09_模块.py
# @Software: PyCharm
#  待确认
# def __getattr__(name):
#     return 'Hello,%s' % name
#
# def __getattr__2(name):
#     return 'Hi,%s' % name
# def greeting(name):
#     if len(name) > 3:
#         return __getattr__(name)
#     else:
#         return __getattr__2(name)
# f2 = greeting(4444)