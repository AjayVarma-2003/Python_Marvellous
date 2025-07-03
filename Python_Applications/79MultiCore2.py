import os
import time

def fun(no):
    print("PID of fun is : ", os.getpid())

    sum = 0

    for i in range(1, no+1):
        sum = sum + (i ** 3)

    return sum

def main():
    start_time = time.time()

    data = [10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000]

    result = []

    for i in data:
        ret = fun(i)
        result.append(ret)

    print(result)

    end_time = time.time()

    print("Execution time is : ", end_time - start_time)

if __name__ == "__main__":
    main()