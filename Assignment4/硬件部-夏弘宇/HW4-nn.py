import numpy as np

class NeuralNetwork:
    def __init__(self, layer_sizes):
        self.layer_sizes = layer_sizes
        self.weights = []
        self.biases = []
        for i in range(1, len(layer_sizes)):
            self.weights.append(
                np.random.randn(layer_sizes[i], layer_sizes[i-1]))
            self.biases.append(np.random.randn(layer_sizes[i], 1))
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def forward(self, x):
        for b, w in zip(self.biases, self.weights):
            x = self.sigmoid(np.dot(w, x) + b)
        return x

if __name__ == '__main__':
    layer_sizes = input("Enter the number of neurons in each layer: ").split()
    layer_sizes = [int(i) for i in layer_sizes]
    nn = NeuralNetwork(layer_sizes)
    x = input("Enter the input vector: ").split()
    x = [float(i) for i in x]
    x = np.array(x).reshape(len(x), 1)
    print(f"Output:{nn.forward(x)}")
    