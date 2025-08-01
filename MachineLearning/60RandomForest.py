import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

def main():
    df = pd.read_csv("Telco-Customer-Churn.csv")
    
    df.drop(columns = ['customerID', 'gender'], axis = 1, inplace = True)

    for col in df.select_dtypes(include = 'object'):
        df[col] = LabelEncoder().fit_transform(df[col])

    # print(df.head())

    x = df.drop(columns = 'Churn', axis = 1)
    y = df['Churn']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    model = RandomForestClassifier(n_estimators = 150, max_depth = 7, random_state = 42)

    model.fit(X_train, Y_train)

    Y_prediced = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_prediced)) * 100

    print("Accuracy is : ", accuracy)

if __name__ == "__main__":
    main()