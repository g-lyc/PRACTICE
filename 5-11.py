# -*- coding: UTF-8 -*-

def div(num1,num2):
    if num%num2==0:
        return "True"
    else:
        return "False"
if __name__ == '__main__':
    num1=input("please type the num1:")
    num2=input("please type the num2:")
    print "%d divided %d is %s"%(num1,num2,div(num1,num2))
