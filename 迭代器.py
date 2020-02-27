#coding:utf-8

import os
import sys


# 生成器都是迭代器，迭代器不一定是生成器

l = [1,2,3,4,5]   #可迭代对象，不是迭代器

d = iter(l)      # l.__iter__()

print(d)   #<listiterator object at 0x0000000004DA5518>

#什么是迭代器？
#满足两个条件 1、有iter()方法  2、有next()方法

# for 循环内部三件事：
# 1、 调用可迭代对象的iter方法返回一个迭代器对象
# 2、 不断调用迭代器对象的next方法
# 3、 处理StopIteration

# Iterator 迭代器
# Iterable 可迭代对象

