# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

a={'x':1,'z':3}
b={'y':2,'z':4}

from collections import ChainMap
c=ChainMap(a,b)
print(c['x'])#Outputs1(froma)
print(c['y'])#Outputs2(fromb)
print(c['z'])#Outputs3(froma)

# 合并过程：先从a中找，如果找不到再在b中找
# 些字典并不是真的合并在一起了，ChainMap类只是在内部创建了一个容纳这些字典的列表并重新定义了一些常见的字典操作来遍历这个列表
# 对于字典的更新或删除操作总是影响的是列表中第一个字典
