# -*- coding: UTF-8 -*-

# Oct 22nd, 2016

""" 缩进与{}
    建议使用4个空格"""


""" '与"
    '表示一个字符，它实际对应于编译器字符集的一个整数值
    'a'对应97
    "表示字符串，默认以'\0'结尾
    除了上述之外，Python中没有明显的区别"""
print 'He said, "Hello!"'
print "He said, \"Hello!\""


# 三元操作符" ? : "
x = 0
y = -2
print x if x<y else y


# Python中没有switch...case，可以用以下形式代替：
n = 012
if n == 0:
    print 'n is 0'
elif n == 1:
    print 'n is 1'
elif n == 2:
    print 'n is 2'
else:
    print 'n is other number.'
# 或者使用以下方法
def f():
    return {
        0:'n is 0',
        1:'n is 1',
        2:'n is 2',
    }.get(n, 'n is other number.')
print f()
