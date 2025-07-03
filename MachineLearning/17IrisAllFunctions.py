import pandas as pd
from sklearn.model_selection import train_test_split

def LoadData(file_path):
    df = pd.read_csv(file_path)
    print("Dataset got loaded in memory successfully.")
    return df

def GetInformation(df):
    print("Information of loaded data set is : ")
    print("Shape of data set : ", df.shape)
    print("Columns of data set are : ", df.columns)
    print("Missing values : ", df.isnull().sum())

def EncodeData(df):
    df["variety"] = df["variety"].map({'Setosa' : 0, 'Versicolor' : 1, 'Virginica' : 2})
    return df

def Split_Feature_Label(df):
    x = df.drop("variety", axis = 1)
    y = df["variety"]

    return x, y

def Split(x, y, size = 0.2):
    return train_test_split(x, y, test_size = size)

def main():
    data = LoadData("iris.csv")
    print(data.head())

    GetInformation(data)

    print("Data after encoding : ")
    data = EncodeData(data)
    print(data.head())

    print("Splitting features and labels")
    independent, dependent = Split_Feature_Label(data)
    print(independent.head())
    print(dependent.head())

    X_train, X_test, Y_train, Y_test = Split(independent, dependent, 0.3)
    print("Dimension of X_train is : ", X_train.shape)
    print("Dimension of X_test is : ", X_test.shape)
    print("Dimension of Y_train is : ", Y_train.shape)
    print("Dimension of Y_test is : ", Y_test.shape)

if __name__ == "__main__":
    main()