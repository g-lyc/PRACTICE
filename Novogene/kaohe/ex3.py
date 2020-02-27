# -*-coding:utf-8-*-


fp_in = open('3/test03.vcf','r')
fp_out = open('ex3_out_nosort.vcf','w')

dic = {}
for line in fp_in:
    i=line.strip()
    if i.startswith("#"):
        pass
    else:
		line_list = i.split('\t')
		chr_pos = '\t'.join(line_list[0:2])
		ref = line_list[3]
		alt = line_list[4]
		dp4_list = line_list[-1]
		dp4 = dp4_list.split(':')[-1]
		freq = dp4_list.split(':')[-2]
		one = chr_pos+'\t'+ref
		two = alt+'|'+freq+'|'+'('+dp4+')'
		dic[str(one)] = str(two)
		
for i in dic.keys():
	fp_out.write(i + '\t' + dic[i] + '\n')
		
		
		
		
fp_in.close()
fp_out.close()