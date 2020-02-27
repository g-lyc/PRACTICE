# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

rows=[
{'fname':'Brian','lname':'Jones','uid':1003},
{'fname':'David','lname':'Beazley','uid':1002},
{'fname':'John','lname':'Cleese','uid':1001},
{'fname':'Big','lname':'Jones','uid':1004}
]

from operator import itemgetter

# 按照单个key排序
rows_by_fname=sorted(rows,key=itemgetter('fname'))
rows_by_uid=sorted(rows,key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# 按照多个key排序
rows_by_lfname=sorted(rows,key=itemgetter('lname','fname'))
print(rows_by_lfname)

# 注：可以用lambda实现，但是itemgetter()方式会运行的稍微快点
