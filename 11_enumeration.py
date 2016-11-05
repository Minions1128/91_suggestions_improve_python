# -*- coding: UTF-8 -*-

# Oct 30th, 2016


# 1. 使用类属性
class Seasons:
    Spring, Summer, Autumn, Winter = range(4)

# *枚举实现
class MyEnum:
    def __init__(self, a=None, b=None, c=None, d=None):
        self.x1 = a if a else 0
        self.x2 = b if b != None else self.x1 + 1
        self.x3 = c if c != None else self.x2 + 1
        self.x4 = d if d != None else self.x3 + 1
        self.output()

    def output(self):
        print self.x1, self.x2, self.x3, self.x4


a = MyEnum(b=0, c=222)

# 2. 借助函数
def enum(*args, **kwargs):
    return type("Enum", (object,), 
        dict(zip(args, range(len(args))), **kwargs))

one_season = enum("Spring", "Summer", "Autumn", Winter=1)
print one_season.Spring
