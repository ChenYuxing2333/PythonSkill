#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 20:50
# @Author  : Jason Chan
# @Site    : 
# @File    : 08_类.py
# @Software: PyCharm

class Student(object):
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count += 1

