import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("iris.csv")

    X = df.iloc[:, [0, 1, 2, 3]].values
    print(X.shape)

    model = KMeans(n_clusters = 3, init = "k-means++", n_init = 10, random_state = 42)
    y_kmeans = model.fit_predict(X)

    print(y_kmeans.shape)

    print("Cluster of Setosa : 1")
    for i in range(10):
        print(X[i], y_kmeans[i])

    print("Cluster of Versicolor : 0")
    for i in range(51, 61):
        print(X[i], y_kmeans[i])

    print("Cluster of Virginica : 2")
    for i in range(101, 111):
        print(X[i], y_kmeans[i])

if __name__ == "__main__":
    main()