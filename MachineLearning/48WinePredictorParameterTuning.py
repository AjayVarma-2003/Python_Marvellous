import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def WinePredictor(Dataset):
    df = pd.read_csv(Dataset)

    print("Data set loaded successfully ...")

    print("Number of missing values are : ")
    print( df.isnull().sum())

    # reomve missing values
    # df.dropna(inplace = True)

    # data for training model
    x = df.drop(columns = ['Class'])
    y = df['Class']

    
    # taking standard scaler values of x
    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    # training model
    X_train, X_test, Y_train, Y_test = train_test_split(x_scale, y, test_size = 0.2, random_state = 42)

    accuracy_scores = []
    k_range = range(3, 21)

    for k in k_range:    # parameter tuning
        model = KNeighborsClassifier(n_neighbors = k)

        model.fit(X_train, Y_train)

        # testing model
        Y_predicted = model.predict(X_test)

        accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

        print("Value of K is : ", k)

        accuracy_scores.append(accuracy)

    print(accuracy_scores)
    

def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()