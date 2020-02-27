# -*-coding:utf-8-*-

#import re
input = open('test01.fasta','r')
out = open('test02.fasta','w')


dic={}
for line in input:
    i=line.strip()
    if i.startswith(">"):
        a=''
        id=i[1:6]
    else:
        a=a+i
        x=a.count('G')+a.count('C')
        y=len(a)
        dic[id]=round(float(x)/y*100,2)
for j in sorted(dic.keys()):
    out.write(j+'\t'+str(dic[j])+'\n')
input.close()
out.close()




'''
dic={}
for i in input:
    i=i.strip()
    if i.startswith(">"):
        a=''
        id=i[1:6]
    else:
        a=a+i
        x=a.count('G')+a.count('C')
        y=len(a)
        dic[id]=round(float(x),2)*100/y

for j in sorted(dic.keys()):
    out.write(j+'\t'+str(dic[j])+'\n')
input.close()
out.close()
'''
'''
id_seq_dist = {}
id_list = []
while True:
    line = input.readline()
    if len(line.rstrip()) == 0:
        break
    id = line[1:].split()[0]

    seq = input.readline().rstrip()
    id_seq_dist[id] = seq
    id_list.append(id)

print id_seq_dist
print id_list
'''
