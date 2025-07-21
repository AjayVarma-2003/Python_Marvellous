import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def DataVisualization(dataset):
    plt.figure(figsize = (10, 8))

    sns.scatterplot(data = dataset, x = 'Head Size(cm^3)', y = 'Brain Weight(grams)', hue = 'Gender', palette = 'Set1')
    plt.title("Gender Predictor using head size and brain weight")
    plt.xlabel("Size of head in cm^3")
    plt.ylabel("Weight of brain in grams")
    plt.grid(True)
    plt.show()

def CalculateAccuracy(Y1, Y2):
    accuracy = (accuracy_score(Y1, Y2)) * 100
    return accuracy

def DisplayConfusionMatrix(Y1, Y2):
    conf_mat = confusion_matrix(Y1, Y2)
    print("Confusion Matrix is : ")
    print(conf_mat)

def DisplayClassificationReport(Y1, Y2):
    report = classification_report(Y1, Y2)
    print("Classification report is : ")
    print(report)

def Predictor(dataset):
    DataVisualization(dataset)

    data = dataset[['Head Size(cm^3)','Brain Weight(grams)']]
    target = dataset['Gender']

    X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size = 0.3)

    model = LogisticRegression()
    
    model.fit(X_train, Y_train)

    Y_predicted = model.predict(X_test)

    ret = CalculateAccuracy(Y_test, Y_predicted)
    print("Accuracy of model is : ", ret)

    DisplayConfusionMatrix(Y_test, Y_predicted)

    DisplayClassificationReport(Y_test, Y_predicted)

def main():
    df = pd.read_csv("MarvellousHeadBrain.csv")
    Predictor(df)

if __name__ == "__main__":
    main()