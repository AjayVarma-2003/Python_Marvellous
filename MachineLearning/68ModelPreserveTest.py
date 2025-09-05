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
    Labels = ['Setosa', 'Versicolor', 'Virginica']

    pipe = joblib.load(MODEL_PATH)    # running our saved model of last file.

    sample = np.array([[5.1, 3.5, 1.4, 0.2]])

    Y_predicted = pipe.predict(sample)[0]

    print("Predicted result is : ",Labels[Y_predicted])

if __name__ == "__main__":
    main()


# diabetes predictor using logistic
# Mail sir github link with folder named diabetes predictor with file csv, .py, readme and model file adn if any dependecies then add 
# dependecy.txt .
# readme - descriiption of case study, description of all functions and parameters
# model file - model with max accuracy
# .py - starter, main, imports, artifacts
#       refer sir code as per industry level code, 