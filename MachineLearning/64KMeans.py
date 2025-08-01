import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Border = "-" * 50
colmap = {1 :'r', 2 : 'g', 3 : 'b'}


def GenerateRandomCentroid(df):
    np.random.seed(200)
    k = 3
    centroids = {
        i + 1 : [np.random.randint(0, 80), np.random.randint(0, 80)]
        for i in range(k)
    }

    print(Border)
    print("Random centroids generated are : ")
    print(centroids)
    print(Border)

    return centroids

def plotfigure1(df, cent):
    fig = plt.figure(figsize = (5, 5))
    plt.scatter(df['x'], df['y'], color = 'k')

    for i in cent.keys():
        plt.scatter(*cent[i], color = colmap[i])

    plt.title("Dataset with random centroids")
    plt.xlim(0, 80)
    plt.ylim(0, 80)
    plt.show()

def assigncentroids(df, centroid):
    # Assignment - k clusters are created by associating each observation with the nearest centroid
    # calculate distance formula : sqrt((x1 - x2)^2 - (y1 - y2)^2)
    centroid_distance_col = 0
    for i in centroid.keys():
        df['distance_from_{}'.format(i)] = (
            np.sqrt(((df['x'] - centroid[i][0]) ** 2) - ((df['y'] - centroid[i][1]) ** 2))
        )
        centroid_distance_col = ['distance_from_{}'.format(i) for i in centroid.keys()]

    df['closest'] = df.loc[:, centroid_distance_col].idxmin(axis = 1)

    df['closest'] = df['closest'].map(lambda X: int(X.lstrip('distance_from_')))

    df['color'] = df['closest'].map(lambda X: colmap[X])

    return df

def main():
    df = pd.DataFrame({
        'x' : [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
        'y' : [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
    })

    print(Border)
    print("Data setup for training : ")
    print(df)
    print(Border)

    centroid = GenerateRandomCentroid(df)

    plotfigure1(df, centroid)

    print("Step 2: Assignment K clusters are created by associating each observation with nearest centroid")
    
    print("Before assignment dataset is : ")
    print(df.head())
    
    df = assigncentroids(df, centroid)

    print("First centroid : Red")
    print("Second centroid : Green")
    print("Third centroid : Blue")

    print("After assignment dataset is : ")
    print(df.head())

if __name__ == "__main__":
    main()