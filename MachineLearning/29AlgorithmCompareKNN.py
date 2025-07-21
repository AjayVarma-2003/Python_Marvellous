from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def MarvellousCalculateAccuracyKNN():
    iris = load_iris()
    
    data = iris.data
    target = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size = 0.5, random_state = 42)

    model = KNeighborsClassifier()

    model.fit(X_train, Y_train)
    
    prediction = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, prediction)) * 100

    return accuracy

def main():

    Ret = MarvellousCalculateAccuracyKNN()
    print("Accuracy of KNN classifier is : ", Ret)

if __name__ == "__main__":
    main()