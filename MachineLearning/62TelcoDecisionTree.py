import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("Telco-Customer-Churn.csv")
    
    df.drop(columns = ['customerID', 'gender'], axis = 1, inplace = True)

    for col in df.select_dtypes(include = 'object'):
        df[col] = LabelEncoder().fit_transform(df[col])

    print("Dataset after encoding : ")
    print(df.head())

    # data splitting
    x = df.drop(columns = 'Churn', axis = 1)
    y = df['Churn']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2)

    model = DecisionTreeClassifier(max_depth = 8)

    model.fit(X_train, Y_train)
    Y_predicted = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100
    print("Accuracy of decision tree classifier is : ", accuracy)

if __name__ == "__main__":
    main()