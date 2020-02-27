# -*-coding:utf-8-*-

fp_in = open('2/2.test','r')
fp_in1 = open('2/2.list','r')
fp_out = open('ex2_out.test','w')



dic1={}
for line in fp_in:
    i=line.strip()
    if i.startswith(">"):
        a=''
        id=i[5:-1]
    else:
		a=a+i
		dic1[id] = a
dic2 = {}
for line in fp_in1:
	line = line.strip().split('\t')
	dic2[line[0]] = line[1]
	


 
	
for i in dic1.keys():
	fp_out.write(str(i)+'\t'+str(dic2[i])+'\n'),
	beg = int(dic2[i])
	end = int(dic2[i])+51
	sss = dic1[i]
	fp_out.write(sss[beg:end]+'\n')








fp_in.close()
fp_out.close()  