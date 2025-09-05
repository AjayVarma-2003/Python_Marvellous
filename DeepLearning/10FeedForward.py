import math

relu = lambda x: max(0, x)
sigmoid = lambda z: (1 / (1 + math.exp(-z)))

def main():
    x = [2.0, 3.0]
    w1 = [[0.5, -0.2],
          [0.8, 0.4]]
    b1 = [0.1, -0.1]

    # Hidden neuron 1
    z1 = ((w1[0][0] * x[0]) + (w1[0][1] * x[1]) + (b1[0]))
    a1 = relu(z1)
    print(f"Neuron1 : z = {z1:.3f}, a = {a1:.3f}")

    # Hidden neuron 2
    z2 = ((w1[1][0] * x[0]) + (w1[1][1] * x[1]) + (b1[1]))
    a2 = relu(z2)
    print(f"Neuron2 : z = {z2:.3f}, a = {a2:.3f}")

    # Output layer
    w2 = [1.2, -0.7]
    b = 0.05
    z_out = w2[0] * a1 + w2[1] * a2 + b
    yhat = sigmoid(z_out)
    print(f"Output : z = {z_out:.3f}, sigmoid(y) = {yhat:.3f}")

if __name__ == "__main__":
    main()