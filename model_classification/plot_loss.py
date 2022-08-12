# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

file = sys.argv[1]
#file = './train_vgg.log'

train_loss = []
test_loss = []

with open(file) as f:
    epoch_train_loss = []
    for line in f:
        if line.startswith('Test'):
            loss = sum(epoch_train_loss) / len(epoch_train_loss)
            train_loss.append(float(loss))
            loss = line.split(',')[0].split()[-1]
            test_loss.append(float(loss))
        else:
            loss = line.split('\t')[1].split()[1]
            epoch_train_loss.append(float(loss))

print(len(train_loss))
print(len(test_loss))

import numpy as np
import matplotlib.pyplot as plt

#x = np.linspace(0, 200, 200)
x = np.linspace(0, 181, 181)
y1, y2 = np.array(train_loss), np.array(test_loss)
print(type(y1))
plt.plot(x, y1, label='Train')
plt.plot(x, y2, label='Test')
plt.legend()
plt.xlabel('Epoch')
plt.ylabel('Loss')
#plt.show()
plt.savefig('loss.jpg')

#print(train_loss)

