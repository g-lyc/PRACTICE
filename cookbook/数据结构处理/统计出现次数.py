# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

words=[
'look','into','my','eyes','look','into','my','eyes',
'the','eyes','the','eyes','the','eyes','not','around','the',
'eyes',"don't",'look','around','the','eyes','look','into',
'my','eyes',"you're",'under'
]
from collections import Counter
word_counts=Counter(words)
#出现频率最高的3个单词
top_three=word_counts.most_common(3)
print(top_three)
#Outputs[('eyes',8),('the',5),('look',4)]


# Counter的结果可以加减运算
a=Counter(words)
b=Counter(morewords)
a
Counter({'eyes':8,'the':5,'look':4,'into':3,'my':3,'around':2,
"you're":1,"don't":1,'under':1,'not':1})
b
Counter({'eyes':1,'looking':1,'are':1,'in':1,'not':1,'you':1,
'my':1,'why':1})
#Combinecounts
c=a+b
c
Counter({'eyes':9,'the':5,'look':4,'my':4,'into':3,'not':2,
'around':2,"you're":1,"don't":1,'in':1,'why':1,
'looking':1,'are':1,'under':1,'you':1})
