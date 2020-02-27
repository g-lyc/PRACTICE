#coding:utf-8
'''
带文本菜单的程序 写一个带文本菜单的程序，菜单项如下（1）取五个数的和 (2) 取五个
数的平均值....（X）退出。由用户做一个选择，然后执行相应的功能。 当用户选择退出时程序
结束。 这个程序的有用之处在于用户在功能之间切换不需要一遍一遍的重新启你动的脚本。
'''

def menu():
    print '1.取五个数的和'
    print '2.取五个数的平均值'
    print 'x.退出'
    rel = str(raw_input('请输入您的选项:'))
    return rel

def sum(aTuple):
    num=0
    for i in aTuple:
        num += i
    return num

aTuple = (1,2,3,4,5)

while True:
    sel = menu()
    if sel==str('1'):
        print 'num is:%d'%sum(aTuple)
    elif sel==str('2'):
        print 'num is:%f'%(float(sum(aTuple))/len(aTuple))
    elif sel==str('x'):
        break
    else:
        continue
