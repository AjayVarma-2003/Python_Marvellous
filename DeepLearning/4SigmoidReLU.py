import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    return (1 / (1 + math.exp(-z)))

def ReLUX(z):
    return max(0, z)

def Marvellous_neuron_forward(inputs, weights, bias):
    # Display inputs and weights
    print("Input (x) : ", inputs)
    print("Weights (w) : ", weights)
    print("bias (b) : ", bias)

    # Summation
    z = sum(w * x for w, x in zip(weights, inputs)) + bias
    print("Summation (z = w.x + b) : ", z)

    # Activation function sigmoid
    y_hat = sigmoid(z)
    print("Activation function : Sigmoid")
    print("Output : (y_hat = sigmoid(z)) : ", y_hat)

    # Activation function ReLU
    y_hat = ReLUX(z)
    print("Activatio function : ReLU")
    print("Output : (y_hat = ReLU(z)) : ", y_hat)

def plot_sigmoid_ReLU():
    z_values = np.linspace(-10, 10, 200)
    sigmoid_values = (1 / (1 + np.exp(-z_values)))
    relu_values = np.maximum(0, z_values)

    plt.figure(figsize = (8, 5))
    plt.plot(z_values, sigmoid_values, label = "Sigmoid", linewidth = 2, color = "blue")
    plt.plot(z_values, relu_values, label = "ReLU", linewidth = 2, color = "green")
    plt.axhline(y = 0, color = "black", linewidth = 0.5)
    plt.axhline(y = 1, color = "black", linewidth = 0.5)
    plt.axvline(x = 0, color = "gray", linestyle = "--")
    plt.title("Sigmoid vs ReLU Activation Functions", fontsize = 16)
    plt.xlabel("Summation (z)", fontsize = 14)
    plt.ylabel("Activation Output", fontsize = 14)
    plt.grid(True, linestyle = "--", alpha = 0.6)
    plt.legend()
    plt.show()

def main():
    # Example inputs and weights
    inputs = [1.0, 2.0, 3.0]
    weights = [0.6, 0.4, -0.2]
    bias = 0.5

    print("==== Sigmoid Neuron ====")
    Marvellous_neuron_forward(inputs, weights, bias)

    plot_sigmoid_ReLU()

if __name__ == "__main__":
    main()