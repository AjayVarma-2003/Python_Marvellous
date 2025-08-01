import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def DiabetesPredictor(dataset):
    df = pd.read_csv(dataset)

    print(df.columns)
    print(df.head())
    print(df.shape)

    x = df.drop(columns = 'Outcome', axis = 1)
    y = df['Outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    model = LogisticRegression().fit(X_train, Y_train)

    Y_predicted = model.predict(X_test)

    print("Training accuracy using another method : ")
    print(model.score(X_train, Y_train) * 100)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

    print("Testing accuracy : ", accuracy)

def main():
    DiabetesPredictor("diabetes.csv")

if __name__ == "__main__":
    main()