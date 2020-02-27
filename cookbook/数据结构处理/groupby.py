# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

rows=[
{'address':'5412NCLARK','date':'07/01/2012'},
{'address':'5148NCLARK','date':'07/04/2012'},
{'address':'5800E58TH','date':'07/02/2012'},
{'address':'2122NCLARK','date':'07/03/2012'},
{'address':'5645NRAVENSWOOD','date':'07/02/2012'},
{'address':'1060WADDISON','date':'07/02/2012'},
{'address':'4801NBROADWAY','date':'07/01/2012'},
{'address':'1039WGRANVILLE','date':'07/04/2012'},
]

from operator import itemgetter
from itertools import groupby


#Sort by the desired field first
#缺点：事先需要排序
rows.sort(key=itemgetter('date'))
#Iterate in groups
for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)

#此方法不需要事先排序，占用内存稍微大一些
from collections import defaultdict
rows_by_date=defaultdict(list)
print('*'*20)
print(rows_by_date)
print('*'*20)
for row in rows:
    rows_by_date[row['date']].append(row)

print('*'*20)
print(rows_by_date)
print('*'*20)

#对指定日期访问
for r in rows_by_date['07/01/2012']:
    print(r)

