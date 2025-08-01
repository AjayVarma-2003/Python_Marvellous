from sklearn.cluster import KMeans
import numpy as np

def main():
    print("Code to demonstrate concept of WCSS in KMeans ...")

    X = np.array([[1, 2], [1, 4], [1, 0], [1, 3], [10, 2], [10, 4], [10 ,0], [10, 3]])

    model = KMeans(n_clusters = 2, init = "k-means++", n_init = 10, random_state = 42)

    model.fit(X)
    print(model.inertia_)    # printing WCSS values.

if __name__ == "__main__":
    main()