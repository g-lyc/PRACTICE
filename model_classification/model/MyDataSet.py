# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

from PIL import Image
from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self, txt_path, transform = None):

        imgs = []
        with open(txt_path) as f:
            for line in f:
                line = line.rstrip().split()
                imgs.append((line[0], int(line[1])))

        self.imgs = imgs
        self.transform = transform

    def __getitem__(self, index):
        fn, label = self.imgs[index]
        img = Image.open(fn).convert('RGB')

        if self.transform is not None:
            img = self.transform(img)
        return img, label

    def __len__(self):
        return len(self.imgs)



