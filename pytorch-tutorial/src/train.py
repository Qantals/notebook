# -*- coding: utf-8 -*-
# 作者：小土堆
# 公众号：土堆碎念

import torchvision
import torch
from torch.utils.tensorboard import SummaryWriter

from model import *
# 准备数据集
from torch import nn
from torch.utils.data import DataLoader

train_data = torchvision.datasets.CIFAR10(root="dataset", train=True, transform=torchvision.transforms.ToTensor(),
                                          download=True)
test_data = torchvision.datasets.CIFAR10(root="dataset", train=False, transform=torchvision.transforms.ToTensor(),
                                         download=True)

# length 长度
train_data_size = len(train_data)
test_data_size = len(test_data)
# 如果train_data_size=10, 训练数据集的长度为：10
print("训练数据集的长度为：{}".format(train_data_size))
print("测试数据集的长度为：{}".format(test_data_size))


# 利用 DataLoader 来加载数据集
train_dataloader = DataLoader(train_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)

# 创建网络模型
tudui = Tudui()

# 损失函数
loss_fn = nn.CrossEntropyLoss()

# 优化器
# learning_rate = 0.01
# 1e-2=1 x (10)^(-2) = 1 /100 = 0.01
learning_rate = 1e-2
optimizer = torch.optim.SGD(tudui.parameters(), lr=learning_rate)

# 设置训练网络的一些参数
# 记录训练的次数
total_train_step = 0
# 记录测试的次数
total_test_step = 0
# 训练的轮数
epoch = 10

# 添加tensorboard
writer = SummaryWriter("logs_train")

for i in range(epoch):
    print("-------第 {} 轮训练开始-------".format(i+1))

    # 训练步骤开始
    tudui.train()
    for batch, (X, y) in enumerate(train_dataloader):
        pred = tudui(X)
        loss = loss_fn(pred, y)

        # 优化器优化模型
        optimizer.zero_grad() # 梯度累计计算，需要清零
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            print("训练次数：{}, Loss: {}, this epoch: [{}/{}]".format(batch + 1, loss.item(), (batch + 1) * len(X), len(train_data)))
            writer.add_scalar("train_loss", loss.item(), batch)

    # 测试步骤开始
    tudui.eval()
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad(): # stop tracking gradient
        for data in test_dataloader:
            X, y = data
            pred = tudui(X)
            loss = loss_fn(pred, y)
            total_test_loss += loss.item()
            total_accuracy += (pred.argmax(1) == y).type(torch.float).sum().item()

    print("avg loss: {}".format(total_test_loss/len(test_dataloader)))
    print("整体测试集上的正确率: {}".format(total_accuracy/len(test_data)))
    writer.add_scalar("test_loss", total_test_loss, total_test_step)
    writer.add_scalar("test_accuracy", total_accuracy/len(test_data), total_test_step)
    total_test_step = total_test_step + 1

    torch.save(tudui, "tudui_{}.pth".format(i))
    print("模型已保存")

writer.close()
