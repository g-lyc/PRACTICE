# -*- conding:utf-8 -*-
# Author:lyc
import os, sys
from collections import deque

#deque相比list
#优点：两端插入元素或删除元素时间复杂度都为O(1)
#在列表两端插入或删除元素时间复杂度都为O(N)


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open(r'deque_test.txt') as f:
        for line, prevlines in search(f, 'python', 3):
            for pline in prevlines:
                print(pline, end='')
                #print(line, end='')
                print('-' * 20)
