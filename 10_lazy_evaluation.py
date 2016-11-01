# -*- coding: UTF-8 -*-

# Oct 29th, 2016

 # Lazy Evaluation（惰性计算）

"""1. 避免必要的计算
    if x and y时，如果x为False，y没必要计算
    if x or y是，若x为True，y没必要计算
    * 以下举例，使用注释的if会更快"""
from time import time
t = time()
abbr = ['cf.', 'e.g.', 'ex.', 'etc.', 'fig.', 
    'i.e.', 'Mr.', 'vs.']
for i in range(1000000):
    for w in ('Mr.', 'Hat', 'is', 'chasing', 'the'
            , 'black', 'cat', '.'):
        if w in abbr:
        # if w[-1] == '.' and w in abbr:
            pass
print 'total run time:'
print time()-t
