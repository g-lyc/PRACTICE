#!/usr/bin/env python
# -*-coding:utf-8-*-

fp_in = open('3/test3.vcf','r')
fp_out = open('ex3_out_mid.test','w')

all_dic = {}

for line in fp_in:
	line = line.strip()
	if line.startswith('#'):
		pass
	else:
		line = line.strip().split('\t')
		id = line[0]+'\t'+line[1]+'\t'+line[2]+'\t'+line[3]+'\t'+line[4]+'\t'+line[5]+'\t'+line[6]+'\t'+line[7]+'\t'+line[8]+'\t'+line[9]+'\t'+line[10]
		value = line[9]
		all_dic[value] = id
#print all_dic

for i in all_dic.keys():
	line = i.split(':')
	if line[1] > 6 and int(line[-3]) > 50:
		fp_out.write(str(all_dic[i])+'\n')

fp_in.close()
fp_out.close()  
