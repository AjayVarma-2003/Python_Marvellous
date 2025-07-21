import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def MarvellousAdvertise(Dataset):
    df = pd.read_csv(Dataset)

    print("Dataset sample is : ")
    print(df.head())

    print("Cleaning the dataset")
    df.drop(columns = ['Unnamed: 0'], inplace = True)
    print("Updated data set is : ")
    print(df.head())

    print("Missing values in each column")
    print(df.isnull().sum())

    print("Statistical summary of dataset is : ")
    print(df.describe())

    print("Correlational matrix")
    print(df.corr())

    print("Visual representation : ")
    plt.figure(figsize = (10, 5))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Marvellous Correlation heatmap")
    plt.show()

    sns.pairplot(df)
    plt.suptitle("Pairplot of features", y = 1.02)
    plt.show()

    x = df[['TV', 'radio', 'newspaper']]
    y = df['sales']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    model = LinearRegression()
    
    model.fit(X_train, Y_train)

    Y_predicted = model.predict(X_test)

    MSE = metrics.mean_squared_error(Y_test, Y_predicted)
    RMSE = metrics.root_mean_squared_error(Y_test, Y_predicted)
    R2 = metrics.r2_score(Y_test, Y_predicted)

    print("Mean squared error is : ", MSE)
    print("Root mean squared error is : ", RMSE)
    print("R-squre value is : ", R2)

    print("Model coefficient are : ")
    for col, coef in zip(x.columns, model.coef_):
        print(f"{col} : {coef}")

    print("Y intercept is : ", model.intercept_)

    plt.figure(figsize = (8, 5))
    plt.scatter(Y_test, Y_predicted, color = 'blue')
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.title("Marvellous Advertisment predictor")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()