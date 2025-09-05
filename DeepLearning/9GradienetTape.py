import tensorflow as tf

def main():
    x = tf.Variable(3.0)
    
    with tf.GradientTape() as tape:
        y = x ** 2 + 2 * x + 1    # Function y

    grad = tape.gradient(y, x)

    print("Funtion y : x ^ 2 + 2x + 1 at x = 3")
    print("Gradient dy/dx = ", grad.numpy())     # Expected 8

if __name__ == "__main__":
    main()