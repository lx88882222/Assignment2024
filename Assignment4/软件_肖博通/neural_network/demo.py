from nn import NeuralNetwork
import numpy as np

# 示例用法
def main():
    # 定义神经网络结构，例如 3 层：输入层 2 个神经元，隐藏层 3 个神经元，输出层 1 个神经元
    layers = [2, 3, 1]
    # 初始化神经网络
    nn = NeuralNetwork(layers)
    
    # 创建一个示例输入
    X = np.array([[0.5, 0.1]])
    
    # 进行向前传播
    output = nn.forward(X)
    print("Output:", output)

if __name__ == "__main__":
    main()