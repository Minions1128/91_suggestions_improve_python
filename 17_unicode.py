# -*- coding: UTF-8 -*-

# Nov 5th, 2016


strUnicode = u"unicode 字符串"
    # 前加u标识Unicode
print strUnicode, type(strUnicode)


# 编码遇到的问题：

# 1. 读取有中文的文件会出现乱码
file_headle = open("temp.py", 'r')
print file_headle.read()
file_headle.close()
# 加入decode和encode方法。
# str.encode([编码参数 [, 错误处理]])
# str.decode([编码参数 [, 错误处理]])
# 错误处理有3中方式：
# 1. strict：默认处理方式，抛出UnicodeError
# 2. ignore：忽略
# 3. replace：将不可转换字符用？代替
file_headle = open("temp.py", 'r')
print file_headle.read().decode(
    "utf-8").encode("gbk")
file_headle.close()


# 2. 包含中文会抛出异常
s = "python 中文测试"
print s
# 用以下编码声明
# coding=<>
# -*- coding:<>
# vim: set fileencoding=<>


# 3. 普通字符和Unicode进行字符串连接的时候
s = "中文测试" + u"Chinese Test"
# 将其统一为一种编码方式
s = "中文测试".decode('gbk') + u"Chinese Test"
s = "中文测试" + u"Chinese Test".encode("utf-8")
print s
