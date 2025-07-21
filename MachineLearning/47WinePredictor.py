import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def WinePredictor(Dataset):
    df = pd.read_csv(Dataset)

    print("Data set loaded successfully ...")
    print(df.head())

    print("Dimesions of dataset is : ", df.shape)

    print("Number of missing values are : ")
    print( df.isnull().sum())

    # reomve missing values
    # df.dropna(inplace = True)

    # data visualization
    plt.figure(figsize = (10, 6))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Feature correlation heatmap")
    plt.show()

    # data for training model
    x = df.drop(columns = ['Class'])
    y = df['Class']

    print("Dimensions of features : ", x.shape)
    print("Dimension of labels : ", y.shape)
    
    # taking standard scaler values of x
    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    # training model
    X_train, X_test, Y_train, Y_test = train_test_split(x_scale, y, test_size = 0.2, random_state = 42)

    model = KNeighborsClassifier(n_neighbors = 5)

    model.fit(X_train, Y_train)

    # testing model
    Y_predicted = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

    print("Accuracy score : ", accuracy)

def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()