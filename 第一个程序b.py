#coding:utf-8

'readTextFile.py -- read and display text file'

#get filename
fname = raw_input('Enter filename:')
print

#attempt to open file for reading
try:
    fobj = open(fname,'r')
except IOError,e:
    print "*** file open error:",e
else:
    for eachline in fobj:
        print eachline
    fobj.close()
