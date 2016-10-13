#coding:utf-8

'''
要求：生成一个4*4的2维数组并将其顺时针旋转90度
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
--------------------
[0, 0, 0, 0]
[1, 1, 1, 1]
[2, 2, 2, 2]
[3, 3, 3, 3]
'''
data = [[col for col in range(4)] for row in range(4)]
for row in data:
    print row
print "---------------------------"

for row_index,row in enumerate(data):
    for col_index in range(row_index,len(row)):
        tmp = data[col_index][row_index]
        data[col_index][row_index] = row[col_index]
        data[row_index][col_index] = tmp

for i in data:
    print i
