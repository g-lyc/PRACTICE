# -*- coding: UTF-8 -*-
print 'Enter a expression and I will tell you the answer.'
exp = raw_input('>')
if len(exp.split('-'))==2 and len(exp.split('+'))==2:
    try:
        elist=exp.split('-')
        a = float(elist[0])
        b = float(elist[1])
        print a-b
    except ValueError,v:
        try:
            elist=exp.split('+')
            a = float(elist[0])
            b = float(elist[1])
            print a+b
        except ValueError,v:
            print "Input invalid 1"
elif len(exp.split('-'))==2 and len(exp.split('+')) !=2:
    elist=exp.split('-')
    try:
        a = float(elist[0])
        b = float(elist[1])
        print a-b
    except ValueError,v:
        print "Input invalid 2"
elif len(exp.split('-'))==3:
    elist=exp.split('-')
    try:
        a = float(elist[1])
        b = float(elist[2])
        print -a-b
    except ValueError,v:
        print 'Input invalid 3'
elif len(exp.split('+'))==2 and len(exp.split('-')) !=2:
    elist=exp.split('+')
    try:
        a = float(elist[0])
        b = float(elist[1])
        print a+b
    except ValueError,v:
        print 'Input invalid 4'
elif len(exp.split('+'))==3:
    elist=exp.split('+')
    try:
        a = float(elist[1])
        b = float(elist[2])
        print a+b
    except ValueError,v:
        print 'Input invalid 5'
elif len(exp.split('*'))==2:
    elist=exp.split('*')
    try:
        a = float(elist[0])
        b = float(elist[1])
        print a*b
    except ValueError,v:
        print 'Input invalid 6'
elif len(exp.split('/'))==2:
    elist=exp.split('/')
    try:
        a = float(elist[0])
        b = float(elist[1])
        print a/b
    except ValueError,v:
        print 'Input invalid 7'
elif len(exp.split('%'))==2:
    elist=exp.split('%')
    try:
        a = float(elist[0])
        b = float(elist[1])
        print a%b
    except ValueError,v:
        print 'Input invalid 8'
elif len(exp.split('**'))==2:
    elist=exp.split('**')
    try:
        a = float(elist[0])
        b = float(elist[1])
        print a**b
    except ValueError,v:
        print 'Input invalid 9'
else:
    print 'Input error'
