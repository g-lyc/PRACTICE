# -*-coding:utf-8-*-

fp_in = open('4/test4.vcf.final.xls','r')
fp_out = open('ex4_out_mid.xls','w')

fp_in.readline()


for line in fp_in:
	line = line.strip().split('\t')
	qian = float(line[10])
	exec1 = float(line[13])
	freq = float(line[14])
	eachline = '\t'.join(line)
	if qian > 0.05 and exec1 > 0.05:
		if freq > 0.15 and freq < 0.85:
			fp_out.write(eachline+'\t'+'杂合'+'\n')
		elif freq == 0.15 or freq == 0.85:
			fp_out.write(eachline+'\t'+'杂合'+'\n')
		else:
			fp_out.write(eachline+'\t'+'纯合'+'\n')















fp_in.close()
fp_out.close()  