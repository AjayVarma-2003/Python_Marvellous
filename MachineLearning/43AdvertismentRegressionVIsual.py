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

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()