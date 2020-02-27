#-*-coding:utf-8-*-
fp_in = open("5/test05.fsa","r")
fp_out = open("5out.fsa","w")

all_dic = {}


for eachline in fp_in:
	eachline = eachline.strip()
	if eachline.startswith('>'):
		l = eachline.split('|')
		genename = l[1]
		s = ''
	else:
		s = s + eachline
	all_dic[genename] = s

#print all_dic

		
for i in all_dic.keys():
	fp_out.write(i+'\t'+str(len(all_dic[i]))+'\t'+'A:'+str(all_dic[i].count('A'))+'/'+'T:'+str(all_dic[i].count('T'))+'/'+'G:'+str(all_dic[i].count('G'))+'/'+'C:'+str(all_dic[i].count('C'))+'\n')








fp_in.close()
fp_out.close()     
    
