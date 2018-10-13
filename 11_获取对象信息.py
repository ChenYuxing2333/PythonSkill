#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 23:03
# @Author  : Jason Chan
# @Site    : 
# @File    : 11_获取对象信息.py
# @Software: PyCharm

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
hasattr(obj,'x')
hasattr(obj,'y')
setattr(obj,'y',19)
hasattr(obj,'y')
getattr(obj,'y')
