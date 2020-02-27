# -*-coding:utf-8-*-

fp_in1 = open('6.20-7.31样本信息.xls','r')
fp_in2 = open('样本检测结果.xlsx','r')
fp_out = open('output.xls','w')

fp_in1.readline()
fp_in2.readline()

all_dic1 = {}
for line in fp_in1:
	line = line.strip().split('\t')
	id = line[-2]
	n_t = line[13:20]
	N_T = '\t'.join(n_t)
	AO = line[-13]
	AQ = line[-11]
	value = N_T+'\t'+AO+'\t'+AQ
	all_dic1[id] = value
	
	
all_dic2 = {}
for line in fp_in2:
	line = line.strip().split('\t')
	id = line[0]
	line2 = line[1:]
	value = '\t'.join(line2)
	all_dic2[id] = value
	
	
for i in all_dic2.keys():
	fp_out.write(i+'\t'+all_dic1[i]+'\t'+all_dic2[i]+'\n')





















fp_in1.close()
fp_in2.close()
fp_out.close()
