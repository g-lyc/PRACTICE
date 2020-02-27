# -*-coding:utf-8-*-


fp_in1 = open('4/NC_001133.fna','r')
fp_in2 = open('4/NC_001133.ptt','r')
fp_out = open('ex4_out','w')

fp_in1.readline()
fp_in2.readline()




lca_list = []
bottom_dic = {}
for line in fp_in2:
	line2 = line.rstrip().split('\t')
	#print line2[1]
	
	if line2[1] == '+':
		lca = line2[0]
		syn = line2[5]
		gene = line2[4]
		bottom = '>'+gene+'|'+syn+'|'+':'+lca
		bottom_dic[lca] = bottom
		lca_list.append(lca)
#print lca_list
#print bottom_dic

list = []
for i in fp_in1.readline():
	list.append(i)


for i in lca_list:
	j = i.strip().split('..')
	first = int(j[0])
	second = int(j[1])
	fp_out.write(bottom_dic[i]+'\n')
	fp_out.write(str(list[first-1:second])+'\n')
	
	















fp_in1.close()
fp_in2.close()
fp_out.close()