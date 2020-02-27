#!/usr/bin/env python
# -*-coding:utf-8-*-

fp_in1 = open(r'520list.txt','r')
fp_in2 = open(r'548list.txt','r')
fp_out1 = open(r'520_548same.txt','w')
fp_out2 = open(r'520_548diff.txt','w')

gene_list1 = []
for line in fp_in1:
	line1 = line.rstrip()
	gene_list1.append(line1)
	
#print gene_list1
	
gene_list2 = []
for line in fp_in2:
	line1 = line.rstrip()
	gene_list2.append(line1)
	
all_list = gene_list1 + gene_list2	
all_list_clean = list(set(all_list))
		
same_list = []
diff_list = []

for i in all_list_clean:
	if i in gene_list1 and i in gene_list2:
		same_list.append(i)
	else:
		diff_list.append(i)

same_list_sorted = sorted(same_list)
diff_list_sorted = sorted(diff_list)

for i in same_list_sorted:
	fp_out1.write(i + '\n')

for j in diff_list_sorted:
	fp_out2.write(j + '\n')

fp_in1.close()
fp_in2.close()
fp_out1.close()
fp_out2.close()
