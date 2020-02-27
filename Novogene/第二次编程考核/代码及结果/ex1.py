# -*-coding:utf-8-*-


fp_in = open('1/test02.fasta','r')
fp_out = open('ex1_out.fasta','w')

dic={}
dic2={}
for line in fp_in:
    i=line.strip()
    if i.startswith(">"):
        a=''
        id=i[1:4]
    else:
        a=a+i
        y=len(a)
        if y > 200:
			dic[id] = y
			dic2[id] = a
		
		
			#fp_out.write(id+'\t'+str(y)+'\n'+a+'\n')
			
			

for i in sorted(dic.keys()):
		fp_out.write(i+'\t'+str(dic[i])+'\n'+dic2[i]+'\n')













fp_in.close()
fp_out.close()