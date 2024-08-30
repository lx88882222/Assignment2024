import numpy
from enum import Enum

    
def sigmoid(x):
    return [1/(1+numpy.exp(-i)) for i in x]
def sigmoid_derivative(x):
    return [numpy.exp(-i)/(1+numpy.exp(-i))**2 for i in x]
def softmax(x):
    return [numpy.exp(i) for i in x]/sum([numpy.exp(i) for i in x])
def softmax_derivative(x):
    derivative = numpy.zeros((len(x),len(x)))
    for i in range(len(x)):
        for j in range(len(x)):
            if i==j:
                derivative[i][j]=numpy.exp(x[i])*(sum([numpy.exp(i) for i in x])-numpy.exp(i))/(sum([numpy.exp(i) for i in x]))**2
            else:
                derivative[i][j]=-numpy.exp(x[i])*numpy.exp(x[j])/(sum([numpy.exp(i) for i in x]))**2
    return derivative
def cross_entropy_error(predicted, target):
    return -numpy.sum([target[i]*numpy.log(predicted[i]) for i in range(len(predicted))])
def cross_entropy_error_derivative(predicted, target):
    return [-(target[i]/predicted[i]) for i in range(len(predicted))]
def mean_squared_error(predicted, target):
    return numpy.sum([(predicted[i]-target[i])**2 for i in range(len(predicted))])
def mean_squared_error_derivative(predicted, target):
    return [2*(predicted[i]-target[i]) for i in range(len(predicted))]
# class ActivationFunction(Enum):
#     SIGMOID = 1
#     SOFTMAX = 2

# ActivationFunction.SIGMOID.value = sigmoid
# ActivationFunction.SIGMOID.derivative = sigmoid_derivative
# ActivationFunction.SOFTMAX.value = softmax
# ActivationFunction.SOFTMAX.derivative = softmax_derivative

# class LossFunction(Enum):
#     CROSS_ENTROPY = 1
#     MEAN_SQUARED_ERROR = 2

# LossFunction.CROSS_ENTROPY.value = cross_entropy_error
# LossFunction.CROSS_ENTROPY.derivative = cross_entropy_error_derivative
# LossFunction.MEAN_SQUARED_ERROR.value = cross_entropy_error
# LossFunction.MEAN_SQUARED_ERROR.derivative = mean_squared_error_derivative

