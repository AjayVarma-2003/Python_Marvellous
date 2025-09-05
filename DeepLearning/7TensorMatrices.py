import tensorflow as tf

def main():
    a = tf.constant([1, 2], [3, 4], dtype = tf.float32)
    b = tf.constant([5, 6], [7, 8], dtype = tf.float32)

    matmul = tf.multiply(a, b)    # matrix multiplication
    transpose = tf.transpose(a)    # matrix transpose

    print("Matrix A : \n", a.numpy())
    print("Matrix B : \n", b.numpy())
    print("A * B : \n", matmul.numpy())
    print("Transpose of A : \n", transpose.numpy())

if __name__ == "__main__":
    main()