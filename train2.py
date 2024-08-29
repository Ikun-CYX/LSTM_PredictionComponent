# 配置环境
import matplotlib.pyplot as plt
import pandas as pd
import torch.nn as nn
import numpy as np
import torch.optim


# ---------------- 准备数据 -------------------
data = pd.read_csv(r'D:\垂直领域\dataset\2024_8_26\data_test\Hospital1.csv')  # 读取csv文件
data = np.array(data['RATE'])  # 提取占有率
seq_l = 6  # 回溯及预测步长，其间隔为 5min


# 构造 rnn 模型数据结构
def rnn_data(sequence, length):
    output_sequence = np.zeros([sequence.shape[0]-length, length, 1])  # [batch, seq, feature]
    output_y = np.zeros([sequence.shape[0]-length, 1])
    for i in range(sequence.shape[0] - length):
        output_sequence[i, :, 0] = sequence[i:(i+length)]
        output_y[i, 0] = sequence[i+length]
    return output_sequence, output_y

print(data.shape)
x, y = rnn_data(data, seq_l)

# print(x)
# print(y)
print(x.shape)
print(y.shape)
1/0

x_tensor = torch.tensor(x, dtype=torch.float)  # 转化为 torch.tensor 格式
y_tensor = torch.tensor(y, dtype=torch.float)


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
net = LSTM(1, 12, 1, seq_l)  # 网络
loss_function = nn.MSELoss()  # 损失函数
optimizer = torch.optim.Adam(net.parameters())  # 优化器
epoch = 1000  # 最大迭代次数


# ---------------- 训练 -------------------
for i in range(epoch):
    optimizer.zero_grad()  # 梯度清零
    y_predict = net(x_tensor)  # 预测
    loss = loss_function(y_predict, y_tensor)  # 计算损失
    loss.backward()  # 损失回传，计算梯度
    optimizer.step()  # 根据梯度更新模型

 # 拟合曲线图
    if (i+1) % 10 == 0:
        print('loss =', loss.item())
        x_plot = x_tensor.detach().numpy()
        y_predict_plot = y_predict.detach().numpy()
        y_plot = y_tensor.detach().numpy()
        plt.clf()
        plt.plot(y_plot, label='original')
        plt.plot(y_predict_plot, label='predicted')
        plt.legend()
        plt.tight_layout()
        plt.pause(0.5)
        plt.ioff()