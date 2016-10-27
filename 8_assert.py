# -*- coding: UTF-8 -*-

# Oct 27th, 2016

""" assert:
    可以使用python -O 来忽略assert"""
x = 1
y = 2
assert x == y, 'NOT EQUAL'
# 此代码实际执行：
if __debug__ and not x == y:
    raise AssertionError('NOT EQUAL')