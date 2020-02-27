# -*-coding:utf-8-*-
import re

fp_in1 = open('test03_1.info','r')
fp_in2 = open('test03_2.info','r')
fp_in3 = open('test03_3.info','r')
fp_out = open('test03_out.info','w')

fp_out.write('Chr' + '\t' + 'Position' + '\t' + 'Ref' + '\t' + 'test03_1' + '\t' + 'test03_2' + '\t' + 'test03_3' + '\n')

all_line1 = []
all_line2 = []
all_line3 = []
last1 = []
last2 = []
last3 = []
chr_list = []
for line in fp_in1:
    line_list = line.rstrip().split('\t')
    line2_list = line_list[:-1]
    line2 = '\t'.join(line2_list)
    all_line1.append(line2)
    last1.append(line_list[-1])
    chr_list.append(line_list[0])

for line in fp_in2:
    line_list = line.rstrip().split('\t')
    line2_list = line_list[:-1]
    line2 = '\t'.join(line2_list)
    all_line2.append(line2)
    last2.append(line_list[-1])
    chr_list.append(line_list[0])

for line in fp_in3:
    line_list = line.rstrip().split('\t')
    line2_list = line_list[:-1]
    line2 = '\t'.join(line2_list)
    all_line3.append(line2)
    last3.append(line_list[-1])
    chr_list.append(line_list[0])

#print all_line1
#print last1

all_lines = all_line1 + all_line2 + all_line3
all_lines = list(set(all_lines))
#print all_line

chr_list = list(set(chr_list))
#print chr_list

chr_pos_ref = {}
for chr in chr_list:
    chr_tab = chr + '\t'
    chr_pos_ref[chr] = []
    for item in all_lines:
        match1 = re.match(chr_tab, item)
        if match1:
            item_list = [int(item.split('\t')[1]),item]
            chr_pos_ref[chr].append(item_list)

#print chr_pos_ref
for chr in chr_list:
    chr_pos_ref[chr] = sorted(chr_pos_ref[chr])

all_lines_sorted=[]
for chr in chr_list:
	for i in range(len(chr_pos_ref[chr])):
		all_lines_sorted.append(chr_pos_ref[chr][i][1])

#print all_lines_sorted

for sorted_line in all_lines_sorted:
    last_three = ['-', '-', '-']
    if sorted_line in all_line1:
        index = all_line1.index(sorted_line)
        last_three[0] = last1[index]
    if sorted_line in all_line2:
        index = all_line2.index(sorted_line)
        last_three[1] = last2[index]
    if sorted_line in all_line3:
        index = all_line3.index(sorted_line)
        last_three[2] = last3[index]

    fp_out.write(sorted_line + '\t' + last_three[0] + '\t' + last_three[1] + '\t' + last_three[2] + '\n')



fp_in1.close()
fp_in2.close()
fp_in3.close()
fp_out.close()

'''
chr_123 = {}
pos_ref = {}

while True:
    line = fp_in1.readline()
    if len(line.rstrip()) == 0:
        break
    line = line.rstrip().split('\t')
    key = line[0]
    value = line[3]
    chr_123[key] = []
    chr_123[key].append(value)

#print chr_123

while True:
    line = fp_in2.readline()
    if len(line.rstrip()) == 0:
        break
    line = line.rstrip().split('\t')
    key = line[0]
    if key in chr_123.keys():
        chr_123[key].append(line[3])
    else:
        chr_123[key] = []
        chr_123[key].append(line[3])

while True:
    line = fp_in3.readline()
    if len(line.rstrip()) == 0:
        break
    line = line.rstrip().split('\t')
    key = line[0]
    if key in chr_123.keys():
        chr_123[key].append(line[3])
    else:
        chr_123[key] = []
        chr_123[key].append(line[3])
for j in chr_123.keys():
    for i in chr_123.values():
        if len(i) == 1:
            chr_123[j].append('-','-')
        if len(i) == 2:
            chr_123[j].append('-')
print chr_123
'''

