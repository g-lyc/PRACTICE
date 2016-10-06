#!-*-coding:utf-8-*-
'''
需求：描述人类的恋爱，成婚，生子过程

一、分解需求
1.男人和女人
2.男人和男人
3.女人和女人

二、找到共通性
1.都是人
2.两个人

三、找到最小节点
1.男人
2.女人

'''

#从最小节点开始往上走
class boy(object):
    gender = 1

    def __init__(self,name):
        self.name = name

class girl(object):
    gender = 0

    def __init__(self,name):
        self.name = name

#共通性
class love(object):
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def meet(self):
        return u'这是s%和s%的恋爱'%(self.first.name,self.second.name)

    def marry(self):
        return u'这是s%和s%的婚姻'%(self.first.name,self.second.name)

    def children(self):
        return u'这是s%和s%的孩子'%(self.first.name,self.second.name)

#开始写需求
class normal_love(love):
    '''
    男人和女人
    '''
    def __init__(self,first,second):
        if 1 != first.gender + second.gender:
            print u'对象引入错误'
        else:
            love.__init__(self,first,second)
    # def meet(self):
    #     pass
    #
    # def marry(self):
    #     pass
    #
    # def children(self):
    #     pass

class gay_love(love):
    '''
    男人和男人
    '''
    def __init__(self,first,second):
        if 2 != first.gender + second.gender:
            print u'对象引入错误'
        else:
            love.__init__(self,first,second)

class girl_love(love):
    '''
    女人和女人
    '''
    def __init__(self,first,second):
        if 0 != first.gender + second.gender:
            print u'对象引入错误'
        else:
            love.__init__(self,first,second)

hanmeimei = girl('韩梅梅')
lilei = boy('李磊')

normal = normal_love(hanmeimei,lilei)
gay = gay_love(hanmeimei,lilei)
gi = girl_love(hanmeimei,lilei)

print normal.meet()
print gay.meet()
print gi.meet()
