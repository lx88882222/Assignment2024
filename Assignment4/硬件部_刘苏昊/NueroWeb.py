import numpy as np

class NeuroWeb:
    def __init__(self, layer_sizes):
        self.layer_sizes = layer_sizes
        self.weights = []
        self.biases = []
        self.num_layers = len(layer_sizes)
        #声明权值矩阵和偏置向量
        
        for i in range(1, self.num_layers):
            weight_matrix = np.random.randn(layer_sizes[i], layer_sizes[i-1])
            bias_vector = np.random.randn(layer_sizes[i], 1)
            #示例中的权值矩阵和偏置向量是随机生成的，实际应该根据训练数据进行初始化
            self.weights.append(weight_matrix)
            self.biases.append(bias_vector)
    
    def forward_spread(self, input_data):
        activations = [input_data]
        
        for i in range(1, self.num_layers):
            z = np.dot(self.weights[i-1], activations[i-1]) + self.biases[i-1]
            a = self.sigmoid(z)
            activations.append(a)
        return activations[-1]
    

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
        #sigmoid函数的实现，z是一个向量，对向量中的每个元素进行sigmoid运算
        
if __name__ == '__main__':
    layer_sizes = [2, 3, 1]
    input_data = np.random.randn(2, 1)
    net = NeuroWeb(layer_sizes)
    output = net.forward_spread(input_data)
    print(output)