# -*- coding: UTF-8 -*-

# Oct 28th, 2016

""" 不要使用中间变量交换数据"""


x = 1
y = 2

x, y = y, x
print x, y

""" Python执行顺序：
    1. 创建元组(y, x)，标识符和值分别对应
    2. 由元组的形式进行赋值
    * 可以通过dis模块来进行分析"""

import dis

def swap1():
    x = 2
    y = 3
    x, y = y, x

def swap2():
    x = 2
    y = 3
    temp = x
    x = y
    y = temp

print dis.dis(swap1)
print '------------------------------'
print dis.dis(swap2)
