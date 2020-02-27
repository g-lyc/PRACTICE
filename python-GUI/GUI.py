#coding:utf-8

from Tkinter import *
from ScrolledText import ScrolledText
import urllib
import re
import urllib2
import threading

def get(ID):
    varl.set('已经获取到第%s本书'%ID)
    html = urllib.urlopen('https://read.douban.com/ebooks/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA/?cat=book&sort=top&start='+str(ID)).read()
    reg = r'<span class="price-tag ">(.*?)元</span>.*?read.douban.com\'\)">(.*?</a>)'
    reg = re.compile(reg)  #编译正则表达式，提高效率
    return re.findall(reg,html) #匹配有顺序的返回  列表

def write():
    ID = 0
    a = []
    s = 0
    while ID <= 240:
        L = get(ID)
        ID += 20
        for i in L:
            s += 1
            a.append(float(i[0]))
            text.insert(END,'书名：%s     价格:%s\n'%(i[1],i[0]))
    text.insert(END,'--------------------------------------\n')
    text.insert(END,'该书本的总数量%s\n'%s)
    text.insert(END,'该书本的总价格%s\n'%sum(a))
    text.insert(END,'平均每本%.2f元'%(sum(a)/s))
    fn = open('read.txt','w')
    fn.write(text.get(1.0,END).encode('gbk'))
    fn.close()
    varl.set('全部处理完成')

def th():
    t1 = threading.Thread(target=write)
    t1.start()

#实例化一个变量
root = Tk()
root.title('跟着老师一起玩python') #改标签
root.geometry('+700+100')#坐标位置
text = ScrolledText(root,font=('微软雅黑',10))
text.grid()

button = Button(root,text='不信你就点一点',font=('微软雅黑',10),command=th)
button.grid()

varl = StringVar()#变量绑定
label = Label(root,font=('微软雅黑',10),fg='red',textvariable=varl)#控制变量显示的文字
label.grid()
varl.set('准备中....')
#发送创建窗口指令
root.mainloop()
