# -*-coding:utf-8-*-
import re

fp_in = open('ex3_out_mid.test','r')
fp_out = open('ex3_out.test','w')


all_lines = []
for line in fp_in:
	line_list = line.rstrip().split('\t')
	all_lines.append('\t'.join(line_list))	
#print all_lines	

		
all_first_num_clean = []
for i in range(1,23):
	all_first_num_clean.append(str(i))
all_first_num_clean=all_first_num_clean+['X']
#print all_first_num_clean

num_line_dic = {}
for num in all_first_num_clean:
	num_tab = num + '\t'
	num_line_dic[num] = []
	for item in all_lines:
		match1 = re.match(num_tab,item)
		if match1:
			item_list = [int(item.split('\t')[1]),item]
			num_line_dic[num].append(item_list)
			
for num in all_first_num_clean:
	num_line_dic[num] = sorted(num_line_dic[num])
	
all_line_sorted = []
for num in all_first_num_clean:
	for i in range(len(num_line_dic[num])):
		all_line_sorted.append(num_line_dic[num][i][1])

for sorted_line in all_line_sorted:
	fp_out.write(sorted_line + '\n')
		



fp_in.close()
fp_out.close()
