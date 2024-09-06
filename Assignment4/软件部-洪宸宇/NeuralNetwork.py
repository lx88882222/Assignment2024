# 利用numpy实现一个简单的神经网络（仅向前传播）
import numpy as np


class NeuralNetwork:
    def __init__(self, layers):
        # 利用传入的层数列表初始化神经网络
        self.layers = layers
        # 初始化权重和偏置
        self.weights = [np.random.randn(layers[i + 1], layers[i]) for i in range(len(layers) - 1)]
        self.biases = [np.random.randn(layers[i + 1], 1) for i in range(len(layers) - 1)]

    # 定义激活函数
    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    # 定义向前传播
    def forward(self, x):
        for weight, bias in zip(self.weights, self.biases):
            x = self.sigmoid(np.dot(weight, x) + bias)
        return x


# 测试
if __name__ == '__main__':
    # 定义一个3层的神经网络，输入层3个神经元，隐藏层5个神经元，输出层2个神经元
    nn = NeuralNetwork([3, 5, 2])

    # 输入数据3*1
    input = np.array([[0.1], [0.2], [0.3]])

    # 计算结果2*1
    output = nn.forward(input)
    print("Output:", output)
