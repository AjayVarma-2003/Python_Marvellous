import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousTitanicLogistic(Dataset):
    df = pd.read_csv(Dataset)

    print("Data set loaded successfully ...")
    print(df.head())

    print("Dimesions of dataset is : ", df.shape)

    df.drop(columns = ['Passengerid', 'zero'], axis = 1, inplace = True)
    print("Dimesion of dataset after droping is : ", df.shape)

    print("Number of missing values are : ")
    print( df.isnull().sum())

    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])    # handling missing values
    print("Number of missing values after handling it : ")
    print( df.isnull().sum())

    # data visualization
    plt.figure()
    target = "Survived"
    sns.countplot(data = df,x = target).set_title("Survived vs Non Survived")
    plt.show()

    plt.figure()
    target = "Survived"
    sns.countplot(data = df, x = target, hue = 'Sex').set_title("Survived vs Non Survived based on gender")
    plt.show()

    plt.figure()
    target = "Survived"
    sns.countplot(data = df, x = target, hue = 'Pclass').set_title("Survived vs Non Survived based of Pclass")
    plt.show()

    plt.figure()
    df['Age'].plot.hist().set_title("Age report")
    plt.show()

    plt.figure()
    df['Fare'].plot.hist().set_title("Fare report")
    plt.show()
    
    plt.figure(figsize = (10, 6))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Feature correlation heatmap")
    plt.show()

    # data for training model
    x = df.drop(columns = ['Survived'])
    y = df['Survived']

    print("Dimensions of features : ", x.shape)
    print("Dimension of labels : ", y.shape)
    
    # taking scaler values of x
    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    # training model
    X_train, X_test, Y_train, Y_test = train_test_split(x_scale, y, test_size = 0.2, random_state = 42)

    model = LogisticRegression()

    model.fit(X_train, Y_train)

    # testing model
    Y_predicted = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

    con_matrix = confusion_matrix(Y_test, Y_predicted)

    print("Accuracy is : ", accuracy)
    print("Confusion matrix is : ")
    print(con_matrix)

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()