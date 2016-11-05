# -*- coding: UTF-8 -*-

# Oct 31st, 2016


# 不推荐使用type进行变量类型检查

# 0. types
import types

def _type(element):
    _e_type = type(element)
    if _e_type is types.ListType:
        return 'List'
    elif _e_type is types.BooleanType:
        return 'Boolean'
    elif _e_type is types.StringType:
        return 'String'
    elif _e_type is types.DictType:
        return 'Dict'
    else:
        return 'other'

print _type([1])

# 1. 基于内建类型扩展的用户自定义类型，type函数不能返回正确结果
import types
class UserInt(int):
    def __init__(self, val=0):
        self._val = int(val)
    def __add__(self, val):
        if isinstance(val, UserInt):
            return UserInt(self._val + val._val)
        return self._val + val
    def __iadd__(self, val):
        raise NotImplementedError("not support operation")
    def __str__(self):
        return str(self._val)
    def __repr__(self):
        return 'Integer(%s)' % self._val

n = UserInt()
print n
# 0
m = UserInt(2)
print m
# 2
print n + m
# 2
print type(n) is types.IntType
# False
# 改为如下形式可以返回正确结果
print isinstance(n, int)
# True


# 2. 古典类中，所有类的实例都相等
class A:
    pass
a = A()

class B:
    sb = 0
    pass
b = B()
print type(a) is type(b)
# True
print type(a)
# <type 'isinstance'>
