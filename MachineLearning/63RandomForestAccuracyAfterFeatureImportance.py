import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("Telco-Customer-Churn.csv")
    
    df.drop(columns = ['customerID', 'gender'], axis = 1, inplace = True)
    print(df.head())

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

    print("Accuracy before handling feature importance : ", accuracy)    # 81.12136266855926

    importance = pd.Series(model.feature_importances_, index = x.columns)
    importance = importance.sort_values(ascending = False)

    importance.plot(kind = 'bar', figsize = (10, 8), title = 'Feature Importance')
    plt.show()

    df_new = df.drop(columns = ['MultipleLines', 'StreamingTV', 'StreamingMovies', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService'], axis = 1)
    print(df_new.head())

    # building model trainind testing and calculating model again.
    x = df_new.drop(columns = 'Churn', axis = 1)
    y = df_new['Churn']

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    model = RandomForestClassifier(n_estimators = 150, max_depth = 7, random_state = 42)

    model.fit(X_train, Y_train)

    Y_prediced = model.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_prediced)) * 100

    print("Accuracy after handling feature importance : ", accuracy)    # 81.33427963094393

if __name__ == "__main__":
    main()