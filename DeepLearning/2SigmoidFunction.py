import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    """
        Sigmoid function squashes values to (0, 1) range
        formula : (1/(1 + e ^ -z))
    """
    return (1 / (1 + math.exp(-z)))

def Marvellous_neuron_forward(inputs, weights, bias):
    # Display inputs and weight
    print("Input (x) : ", inputs)
    print("Weights (w) : ", weights)
    print("Bias (b) : ", bias)

    # Summation z = w.x + b
    z = sum(w * x for w, x in zip(weights, inputs)) + bias
    print("Summation (z = w.x + b) : ", z)

    # Activation function output
    y_hat = sigmoid(z)
    print("Activation function : Sigmoid ")
    print("Output (y_hat = sigmoid(z)) : ", y_hat)

    return z, y_hat

def plot_sigmoid():
    z_values = np.linspace(-10, 10, 200)    # range of z values
    sigmoid_values = (1 / (1 + np.exp(-z_values)))

    plt.figure(figsize = (8, 5))
    plt.plot(z_values, sigmoid_values, label = "Sigmoid", linewidth = 2, color = "blue")
    plt.axhline(y = 0, color = "black", linewidth = 0.5)
    plt.axhline(y = 1, color = "black", linewidth = 0.5)
    plt.axvline(x = 0, color = "gray", linestyle = "--")
    plt.title("Sigmoid Activation Function", fontsize = 14)
    plt.xlabel("Summation (z)", fontsize = 14)
    plt.ylabel("Activatio Output", fontsize = 14)
    plt.grid(True, linestyle = "--")
    plt.legend()
    plt.show()

def main():
    # Example inputs and weights
    inputs = [1.0, 2.0, 3.0]
    weights = [0.6, 0.4, 0.2]
    bias = 0.5

    z, y_hat = Marvellous_neuron_forward(inputs, weights, bias)

    # plot sigmoid curve
    plot_sigmoid()

if __name__ == "__main__":
    main()