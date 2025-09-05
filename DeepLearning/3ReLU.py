import matplotlib.pyplot as plt
import numpy as np

def ReLUX(z):
    return max(0, z)

def Marvellous_neuron_forward(inputs, weights, bias):
    # Display inputs and weights
    print("Inputs (x) : ", inputs)
    print("Weights (w) : ", weights)
    print("Bias (b) : ", bias)

    # Summation z = w.x + b
    z = sum(w * x for w, x in zip(weights, inputs)) + bias
    print("Summation (z = w.x + b) : ", z)

    # Activation function output
    y_hat = ReLUX(z)

    print("Activation function : ReLU")
    print("Output : (y_hat = ReLU(z)) : ", y_hat)

def plot_relu():
    z_values = np.linspace(-10, 10, 200)
    relu_values = np.maximum(0, z_values)

    plt.figure(figsize = (8, 5))
    plt.plot(z_values, relu_values, label = "ReLU", linewidth = 2, color = "green")
    plt.axhline(y = 0, color = "black", linewidth = 0.5)
    plt.axvline(x = 0, color = "gray", linestyle = "--")
    plt.title("ReLU Activation function", fontsize = 16)
    plt.xlabel("Summation (z)", fontsize = 14)
    plt.ylabel("Activation Output", fontsize = 14)
    plt.grid(True, linestyle = "--", alpha = 0.6)
    plt.legend()
    plt.show()

def main():
    # Example weights and inputs
    inputs = [1.0, 2.0, 3.0]
    weights = [0.6, 0.4, -0.2]
    bias = 0.5

    Marvellous_neuron_forward(inputs, weights, bias)

    plot_relu()

if __name__ == "__main__":
    main()