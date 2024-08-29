# 配置环境
import matplotlib.pyplot as plt
import pandas as pd
import torch.nn as nn
import numpy as np
import torch.optim
from dataset import Use_Dataset
from sklearn.model_selection import train_test_split


# ---------------- 准备数据 -------------------

file_path = r'D:\垂直领域\dataset\2024_8_26\data\converted_file.json'

x, y = Use_Dataset(file_path)

x_tensor = torch.tensor(x, dtype=torch.float)  # 转化为 torch.tensor 格式
y_tensor = torch.tensor(y, dtype=torch.float)

print(x_tensor.shape)
print(y_tensor.shape)

X_train, X_test, y_train, y_test = train_test_split(x_tensor, y_tensor, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)


# ---------------- 搭建模型 -------------------
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, seq_l):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)  # lstm layer
        self.linear = nn.Linear(hidden_size * seq_l, output_size)  # linear layer

    def forward(self, x_in):
        x_in, _ = self.lstm(x_in)
        b, s, f = x_in.shape  # batch_size, sequence_length, feature_number
        x_in = x_in.reshape(b, s * f)
        x_in = self.linear(x_in)
        return x_in


# ---------------- 初始化、实例化 -------------------
input_size = 10
hidden_size =12
output_size =10
seq_l = 6

net = LSTM(input_size, hidden_size, output_size, seq_l)  # 网络

loss_function = nn.MSELoss()  # 损失函数

optimizer = torch.optim.Adam(net.parameters())  # 优化器

epoch = 1000  # 最大迭代次数


# ---------------- 训练 -------------------
for i in range(epoch):
    optimizer.zero_grad()  # 梯度清零
    y_predict = net(x_tensor)  # 预测
    loss = loss_function(y_predict, y_tensor)  # 计算损失
    print(loss)
    loss.backward()  # 损失回传，计算梯度
    optimizer.step()  # 根据梯度更新模型

