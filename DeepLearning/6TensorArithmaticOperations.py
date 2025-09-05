import tensorflow as tf

def main():
    a = tf.constant(5)
    b = tf.constant(3)

    add = tf.add(a, b)
    sub = tf.subtract(a, b)
    mul = tf.multiply(a, b)
    div = tf.division(a, b)

    print("a + b : ", add.numpy())
    print("a - b : ", sub.numpy())
    print("a * b : ", mul.numpy())
    print("a / b : ", div.numpy())

if __name__ == "__main__":
    main()