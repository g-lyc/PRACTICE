#coding:utf-8

import os
import sys

import hashlib

# 用来加密的模块

# 1、md5加密

m = hashlib.md5()

m.update('hello world'.encode('utf8'))

print(m.hexdigest())

#print(m)


#sha

m = hashlib.sha256()