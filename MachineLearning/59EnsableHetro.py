import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier

def DiabetesPredictor(dataset):
    df = pd.read_csv(dataset)

    x = df.drop(columns = 'Outcome', axis = 1)
    y = df['Outcome']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    X_train, X_test, Y_train, Y_test = train_test_split(x_scale, y, test_size = 0.2, random_state = 42)

    model1 = LogisticRegression()
    model2 = DecisionTreeClassifier(max_depth = 8)
    model3 = KNeighborsClassifier(n_neighbors = 5)

    voting = VotingClassifier(
        estimators = [
            ('lr', model1),
            ('dt', model2),
            ('knn', model3)
        ],
        voting = 'hard'
    )

    voting.fit(X_train, Y_train)
    Y_predicted = voting.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100
    print("Accuracy score of model is : ", accuracy)

    report = classification_report(Y_test, Y_predicted)
    print("Classification report is : ")
    print(report)

def main():
    DiabetesPredictor("diabetes.csv")

if __name__ == "__main__":
    main()