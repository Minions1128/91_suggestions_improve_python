# -*- coding: UTF-8 -*-

# Nov 7th, 2016


""" 3种方式引入外部模块：
    1. import
    2. from import
    3. __import__

    优先使用import a.B
    有节制的使用from a import B的形式
    尽量避免使用from a import *的形式，
    容易污染命名空间，
    无法清晰的描述引入了哪几个对象。"""