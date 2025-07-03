import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    df = pd.read_csv("iris.csv")    # data load
    print("Dataset loaded successfully...")

    print(df["variety"])

    df["variety"] = df["variety"].map({'Setosa' : 0, 'Versicolor' : 1, 'Virginica' : 2})    # data encode

    x = df.drop("variety", axis = 'columns')
    y = df["variety"]

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2)    # data split

    # used to split the data in four parts with 80% for training and 20% for testing.
    # X_train = 80% train independent variable, Y_train = 20% train dependent variable,
    # X_test = 20% test independent variable, Y_test = 20% test dependent variable

    print("Dimension of X_train is : ", X_train.shape)    # A
    print("Dimension of X_test is : ", X_test.shape)      # C
    print("Dimension of Y_train is : ", Y_train.shape)    # B
    print("Dimension of Y_test is : ", Y_test.shape)      # D

if __name__ == "__main__":
    main()