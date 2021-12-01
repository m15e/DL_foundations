
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/02_fully_connected.ipynb
from exp.nb_01 import *

def get_data():
    mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
    x_set = mnist_trainset.data.reshape(mnist_trainset.data.shape[0], 784)
    x_train, x_valid = x_set[:50000], x_set[50000:]
    y_train, y_valid = mnist_trainset.targets[:50000], mnist_trainset.targets[50000:]
    print(x_train.shape, y_train.shape, x_valid.shape, y_valid.shape)
    print(x_train.type(), y_train.type(), x_valid.type(), y_valid.type())

    return x_train, y_train, x_valid, y_valid

def normalize(x, m, s): return (x-m)/s

def test_near_zero(a, tol=1e-3): assert a.abs() < tol, f"Near zero: {a}"

from torch.nn import init

#  we use output.squeeze to remove a given unit axis - we add a -1 param in case the we have input size 1
def mse(output, targ): return (output.squeeze(-1)-targ).pow(2).mean()