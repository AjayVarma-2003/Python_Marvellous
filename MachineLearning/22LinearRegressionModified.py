import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.set_printoptions(legacy = '1.25')    # to avoid printing like np.float(2.8) etc etc.

def MeanValue(value1, value2):
    mean1 = np.mean(value1)
    mean2 = np.mean(value2)

    return mean1, mean2

def Slope(value1, value2, mean1, mean2):
    # formula to find slope of line
    # slope = summation((x-x_mean) * (y-y_mean)) / summation(x-x_mean) ** 2
    # in this function x = value1, x_mean = mean1, y = value2, y_mean = mean2
    result = 0
    numerator = 0
    denominator = 0

    for i in range(len(value1)):
        numerator = numerator + ((value1[i] - mean1) * (value2[i] - mean2))
        denominator = denominator + (value1[i] - mean1) ** 2

    result = numerator / denominator

    return result

def Y_intercept(mean1, mean2, slope):
    # y = mx + C
    # C is y_intercept
    result = 0
    
    result = mean2 - (slope * mean1)

    return result

def PlotGraph(x, y_pre, value1, value2):
    plt.plot(x, y_pre, color = "blue", label = "Regression line")
    plt.scatter(value1, value2, color = "red", label = "Actual values")

    plt.xlabel("Independent variable")
    plt.ylabel("Dependent variable")

    plt.legend()
    plt.show()

def CalculateRsquare(y_pre, mean, value):
    # formula to calculate R^2 is : 
    # R^2 = summation(y_pred - y_mean) ** 2 / summation(y - y_mean) ** 2
    result = 0
    numerator = 0
    denominator = 0

    for i in range(len(value)):
        numerator = numerator + ((y_pre[i] - mean) ** 2)
        denominator = denominator + ((value[i] - mean) ** 2)

    result = numerator / denominator 

    return result 

def MarvellousPredictor():
    # Load data
    x = [1, 2, 3, 4, 5]
    y = [3, 4, 2, 4, 5]

    print("Values of independent variable is : ", x)
    print("Values of dependent variable is : ", y)

    x_mean, y_mean = MeanValue(x, y)

    print("Mean value of independent variables is : ", x_mean)
    print("Mean value of dependent variables is : ", y_mean)

    # calculate slope of line.
    m = Slope(x, y, x_mean, y_mean)
    print("Slope of line is : ", m)

    # calculate y-intercept
    C = Y_intercept(x_mean, y_mean, m)
    print("Y-intercept of line is : ", C)

    # plot graph
    X = np.linspace(1, 6, len(x))    # start, end, number of samples to generate
    
    Y_Predicted = []
    for i in range(len(x)):
        sum = 0
        sum = C + (m * x[i])
        Y_Predicted.append(sum)

    print(Y_Predicted)

    PlotGraph(X, Y_Predicted, x, y)

    # calculate R square value
    Rsquare = CalculateRsquare(Y_Predicted, y_mean, y)
    print("Value of R-square is : ", Rsquare)    # 0.3076923076923078 = 0.31

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()