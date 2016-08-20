# -*- coding: UTF-8 -*-

type = raw_input("请输入你要计算的几何种类（A正方形，B立方体，C圆，D球):")
if type=="A":
    b=raw_input("请输入正方形的边长:")
    a=float(b)
    print "正方形的面积为:%f" %(a*1.000*a)
elif type=="B":
    b=raw_input("请输入正方体的边长:")
    a=float(b)
    print "正方体的体积为:%f" %(a*1.000*a*6)
elif type=="C":
    b=raw_input("请输入圆的半径:")
    a=float(b)
    print "圆的面积为:%f" %(3.14159*a*a)
elif type=="D":
    b=raw_input("请输入球的半径:")
    a=float(b)
    print "球的体积为:%f"%(4*3.14159*a*a)
else:
    print "你输入的几何种类错误，请重新运行程序重新输入"
