# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

#Code to execute in an independent thread
import time
def countdown(n):
    while n>0:
        print('T-minus',n)
        n-=1
        time.sleep(5)
#Createandlaunchathread
from threading import Thread
t=Thread(target=countdown,args=(10,))
t.start()