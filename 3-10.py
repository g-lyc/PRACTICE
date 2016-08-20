#coding:utf-8
#3-10第一个

import os
#get file name
while True:
    fname=raw_input('Enter file name:')
#    if os.path.exists(fname):
#        print "ERROR: '%s' already exists"% fname
#    else:
#        break
    try:
        fobj = open(fname,'r')
    except IOError,e:
        break;
    else:
        print "Error:'%s' already exists"% fname
        fobj.close

#get file content (text) lines
all=[]
print "\nEnter lines ('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.write('\n'.join(all))
fobj.close()
print 'DONE!'


#第二个

#get filename
fname = raw_input('Enter filename:')
print

#attempt to open file for reading
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
        print eachline,
    fobj.close()
else:
    print 'this file not exists'
