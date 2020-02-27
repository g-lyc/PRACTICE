#coding:utf-8

import os
import sys


# def fib(max):
#     n, a, b = 0, 0 , 1
#     while n < max:
#         print(b)
#         a, b = b, a+b    #先执行右边再赋值
#         n += 1
#
# fib(13)



#利用生成器来实现

def fib(max):
    n, a, b = 0, 0 , 1
    while n < max:
        #print(b)
        yield b
        a, b = b, a+b
        n += 1

print(fib(8))  #<generator object fib at 0x000000000622DEA0>


#生成器 send 方法

def bar():
    print('ok')
    count = yield 1

    print('ok1')
    yield 2

b = bar()

b.send(None)  #next(b)





