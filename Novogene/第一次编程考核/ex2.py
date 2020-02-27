# -*-coding:utf-8-*-

input_file = open('SNV_InDel_data.xls','r')
out_file = open('SNV_InDel_data_out.xls','w')

sample_list = input_file.readline()
sample_list = sample_list.rstrip().split('\t')[3:14]
#print len(sample_list)


gene_sample_dic = {}
while True:
    line = input_file.readline()
    if len(line.rstrip())==0:
        break
    line = line.rstrip().split('\t')
    gene_name = line[15]
    sample_value = line[3:14]

    for i in range(len(sample_list)):
        if gene_sample_dic.has_key(gene_name):
            gene_sample_dic[gene_name].update({sample_list[i]:0})
            if sample_value[i] != '-':
                gene_sample_dic[gene_name][sample_list[i]] += 1
        else:
            
            gene_sample_dic.update({gene_name:{sample_list[i]:0}})
            if sample_value[i] == '-':
                gene_sample_dic[gene_name][sample_list[i]] = 0
            else:
                gene_sample_dic[gene_name][sample_list[i]] = 1
          

#print gene_sample_dic
#print gene_sample_dic.keys()
#print gene_sample_dic.values()


out_file.write('gene' + '\t' + '\t'.join(sample_list) + '\n')

for j in sorted(gene_sample_dic.keys()):
    out_file.write(j),
    for i in sample_list:
        out_file.write('\t' + str(gene_sample_dic[j][i])),
    out_file.write('\n')
        


input_file.close()
out_file.close()
