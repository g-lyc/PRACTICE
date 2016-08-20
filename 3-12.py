#coding:utf-8

'to read or make a file'

import os
def makeTextFile():
    '''make a file'''
    while True:
        fname=raw_input('Enter file name:')
        try:
            fobj = open(fname,'r')
        except IOError,e:
            break;
        else:
            print "Error:'%s' already exists"% fname
            fobj.close

    all=[]
    print "\nEnter lines ('.' by itself to quit).\n"

    while True:
        entry = raw_input('>')
        if entry == '.':
            break
        else:
            all.append(entry)

    fobj = open(fname,'w')
    fobj.write('\n'.join(all))
    fobj.close()
    print 'DONE!'

def readTextFile():
    '''read a file'''
    fname = raw_input('Enter filename:')
    print

    if os.path.exists(fname):
        fobj = open(fname,'r')
        for eachline in fobj:
            print eachline,
        fobj.close()
    else:
        print 'this file not exists'

def main():
    '''main menu'''
    while True:
        print '1.Read a file'
        print '2.Make a file'
        print 'x.exit'
        myStr = raw_input('input your choice:')
        if myStr == '1':
            readTextFile()
        elif myStr =='2':
            makeTextFile()
        elif myStr == 'x':
            break

if __name__ == '__main__':
    main()
