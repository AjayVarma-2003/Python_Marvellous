import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score, confusion_matrix

def MarvellousHeadBrainLinear(Dataset):
    Line = "*" * 50
    df = pd.read_csv(Dataset)

    print(Line)
    print("First few records of the dataset are : ")
    print(Line)
    print(df.head())
    print(Line)
    
    print("Statistical information of dataset : ")
    print(Line)
    print(df.describe())
    print(Line)

    x = df[['Head Size(cm^3)']]
    y = df[['Brain Weight(grams)']]

    print("Independent variables are : Head Size")
    print("Dependent varibales are : Brain Weight")

    print("Total records in dataset are : ", df.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
    print("Dimensions of training dataset : ", X_train.shape)
    print("Dimension of testing dataset : ", X_test.shape)

    model = LinearRegression()

    model.fit(X_train, Y_train)

    Y_predicted = model.predict(X_test)

    mse = mean_squared_error(Y_test, Y_predicted)

    rmse = root_mean_squared_error(Y_test, Y_predicted)    # square root of mse

    r2 = r2_score(Y_test, Y_predicted)

    print("Mean squared error is : ", mse)
    print("Root mean squared error is : ", rmse)
    print("R-square score is : ", r2)

def main():
    MarvellousHeadBrainLinear("MarvellousHeadBrain.csv")

if __name__ == "__main__":
    main()