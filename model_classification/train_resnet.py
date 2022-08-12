# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

from model.MyDataSet import MyDataset
from model.ResNet import resnet152
import torch
import torch.nn as nn
from torchvision import transforms
from torch.utils.data import DataLoader
from torch.autograd import Variable



def train(model, device, train_loader, optimizer, epoch, batch_size):

    model.train()
    for batch_index, (images, labels) in enumerate(train_loader):
        #print(images.shape)
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


def eval_training(model, device, test_loader):
    model.eval()

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
        test_loss / len(test_loader.dataset),
        correct.float() / len(test_loader.dataset)
    ))

    return correct.float() / len(test_loader.dataset)




if __name__ == '__main__':

    EPOCH = 200
    BATCH_SIZE = 32
    LR = 0.001
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    MILESTONES = [60, 120, 160]
    SAVE_EPOCH = 100

    model = resnet152()
    #model.initialize()

    transform = transforms.Compose([
        transforms.CenterCrop(3000),
        transforms.Resize(224),
        transforms.ToTensor()])

    train_data = MyDataset('./train.txt',transform = transform)
    test_data = MyDataset('./test.txt', transform = transform)

    train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=BATCH_SIZE, shuffle=True)

    optimizer = torch.optim.Adam(model.parameters(), lr=LR, betas=(0.9, 0.99))

    checkpoint_path = os.path.join('checkpoint', 'ResNet', 'first')
    if not os.path.exists(checkpoint_path):
        os.makedirs(checkpoint_path)
    checkpoint_path = os.path.join(checkpoint_path, '{net}-{epoch}-{type}.pth')
    print(checkpoint_path)
    best_acc = 0.0
    for epoch in range(1, EPOCH+1):
        train(model, device, train_loader, optimizer, epoch, BATCH_SIZE)
        acc = eval_training(model, device, test_loader)

        if epoch > MILESTONES[1] and best_acc < acc:
            torch.save(model.state_dict(), checkpoint_path.format(net='ResNet', epoch=epoch, type='best'))
            best_acc = acc
            continue

        if not epoch % SAVE_EPOCH:
            torch.save(model.state_dict(), checkpoint_path.format(net='ResNet', epoch=epoch, type='regular'))
