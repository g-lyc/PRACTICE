#coding:utf-8

#import Tkinter

#top = Tkinter.Tk()
#top.mainloop()
#pack简单     grid复杂界面

from Tkinter import *
root = Tk()
root.geometry('500x200')   #位置

li = ['python','java','php']
lid = ['缩微','小王子']

listb  = Listbox(root)#创建两个列表组件
listb2 = Listbox(root)

#插入数据

for item in li:
    listb.insert(0,item)
for item in lid:
    listb.insert(0,item)

#小部件放入主窗口
listb.pack()
listb2.pack()
root.mainloop()
