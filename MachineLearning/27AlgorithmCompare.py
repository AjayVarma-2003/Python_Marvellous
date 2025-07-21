from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()
    
    data = iris.data
    target = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size = 0.5)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)
    
    prediction = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, prediction)) * 100

    return accuracy

def main():
    Ret = MarvellousCalculateAccuracyDecisionTree()
    print("Accuracy of decision tree classifier is : ", Ret)

if __name__ == "__main__":
    main()