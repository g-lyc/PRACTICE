# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 常规
# 缺点：比较乱
record='....................100.......513.25444..........'
cost=int(record[20:23])*float(record[31:37])
#print(cost)

# 命名
# 比较规范，便于处理
SHARES=slice(20,23)
PRICE=slice(31,37)
cost=int(record[SHARES])*float(record[PRICE])
print(cost)


# 切片命名属性
a=slice(5,50,2)
a.start
a.stop
a.step

s='HelloWorld'
#自动收缩范围
a.indices(len(s))
#(5,10,2)
for i in range(*a.indices(len(s))):
    print(s[i])