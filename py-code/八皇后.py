#!-*-coding:utf-8-*-
import random

#定义检查冲突的函数
def conflict(state,nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False

#主函数（递归）
def queens(num=8,state=()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,) + result

#print list(queens(4))
#print list(queens(8))

#将输出处理结果处理的更容易理解一点
def prettyprint(solution):
    def line(pos,length=len(solution)):
        return '.'*(pos) + 'X' + '.'*(length-pos-1)
    for pos in solution:
        print line(pos)

prettyprint(random.choice(list(queens(8))))
