import numpy as np

class NeuralNetwork:
    # layer_sizes: 神经网络各层的神经元个数，
    # 例如[3, 5, 2]表示输入层有3个神经元，隐藏层有5个神经元，输出层有2个神经元
    # activation_function: 激活函数，可选'relu'或'sigmoid'
    # 例如activation_function='relu'表示使用ReLU激活函数
    # 例如activation_function='sigmoid'表示使用Sigmoid激活函数

    # 实例化一个神经网络对象
    # 例如nn = NeuralNetwork([3, 5, 2], activation_function='relu')
    # 表示创建一个输入层有3个神经元，隐藏层有5个神经元，输出层有2个神经元的神经网络，
    # 使用ReLU激活函数
    # 调用forward方法进行前向传播
    # 例如output = nn.forward(X)表示对输入X进行前向传播，得到输出output
    def __init__(self, layer_sizes, activation_function='relu'):
        self.layer_sizes = layer_sizes
        self.activation_function = activation_function
        self.weights = []
        self.biases = []
        self._initialize_parameters()
    
    def _initialize_parameters(self):
        for i in range(len(self.layer_sizes) - 1):
            self.weights.append(
                np.random.randn(
                    self.layer_sizes[i], self.layer_sizes[i + 1]) * 0.01)
            self.biases.append(np.zeros((1, self.layer_sizes[i + 1])))
    
    def _relu(self, z):
        return np.maximum(0, z)
    
    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def _activation(self, z):
        if self.activation_function == 'relu':
            return self._relu(z)
        elif self.activation_function == 'sigmoid':
            return self._sigmoid(z)
        else:
            raise ValueError("Unsupported activation function")

    def forward(self, X):
        self.activations = [X]
        self.zs = []
        A = X
        
        for w, b in zip(self.weights, self.biases):
            Z = np.dot(A, w) + b
            self.zs.append(Z)
            A = self._activation(Z)
            self.activations.append(A)
        
        return A


# 示例：创建一个具有输入层、一个隐藏层和输出层的神经网络
layer_sizes = [3, 5, 2]  
# 输入层有3个神经元，隐藏层有5个神经元，输出层有2个神经元
nn = NeuralNetwork(layer_sizes, activation_function='relu')

# 测试前向传播
X = np.array([[0.1, 0.2, 0.3]])
output = nn.forward(X)
print("网络输出：", output)
