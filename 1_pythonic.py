# -*- coding: UTF-8 -*-

# Oct 20th, 2016

""" Pythonic:
    充分提现python代码风格，其可读性高。以快速排序举例"""
def quick_sort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + [pivot] + quick_sort(greater)

print quick_sort([1, 3, 5, 2, 6, 4])


# swap
a = 1
b = 2
a, b = b, a


#遍历容器
alist = [1, 3, 5, 2, 6, 4]
for i in alist:
    print i


# 打开文件用with语句
with open(path, 'r') as f:
    do_sth_with(f)

# 逆置list或者str
a = [1, 2, 3, 4]
c = 'abcd'
print a[::-1]
print c[::-1]
print list(reversed(a))
print list(reversed(c))


# 基本输出方式
print 'Hello %s' % 'Tom'
print 'Hello %(name)s' % {'name':'Tom'}
value = {'language':'Python', 'greet':'Hello World'}
print '%(greet)s from %(language)s' % value
print '{greet} from {language}'.format(**value)
