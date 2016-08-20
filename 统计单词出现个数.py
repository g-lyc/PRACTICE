#-*-coding:utf-8-*-

'''
collections模块中的Counter函数统计字符出现的个数
'''

from collections import Counter

def words():
    c = Counter()
    with open('result') as f:
        for line in f:
            c.update(line.split(' '))
    return sum(c.values())

if __name__ == '__main__':
    print(words())
