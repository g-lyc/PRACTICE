#coding:utf-8
b = bool(False)
while b is False:
    num = int(raw_input('请输入一个1到100之间的数'))
    if num>=1 and num<=100:
        print 'succeed!'
        break
    else:
        print 'input error!'
