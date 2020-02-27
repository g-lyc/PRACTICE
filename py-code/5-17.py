# -*- coding: UTF-8 -*-

import random
num = random.randint(1,100)
lst=[]
for item in range(num):
    tmp = random.randint(0,(pow(2,31)-1))
    lst.append(tmp)
lst.sort()
print lst
