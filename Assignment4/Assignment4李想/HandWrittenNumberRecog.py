'''
HandWrittenNumberRecog.py
手写数字识别
数据集：MNIST
网络：全连接神经网络
'''
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
import matplotlib.pyplot as plt


class Net(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(28*28, 64) #定义全连接层 输入为28*28 输出为64
        self.fc2 = torch.nn.Linear(64, 64) #定义全连接层 输入为64 输出为64
        self.fc3 = torch.nn.Linear(64, 64) #定义全连接层 输入为64 输出为64
        self.fc4 = torch.nn.Linear(64, 10) #定义全连接层 输入为64 输出为10 代表10个类别
    def forward(self, x):
        x = torch.nn.functional.relu(self.fc1(x)) #激活函数relu
        x = torch.nn.functional.relu(self.fc2(x)) #激活函数relu
        x = torch.nn.functional.relu(self.fc3(x)) #激活函数relu
        x = torch.nn.functional.log_softmax(self.fc4(x), dim=1) #激活函数log_softmax
        return x #形状为[batch_size, 10] 10代表10个类别


def get_data_loader(is_train):
    to_tensor = transforms.Compose([transforms.ToTensor()]) #将图片转换为tensor
    data_set = MNIST("", is_train, transform=to_tensor, download=True) #下载数据集
    return DataLoader(data_set, batch_size=15, shuffle=True) #返回数据加载器


def evaluate(test_data, net):
    n_correct = 0
    n_total = 0
    with torch.no_grad(): #不计算梯度
        for (x, y) in test_data: #(x, y)代表一个batch的中的数据，x为图片，y为标签
            outputs = net.forward(x.view(-1, 28*28)) #view函数将图片展平为[batch_size, 28*28]
            for i, output in enumerate(outputs):#遍历batch中的每一张图片
                if torch.argmax(output) == y[i]:#argmax函数返回最大值的索引，即预测的类别
                    n_correct += 1 #预测正确
                n_total += 1 #总数加1
    return n_correct / n_total


def main():

    train_data = get_data_loader(is_train=True) #获取训练数据，靠is_train参数控制
    test_data = get_data_loader(is_train=False) #获取测试数据，靠is_train参数控制
    net = Net() #实例化网络
    
    print("initial accuracy:", evaluate(test_data, net))#先测试一下初始的准确率，应该为0.1左右
    optimizer = torch.optim.Adam(net.parameters(), lr=0.001) #设置优化器，Adam优化器，学习率为0.001
    for epoch in range(5): #训练5个epoch
        for (x, y) in train_data:
            net.zero_grad() #梯度清零
            output = net.forward(x.view(-1, 28*28)) #前向传播
            loss = torch.nn.functional.nll_loss(output, y) #计算损失（或者说成本cost）
            loss.backward() #反向传播
            optimizer.step() #更新参数
        print("epoch", epoch, "accuracy:", evaluate(test_data, net)) #每个epoch测试一下准确率

    for (n, (x, _)) in enumerate(test_data): #测试一下前4张图片的预测结果
        if n > 3: #只显示前4张图片
            break
        predict = torch.argmax(net.forward(x[0].view(-1, 28*28)))
        plt.figure(n)
        plt.imshow(x[0].view(28, 28))
        plt.title("prediction: " + str(int(predict)))
    plt.show()


if __name__ == "__main__":
    main()
