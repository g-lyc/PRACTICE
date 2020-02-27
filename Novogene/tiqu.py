#!/usr/bin/env python

import sys
'''
if len(sys.argv)!=3:
	    print "python test.py input_file out_file"
		exit(0)
'''
input_file=open(sys.argv[1],"r")
out_file=open(sys.argv[2],"w")

input_file.readline()

top_five = []
last = []
for line in input_file:
	line_list = line.strip().split('\t')
	line_top = line_list[0:5]
	line_bottom = line_list[-1]
	top_five.append('\t'.join(line_top))
	last.append('\t'.join(line_bottom))
#print top_five
#print last

last_list = []
for line in last:
	line2 = [line[6]+'\t'+line[4],line[5]+'\t'+line[3]+'\t'+line[0]]
	last_list.append(line2)

for i in top_five:
	out_file.write(i),
	for j in last_list:
		out_file.write('\t' + j + '\n') 



input_file.close()
out_file.close()

