# -*- coding: UTF-8 -*-

from __future__ import division
def celcius(F):
    C=F-32*(5/9)
    return C
if __name__ =="__main__":
    F=input("please enter the Fahrenheit degree:")
    print celcius(F)
