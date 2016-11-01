# -*- coding: UTF-8 -*-

# Oct 27th, 2016

""" assert:
    可以使用python -O 来忽略assert
    使用assert的一些规则：
    1. 不要滥用
    2. 要先使用Python自身的异常处理
    3. 不要使用assert来判断用户输入的内容
    4. 函数调用后，返回值可以使用assert
    5. 如果后续业务逻辑继续下去的先决条件可以使用assert"""

x = 1
y = 2
assert x == y, 'NOT EQUAL'
# 此代码实际执行：
if __debug__ and not x == y:
    raise AssertionError('NOT EQUAL')
