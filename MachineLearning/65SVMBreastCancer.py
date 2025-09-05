import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousCancerDetection():
    df = load_breast_cancer()

    x = df.data
    y = df.target

    data = pd.DataFrame(x, columns = df.feature_names)
    data['target'] = y

    # print("Dimension of dataset is : ", df.shape)

    print("Classes : ", dict(zip(df.target_names, (0, 1))))

    scalar = StandardScaler()
    x_scaled = scalar.fit_transform(x)

    X_train, X_test, Y_train, Y_test = train_test_split(x_scaled, y, test_size = 0.2, random_state = 42)

    model = SVC(kernel = 'linear', C = 1)
    model.fit(X_train, Y_train)

    Y_predicted = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100
    print("Accuracy of model is : ", accuracy)

    conf_mat = confusion_matrix(Y_test, Y_predicted)
    print("Confusion matrix is : ")
    print(conf_mat)

def main():
    MarvellousCancerDetection()

if __name__ == "__main__":
    main()