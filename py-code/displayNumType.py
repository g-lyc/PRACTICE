#coding:utf-8

def displayNumType(num):
    print num,'is',
    if isinstance(num,(int,long,float,complex)):
        print 'a number of type:',type(num).name
    else:
        print 'not a number at all'

displayNumType(-69)
displayNumType(9999999999999999999999999)
displayNumType(98.6)
