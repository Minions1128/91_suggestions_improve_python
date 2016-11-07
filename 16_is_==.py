# -*- coding: UTF-8 -*-

# Nov 4th, 2016


""" is vs. ==
    is 表示对象实体, id()==id()
    == 表示相等"""
a1 = "Hi"
b1 = "Hi"
print a1 == b1, a1 is b1

a2 = "I am using long string for testing"
b2 = "I am using long string for testing"
print a2 == b2, a2 is b2
# 使用逐行输入解释的方式结果为True False

a3 = "string"
b3 = "".join(['s', 't', 'r', 'i', 'n', 'g'])
print a3 == b3, a3 is b3
