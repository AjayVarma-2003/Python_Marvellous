import tensorflow as tf

def main():
    c = tf.constant([1, 2, 3], dtype = tf.float32)
    d = tf.constant(3.0)

    broadcast_add = c + d
    broadcast_mult = c * d

    print("C : ", c.numpy())
    print("C + D : ", broadcast_add.numpy())
    print("C * D : ", broadcast_mult.numpy())

if __name__ == "__main__":
    main()