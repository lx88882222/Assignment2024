import numpy as np

class NeuralNetwork:#所有权重和偏置都是随机初始化的（由于没有规则，所以不会得到有用的结果）
    def __init__(self, layers):
        """
        初始化神经网络
        :param layers: 一个列表，表示每层的神经元数量
        """
        self.layers = layers
        self.weights = [self._create_weight_matrix(layers[i], layers[i + 1]) for i in range(len(layers) - 1)]
        self.biases = [self._create_bias_vector(layers[i + 1]) for i in range(len(layers) - 1)]

    def _create_weight_matrix(self, input_size, output_size):
        """
        创建权重矩阵
        :param input_size: 输入神经元数量
        :param output_size: 输出神经元数量
        :return: 权重矩阵
        """
        return np.random.randn(input_size, output_size)

    def _create_bias_vector(self, output_size):
        """
        创建偏置向量
        :param output_size: 输出神经元数量
        :return: 偏置向量
        """
        return np.random.randn(output_size)

    def _sigmoid(self, z):
        """
        Sigmoid 激活函数
        :param z: 输入值
        :return: 激活后的值
        """
        return  np.exp(-np.logaddexp(0, -z))

    def forward(self, X):
        """
        向前传播
        :param X: 输入数据
        :return: 输出结果
        """
        a = X
        for weight, bias in zip(self.weights, self.biases):
            z = np.dot(a, weight) + bias
            a = self._sigmoid(z)
        return a