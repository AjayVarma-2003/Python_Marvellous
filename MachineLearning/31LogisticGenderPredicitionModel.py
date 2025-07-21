import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def MarvellousLogistic(datasetpath):
    df = pd.read_csv(datasetpath)

    print("Dimension of dataframe is : ", df.shape)
    print("Initial data is : ")
    print(df.head())

    df['Gender'] = df['Gender'].map({'Female' : 0, 'Male' : 1})

    print("encoded data is : ")
    print(df.head())

    plt.figure(figsize = (10, 8))
    
    sns.scatterplot(data = df, x = "Height", y = "Weight", hue = "Gender", palette = "Set1")
    plt.title("Marvellous Weight Height predictor")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.grid(True)
    plt.show()

    x = df[['Height', 'Weight']]
    y = df["Gender"]

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    model = LogisticRegression()

    model.fit(X_train, Y_train)

    Y_predicted = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100

    print("Accuracy is : ", accuracy)

    Conf_Matrix = confusion_matrix(Y_test, Y_predicted)
    print("Confusion matrix is : ")
    print(Conf_Matrix)

    report = classification_report(Y_test, Y_predicted)
    print("Classification report is : ")
    print(report)

def main():
    MarvellousLogistic("weight-height.csv")

if __name__ == "__main__":
    main()