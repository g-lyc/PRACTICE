a='ATGGTACCCGGTAGCTAGCTAGNTATTTAAGCCCCAT'
#循环方法
arc=''
for each in a:
    if each == 'A':
        arc='T'+arc
    elif each == 'T':
        arc='A'+arc
    elif each =='C':
        arc='G'+arc
    elif each == 'G':
        arc='C'+arc
    else:
        arc='N'+arc
print arc
#字典方法
rule={'A':'T','T':'A','C':'G','G':'C','N':'N'}
arc=''.join(rule[each] for each in a)[::-1]
