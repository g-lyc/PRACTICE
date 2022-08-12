# -*- conding:utf-8 -*-
#Author:lyc
import os, sys
os.environ['CUDA_VISIBLE_DEVIDES'] = '0,1,2,3'

from model.MyDataSet import MyDataset
from model.VGG16 import vgg16_bn
from model.utils import WarmUpLR
import torch
import torch.nn as nn
from torchvision import transforms
from torch.utils.data import DataLoader
from torch.autograd import Variable

from datetime import datetime


def train(model, device, train_loader, optimizer, epoch, batch_size):

    model.train().to(device)
    for batch_index, (images, labels) in enumerate(train_loader):

        if epoch <= warm:
            warmup_scheduler.step()

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss_function = nn.CrossEntropyLoss()
        loss = loss_function(outputs, labels)
        loss.backward()
        optimizer.step()

        print('Training Epoch: {epoch} [{trained_samples}/{total_samples}]\tLoss: {:0.4f}\tLR: {:0.6f}'.format(
            loss.item(),
            optimizer.param_groups[0]['lr'],
            epoch=epoch,
            trained_samples=batch_index * batch_size + len(images),
            total_samples=len(train_loader.dataset)
        ))
        o.write('Training Epoch: {epoch} [{trained_samples}/{total_samples}]\tLoss: {:0.4f}\tLR: {:0.6f}\n'.format(
            loss.item(),
            optimizer.param_groups[0]['lr'],
            epoch=epoch,
            trained_samples=batch_index * batch_size + len(images),
            total_samples=len(train_loader.dataset)
        ))


def eval_training(model, device, test_loader):
    model.eval().to(device)

    test_loss = 0.0 # cost function error
    correct = 0.0

    with torch.no_grad():
        for (images, labels) in test_loader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss_function = nn.CrossEntropyLoss()
            loss = loss_function(outputs, labels)
            test_loss += loss.item()
            _, preds = outputs.max(1)
            correct += preds.eq(labels).sum()

    print('Test set: Average loss: {:.4f}, Accuracy: {:.4f}'.format(
        #test_loss / len(test_loader.dataset),
        test_loss / (len(test_loader.dataset)//BATCH_SIZE),
        correct.float() / len(test_loader.dataset)
    ))
    o.write('Test set: Average loss: {:.4f}, Accuracy: {:.4f}\n'.format(
        #test_loss / len(test_loader.dataset),
        test_loss / (len(test_loader.dataset)//BATCH_SIZE),
        correct.float() / len(test_loader.dataset)
    ))

    return correct.float() / len(test_loader.dataset)




if __name__ == '__main__':

    EPOCH = 200
    BATCH_SIZE = 16 
    LR = 0.0001
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    #device = 'cpu'
    MILESTONES = [60, 120, 160]
    SAVE_EPOCH = 50
    warm = 1  #warm up training phase

    model = vgg16_bn()
    model.initialize()

    transform = transforms.Compose([
        transforms.CenterCrop(3000),
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize((0.174188,0.093467,0.036374),(0.256325,0.144939,0.068679))])

    train_data = MyDataset('./train.txt',transform = transform)
    test_data = MyDataset('./test.txt', transform = transform)

    train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=BATCH_SIZE, shuffle=True)

    optimizer = torch.optim.Adam(model.parameters(), lr=LR, betas=(0.9, 0.99))
    #optimizer = torch.optim.SGD(model.parameters(), lr=LR, momentum=0.9, weight_decay=5e-4)
    train_scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=MILESTONES, gamma=0.2) #learning rate decay
    iter_per_epoch = len(train_loader)
    warmup_scheduler = WarmUpLR(optimizer, iter_per_epoch * warm)

    checkpoint_path = os.path.join('checkpoint', 'VGG', 'first')
    if not os.path.exists(checkpoint_path):
        os.makedirs(checkpoint_path)
    checkpoint_path = os.path.join(checkpoint_path, '{net}-{epoch}-{type}.pth')
    print(checkpoint_path)
    best_acc = 0.0
    
    o = open('train_vgg.log','w')
    for epoch in range(1, EPOCH+1):

        if epoch > warm:
            train_scheduler.step(epoch)

        train(model, device, train_loader, optimizer, epoch, BATCH_SIZE)
        acc = eval_training(model, device, test_loader)

        if epoch > MILESTONES[1] and best_acc < acc:
            torch.save(model.state_dict(), checkpoint_path.format(net='VGG16', epoch=epoch, type='best'))
            best_acc = acc
            continue

        if not epoch % SAVE_EPOCH:
            torch.save(model.state_dict(), checkpoint_path.format(net='VGG16', epoch=epoch, type='regular'))

    o.close()
