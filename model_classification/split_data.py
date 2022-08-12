# -*- conding:utf-8 -*-
#Author:lyc
import os, sys
import random
from shutil import copyfile

pos_img = '/home/users/liyichen/project/64/z'
neg_img = '/home/users/liyichen/project/ssd.pytorch.sign/data/VOCdevkit/VOC2020/JPEGImages'

# input_data_0 = '../1_Data_Augmentation/data/0'
# input_data_1 = '../1_Data_Augmentation/data/1'


s_0, s_1 = [],[]
for s in os.listdir(neg_img):
    s_0.append(neg_img+'/'+s)

for s in os.listdir(pos_img):
    s_1.append(pos_img+'/'+s)

s_1 = random.sample(s_1, len(s_0))

train_0 = random.sample(s_0,int(len(s_0)*0.85))
test_0 = [i for i in s_0 if i not in train_0]

train_1 = random.sample(s_1,int(len(s_1)*0.85))
test_1 = [i for i in s_1 if i not in train_1]
#print(test_1)

with open('train.txt','w') as o:
    for i in train_0:
        o.write('{} 0\n'.format(i))
    for i in train_1:
        o.write('{} 1\n'.format(i))

with open('test.txt','w') as o:
    for i in test_0:
        o.write('{} 0\n'.format(i))
    for i in test_1:
        o.write('{} 1\n'.format(i))

