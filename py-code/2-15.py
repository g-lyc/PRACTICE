#coding:utf-8
#从小到大
num1 = int(raw_input('input num1:'))
num2 = int(raw_input('input num2:'))
num3 = int(raw_input('input num3:'))
if num1 > num2:
    tmp = num2
    num2 = num1
    num1 = tmp
if num2 > num3:
    tmp = num3
    num3 = num2
    num2 = tmp
if num1 > num2:
    tmp = num2
    num2 = num1
    num1 = tmp
print 'min to max is %d,%d,%d'%(num1,num2,num3)

#从大到小
print 'Enter three numbers:'
num1=int(raw_input())
num2=int(raw_input())
num3=int(raw_input())
if num1>num2>num3:
    print num1,num2,num3
elif num1>num3>num2:
    print num1,num3,num2
elif num2>num1>num3:
    print num2,num1,num3
elif num2>num3>num1:
    print num2,num3,num1
elif num3>num1>num2:
    print num3,num1,num2
else:
    print num3,num2,num1
