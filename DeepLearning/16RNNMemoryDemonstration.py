# toy RNN implementation to show how it processed a sequence

import numpy as np

def main():
    # Example :- "I Love AI" (encoded  as numbers)
    sequence = [1, 2, 3]    # Lets say 1 = I, 2 = Love, 3 = AI

    # Initialize weights and hidden state
    Wx, Wh, b = 0.5, 0.8, 0.1    # random chosen values
    h = 0    # initial hidden state

    print("Processing sequence step by step : ")

    for t, x in enumerate(sequence):
        h = np.tanh(Wx * x + Wh * h + b)    # memory update
        print(f"Timestep {t + 1} | Input = {x} | Hidden state = {h:.4f}")

if __name__ == "__main__":
    main()