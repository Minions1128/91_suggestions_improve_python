# -*- coding: UTF-8 -*-

# Nov 3rd, 2016


# enumerate的使用

li = ['a', 'b', 'c', 'd', 'e']
for i, e in enumerate(li):
    print 'index', i, 'element', e
# 其功能等同于
# for i, e in zip(range(len(li)), li):
#     print 'index', i, 'element', e

# 其不适合在函数、字典当中使用：
person_info = {
    'name':'Jon',
    'age':'20',
    'hobby':'football'
}
for k, v in enumerate(person_info):
    print k, v
# 字典使用的是iteritems方法
for k, v in person_info.iteritems():
    print k, v