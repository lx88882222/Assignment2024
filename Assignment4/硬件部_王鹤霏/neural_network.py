import numpy as np
# import my_math
import my_math as mm

class NeuralNetwork:
    def __init__(self, arguments):
        self.input = arguments["input"]
        self.hidden = arguments["hidden"]
        self.neural_count = arguments["neural_count"]
        self.output = arguments["output"]
        self.learning_rate = arguments["learning_rate"]
        self.batch_size = arguments["batch_size"]
        self.epochs = arguments["epochs"]
        # self.loss_function = mm.LossFunction("CROSS_ENTROPY").value
        # self.activation_function = mm.ActivationFunction("SIGMOID").value
        # self.loss_function = mm.LossFunction(loss_function).value
        # self.activation_function = mm.ActivationFunction(activation_function).value
        # self.loss_function_derivative = mm.LossFunction(loss_function).derivative
        # self.activation_function_derivative = mm.ActivationFunction(activation_function).derivative
        self.parameters = np.random.rand(self.input, self.hidden)
        self.weight_in = np.random.rand(self.input+1, self.neural_count)
        self.weight_out = np.random.rand(self.neural_count+1, self.output)
        self.weight_hidden = np.random.rand(self.hidden, self.neural_count+1, self.neural_count)

    def forward(self,input):
        hidden_layer = np.zeros([self.hidden+1, self.neural_count])
        input = np.append(input,1)
        print(f"dimesion of input: {input.shape}")
        hidden_layer[0] = np.dot(input, self.weight_in)
        for i in range(self.hidden):
            hidden_layer[i+1] = np.dot(np.append(hidden_layer[i],1), self.weight_hidden[i])
        output = np.dot(np.append(hidden_layer[self.hidden],1), self.weight_out)
        return output
    
    def backward(self,input,target):
        pass

def main():
    # Set arguments
    arguments = {
        "input": 5,
        "hidden": 3,
        "neural_count": 3,
        "output": 2,
        "learning_rate": 0.1,
        "batch_size": 10,
        "epochs": 100,
        # "loss_function": "CROSS_ENTROPY",
        # "activation_function": "SIGMOID"
    }
    # print("Default arguments: ")
    # print(arguments)
    # for i in range(len(arguments)):
    #     input_value = input("Enter value for "+list(arguments.keys())[i]+": ")
    #     if input_value:
    #         arguments[list(arguments.keys())[i]] = eval(input_value)
    #     else:
    #         pass
    # print("Arguments set to: ")
    # print(arguments)
    # initialize neural network
    nn = NeuralNetwork(arguments)
    input_data = [1,2,3,4,5]
    print(nn.forward(input_data))
    print("Parameters: ")
    print("weight_in: ")
    print(nn.weight_in)
    print("weight_out: ")
    print(nn.weight_out)
    print("weight_hidden: ")
    print(nn.weight_hidden)

if __name__ == '__main__':
    main()