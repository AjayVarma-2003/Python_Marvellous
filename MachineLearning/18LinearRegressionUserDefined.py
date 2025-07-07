import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # load data
    x = [1, 2, 3, 4, 5]
    y = [3, 4, 2, 4, 5]

    print("Values of Independent variables : ", x)
    print("Values of dependent variables : ", y)

    xsum = 0
    ysum = 0

    for i in range(len(x)):
        xsum = xsum + x[i]
        ysum = ysum + y[i]

    mean_x = xsum / len(x)
    mean_y = ysum / len(y)

    print("Mean of x is : ", mean_x)
    print("Mean of y is : ", mean_y)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()