import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("iris.csv")

    X = df.iloc[:, [0, 1, 2, 3]].values

    WCSS = []

    for k in range(1, 11):
        model = KMeans(n_clusters = k, init = "k-means++", n_init = 10, random_state = 42)

        model.fit(X)
        
        print(f"Value of WCSS when number of cluster is {k} : {model.inertia_}")
        WCSS.append(model.inertia_)

    plt.plot(range(1, 11), WCSS, marker = 'o')
    plt.title("Elbow Method for KMeans")
    plt.xlabel("Value of k")
    plt.ylabel("Within cluster sum of square")  
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()