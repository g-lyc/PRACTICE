# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

import os
from PIL import Image
import numpy as np
from scipy.misc import imread

trainPath = r'../data/train'
testPath = r'../data/test'
trainDir = os.listdir(trainPath)
testDir = os.listdir(testPath)

R_channel = 0
G_channel = 0
B_channel = 0
for idx in range(len(trainDir)):
    filename = trainDir[idx]
    img = imread(os.path.join(trainPath, filename)) / 255.0
    R_channel = R_channel + np.sum(img[:, :, 0])
    G_channel = G_channel + np.sum(img[:, :, 1])
    B_channel = B_channel + np.sum(img[:, :, 2])

for idx in range(len(testDir)):
    filename = testDir[idx]
    img = imread(os.path.join(testPath, filename)) / 255.0
    R_channel = R_channel + np.sum(img[:, :, 0])
    G_channel = G_channel + np.sum(img[:, :, 1])
    B_channel = B_channel + np.sum(img[:, :, 2])

num = (len(trainDir)+len(testDir)) * 4496 * 3000
R_mean = R_channel / num
G_mean = G_channel / num
B_mean = B_channel / num

R_channel = 0
G_channel = 0
B_channel = 0
for idx in range(len(trainDir)):
    filename = trainDir[idx]
    img = imread(os.path.join(trainPath, filename)) / 255.0
    R_channel = R_channel + np.sum((img[:, :, 0] - R_mean) ** 2)
    G_channel = G_channel + np.sum((img[:, :, 1] - G_mean) ** 2)
    B_channel = B_channel + np.sum((img[:, :, 2] - B_mean) ** 2)

for idx in range(len(testDir)):
    filename = testDir[idx]
    img = imread(os.path.join(testPath, filename)) / 255.0
    R_channel = R_channel + np.sum((img[:, :, 0] - R_mean) ** 2)
    G_channel = G_channel + np.sum((img[:, :, 1] - G_mean) ** 2)
    B_channel = B_channel + np.sum((img[:, :, 2] - B_mean) ** 2)

R_var = np.sqrt(R_channel / num)
G_var = np.sqrt(G_channel / num)
B_var = np.sqrt(B_channel / num)
print("R_mean is %f, G_mean is %f, B_mean is %f" % (R_mean, G_mean, B_mean))
print("R_var is %f, G_var is %f, B_var is %f" % (R_var, G_var, B_var))