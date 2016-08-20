# -*- coding: UTF-8 -*-

def time(h,t):
    h=int(h)
    t=int(t)
    x=h*60+t
    print 'The minutes is',t
if __name__ == '__main__':
    s=raw_input("please input the time in HH:MM...\n")
    s=s.split(":")
    time(s[0],s[1])
