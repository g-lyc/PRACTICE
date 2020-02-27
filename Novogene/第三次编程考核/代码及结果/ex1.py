# -*-coding:utf-8-*-

fp_in = open('1/1.test','r')
fp_out = open('ex1_out.test','w')

s = ''
all_dic = {}
for eachline in fp_in:
	eachline = eachline.strip()
	s = s + eachline
length = len(s)
#print length

A = s.count('A')
G = s.count('G')
C = s.count('C')
T = s.count('T')

#all_dic['A:'] = round(float(A)/length*100,2)
#all_dic['G:'] = round(float(G)/length*100,2)
#all_dic['T:'] = round(float(T)/length*100,2)
#all_dic['C:'] = round(float(C)/length*100,2)

all_dic[round(float(A)/length,2)] = 'A:'
all_dic[round(float(G)/length,2)] = 'G:'
all_dic[round(float(T)/length,2)] = 'T:'
all_dic[round(float(C)/length,2)] = 'C:'




for i in sorted(all_dic.keys(),reverse = True):
	fp_out.write(all_dic[i]+str(i)+'\n')








fp_in.close()
fp_out.close()  