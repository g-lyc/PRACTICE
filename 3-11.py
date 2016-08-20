#coding:utf-8
import os

fname = raw_input('Enter filename:')
print

#try:
#    fobj = open(fname,'r')
#except IOError,e:
#    print "*** file open error:",e
#else:
#    for eachline in fobj:
#        print eachline
#    fobj.close()
if os.path.exists(fname):
    fobj = open(fname,'r')
    for eachline in fobj:
        print eachline.strip()
    fobj.close()
else:
    print 'this file not exists'
