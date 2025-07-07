import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # load data
    x = [1, 2, 3, 4, 5]
    y = [3, 4, 2, 4, 5]

    print("Values of Independent variables : ", x)
    print("Values of dependent variables : ", y)

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    print("Mean of x is : ", mean_x)
    print("Mean of y is : ", mean_y)

    n = len(x)

    numerator = 0
    denominator = 0
    
    # y = mx + c
    for i in range(n):
        numerator = numerator + (x[i] - mean_x) * (y[i] - mean_y)
        denominator = denominator + (x[i] - mean_x) ** 2

    m = numerator / denominator
    print("Slope of line is : ", m)

    c = mean_y - (m * mean_x)
    print("Value of y-intercept of line is : ", c)

    X = np.linspace(1, 6, n)    # start, stop, number of samples
    Y = c + m * X
    print(Y)

    plt.plot(X, Y, color = "blue", label = "Regression Line")
    plt.scatter(x, y, color = "red", label = "Scatter plot")
    plt.xlabel("X : Independent Varibale")
    plt.ylabel("Y : Dependent Variable")

    plt.legend()
    plt.show()

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()