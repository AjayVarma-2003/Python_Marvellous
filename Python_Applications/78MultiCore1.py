import os
import time

def fun(no):
    sum = 0

    for i in range(1, no+1):
        sum = sum + (i*i*i)

    return sum

def main():
    start_time = time.time()

    ret = fun(1000)
    print(ret)

    end_time = time.time()

    print("Time to execute code is : ", end_time - start_time)

if __name__ == "__main__":
    main()