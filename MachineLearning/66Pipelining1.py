from pathlib import Path
import joblib                                           # used to preserve the model on harddisk i.e freeze model
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Configuration details
ARTIFACTS = Path("artifacts_sample")
ARTIFACTS.mkdir(exist_ok = True)
MODEL_PATH = ARTIFACTS / "iris_pipeline.joblib"
RANDOM_STATE = 42
TEST_SIZE = 0.2

def main():
    iris = load_iris()
    
    x = iris.data
    y = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = TEST_SIZE, random_state = RANDOM_STATE)

    pipe = Pipeline([
        ("scaler", StandardScaler()),    # convert data to standard scaler
        ("model", LogisticRegression(max_iter = 1000)),    # build model
    ])

    pipe.fit(X_train, Y_train)

    Y_predicted = pipe.predict(X_test)

    accuracy = (accuracy_score(Y_test, Y_predicted)) * 100
    print("Accuracy is : ", accuracy)

if __name__ == "__main__":
    main()