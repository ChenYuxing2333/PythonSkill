#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 19:32
# @Author  : Jason Chan
# @Site    : 
# @File    : 07_高阶函数.py
# @Software: PyCharm
# 在 Python3 中，reduce() 函数已经被从全局名字空间里移除了，它现在被放置在 fucntools 模块里，如果想要使用它，则需要通过引入 functools 模块来调用 reduce() 函数
from functools import reduce
def prod(x, y):
    return x * y
print(reduce(prod, [1, 3, 5, 7, 9]))
# 闭包
# 内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）
# python中的闭包从表现形式上定义（解释）为：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure).