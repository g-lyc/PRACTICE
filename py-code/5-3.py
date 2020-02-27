#coding:utf-8
def value(num):
    if 90<=num<=100:
        print 'A'
    elif 80<=num<=89:
        print 'B'
    elif 70<=num<=79:
        print 'C'
    elif 60<=num<=69:
        print 'D'
    elif num>=0 and num<60:
        print 'F'
    else:
        print  "The num is invalid."

try:
    num=int(raw_input("Enter a num:"))
    value(num)
except ValueError,v:
    print 'You must input digits.'
