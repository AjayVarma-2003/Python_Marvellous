from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def main():
    # Synthetic 2d classification
    x, y = make_moons(n_samples = 1000, noise = 0.2, random_state = 42)
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)

    # 2 hidden layers 16 and 8 neurons in each of those layers, ReLU + Adam optimizer
    clf = MLPClassifier(hidden_layer_sizes = (16, 8), activation = "relu", solver = "adam", max_iter = 500, random_state = 42)

    clf.fit(x_train, y_train)

    print("Test accuracy : ", (accuracy_score(y_test, clf.predict(x_test))) * 100)

if __name__ == "__main__":
    main()