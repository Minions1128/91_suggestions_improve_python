# -*- coding: UTF-8 -*-

# Nov 2nd, 2016

""" eval()
    eval(expression[, globals[, locals]])
    global为字典形式，
    locals为任何映射对象
    举例："""

a = 1
b = 10
c = 100
g = {'a':2, 'b':20}
l = {'b':30, 'c':300}
print eval("a+b+c", g, l)

# 但eval会产生安全漏洞
import sys
from math import *

def exp_calc_bot(user_func):
    try:
        print 'Your answer is', eval(user_func)
    except NameError:
        print "The expression your enter is not valid"

print 'Hi, I am exp_calc_bot. please input your expression or enter e to end'
inputstr = ''
while 1:
    print 'Please enter a number or operation. Enter e to complete.:'
    inputstr = raw_input()
    if inputstr == str('e'):
        sys.exit()
    elif repr(inputstr) != repr(''):
        exp_calc_bot(inputstr)
        inputstr = ''

# 输入__import__("os").system("dir")就会产安全问题
# 会将当前目录下的所有文件进行显示

# 指定global和local之后，可能会好一些
def exp_calc_bot(user_func):
    try:
        match_fun_list = ['acos', 'asin', 'atan',
            'cos', 'e', 'log', 'log10', 'pi', 'pow',
            'sin', 'sqrt', 'tan']
        match_fun_dict = dict([(k, globals().get(k))
            for k in match_fun_list])
        print 'Your answer is', eval(user_func,
            {"__builtins__":None}, match_fun_dict)
    except:
        print 'The expression your enter is not valid'

# 但依然无法抵挡如下输入，会将其程序退出
[c for c in ().__class__.__bases__[0].__subclasses__()
    if c.__name__=='Quitter'][0](0)()
# 因此，不要在输入对象是不信任的源的地方使用eval(),
# 可以使用较安全的ast.literal_eval代替
