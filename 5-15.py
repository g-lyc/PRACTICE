# -*- coding: UTF-8 -*-

#最大公约数和最小公倍数
def gcd(num1,num2):
    i=1
    while True:
        i +=1
        if (i%num1==0) and (i%num2==0):
            break
    return "The gcd is %d"%i
def lcm(num1,num2):
    i=max(num1,num2)
    while True:
        i -=1
        if (num1%i==0) and (num2%i==0):
            break
    return "the lcm is %d"%i
if __name__ == '__main__':
    num1=input("please enter the number1:")
    num2=input("please enter the number2:")
    print gcd(num1,num2)
    print lcm(num1,num2)
