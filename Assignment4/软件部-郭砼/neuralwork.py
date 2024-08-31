import numpy as np

# 定义激活函数
def relu(x):
    return np.maximum(0, x)

# 定义神经网络的类
class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_sizes, output_size):
        self.weights = []
        self.biases = []
        self.weights.append(np.random.randn(input_size, hidden_sizes[0]))
        self.biases.append(np.random.randn(hidden_sizes[0]))
        for i in range(1, len(hidden_sizes)):
            self.weights.append(np.random.randn(hidden_sizes[i-1], hidden_sizes[i]))
            self.biases.append(np.random.randn(hidden_sizes[i]))
        self.weights.append(np.random.randn(hidden_sizes[-1], output_size))
        self.biases.append(np.random.randn(output_size))
    

    def forward(self, x):
        for i in range(len(self.weights) - 1):
            x = relu(np.dot(x, self.weights[i]) + self.biases[i])
        output = np.dot(x, self.weights[-1]) + self.biases[-1]
        return output


if __name__ == "__main__":
    input_size = 3  
    hidden_sizes = [4, 5] 
    output_size = 2  
    network = SimpleNeuralNetwork(input_size, hidden_sizes, output_size)
    x = np.array([1.0, 0.5, -1.2])
    output = network.forward(x)
    print(x)
    print(output)
