# -*- conding:utf-8 -*-
#Author:lyc

import os, sys
import argparse

from matplotlib import pyplot as plt

import torch
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch.autograd import Variable

from model.MyDataSet import MyDataset
from model.VGG16 import vgg16_bn

if __name__ == '__main__':

    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    net = vgg16_bn().to(device)
    #weight_file = './checkpoint/VGG/first/VGG16-121-best.pth'
    weight_file = './checkpoint/VGG/first/VGG16-50-regular.pth'

    m = torch.load(weight_file, map_location='cpu')

    net.load_state_dict(m)
    print(net)
    net.eval()

    transform = transforms.Compose([
        transforms.CenterCrop(3000),
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize((0.174188, 0.093467, 0.036374), (0.256325, 0.144939, 0.068679))])

    BATCH_SIZE = 16
    #test_data = MyDataset('./test.txt', transform=transform)
    test_data = MyDataset('./tam.txt', transform=transform)
    test_loader = DataLoader(test_data, batch_size=BATCH_SIZE, shuffle=True)

    correct = 0.0

    TP, TN, FN, FP = 0,0,0,0
    for n_iter, (image, label) in enumerate(test_loader):
        print("iteration: {}\ttotal {} iterations".format(n_iter + 1, len(test_loader)))
        image = Variable(image).to(device)
        label = Variable(label).to(device)
        output = net(image)
        _, pred = output.max(1)
        correct += pred.eq(label).sum()

        softmax_func = torch.nn.Softmax(dim=1)
        # softmax_func(output)
        prob, predict_label = softmax_func(output).max(1)
        print('@'*20)
        print(pred)
        print(label.data)
        #print(predict_label)

        # TP    predict 和 label 同时为1
        TP += ((pred == 1) & (label.data == 1)).cpu().sum().item()
        # TN    predict 和 label 同时为0
        TN += ((pred == 0) & (label.data == 0)).cpu().sum().item()
        # FN    predict 0 label 1
        FN += ((pred == 0) & (label.data == 1)).cpu().sum().item()
        # FP    predict 1 label 0
        FP += ((pred == 1) & (label.data == 0)).cpu().sum().item()

    print(TP, type(TP))
    p = TP / (TP + FP)
    r = TP / (TP + FN)
    F1 = 2 * r * p / (r + p)
    acc = (TP + TN) / (TP + TN + FP + FN)

    print('acc : {}'.format(acc))
    print('recall : {}'.format(r))





    print('Test set: Accuracy: {:.4f}'.format(
        correct.float() / len(test_loader.dataset)
    ))

    #print("Parameter numbers: {}".format(sum(p.numel() for p in net.parameters())))

