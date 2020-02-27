# -*- coding: UTF-8 -*-
a=['bob','about','Zoo','Credit']
#list_of_string=string.split()
#print '*'*50

def f(liststring):
    listtemp=[(x.lower(),x) for x in liststring]#将字符串列表生成元组
    listtemp.sort()
    return [x[1] for x in listtemp]#排序完成后返回原来的字符串
print f(a)


#print sorted(a,key=str.lower)
