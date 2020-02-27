#!/usr/bin/env python
# -*-coding:utf-8-*-

'''
Command line:python same_gene.py file1 file2 file3 ... outfile
'''

import sys

def conver(con_file):
	file = open(con_file,'r')
	gene_list = []
	for line in file:
		line1 = line.rstrip()
		if len(line1) < 1:
			continue
		gene_list.append(line1)
	file.close()
	return gene_list

def focus(list1,list2):
	gene_list1 = list1
	gene_list2 = list2
	same_list = []

	all_list = gene_list1 + gene_list2	
	all_list_clean = list(set(all_list))

	for i in all_list_clean:
		if i in gene_list1 and i in gene_list2:
			same_list.append(i)
		else:
			pass
			
	return same_list

if __name__ == '__main__':
	file_list = sys.argv[1:-1]
	#print file_list
	file1,file2 = conver(file_list[1]),conver(file_list[2])
	same_file = focus(file1,file2)
	first_list = same_file
	for i in file_list[3:]:
		gene_list = conver(i)
		first_list = focus(first_list,gene_list)
	
	fp_out = open(sys.argv[-1],'w')
	for i in first_list:
		fp_out.write(i + '\n')


	
	
	
