# basic RNN example with keras

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding

def main():
    # sample : sequence classification
    # suppose we have 10 sequences, each with 5 timesteps, vocabulory, size = 20

    x = np.random.randint(20, size = (10, 5))    # Input sequences (10 samples, 5 timesteps)
    y = np.random.randint(2, size = (10, 1))    # Binary output (labels)

    # Build RNN model
    model = Sequential()
    model.add(Embedding(input_dim = 20, output_dim = 8, input_length = 5))    # Word embedding
    model.add(SimpleRNN(16, activation = "tanh"))    # RNN layer
    model.add(Dense(1, activation = "sigmoid"))    # Output layer

    # Compile model
    model.compile(optimizer = "adam", loss = "binary_crossentropy")
    metrics = ['accuracy']

    # Train
    model.fit(x, y, epochs = 5, verbose = 1)

    # Predictions
    print("Sample predictions : ", model.predict(x[:1]))

if __name__ == "__main__":
    main()