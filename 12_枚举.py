#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 23:23
# @Author  : Jason Chan
# @Site    : 
# @File    : 12_枚举.py
# @Software: PyCharm

from enum import Enum,unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def init(self, name, gender):
        self.name = name
        if isinstance(gender,Gender):
            self.gender = gender
        else:
            raise TypeError('类型错误')
s = Student('Jason',Gender.Male)
print(s.name,s.gender)
# 为啥运行不出来啊