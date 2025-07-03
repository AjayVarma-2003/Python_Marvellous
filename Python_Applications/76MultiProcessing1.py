import multiprocessing
import multiprocessing.process
import time
import os

def SumEven(no):
    print("PID of SumEven process is : ", os.getpid())
    print("PPID of SumEven process is : ", os.getppid())

    sum = 0

    for i in range(2, no+1, 2):
        sum = sum + i

    print(sum)

def SumOdd(no):
    print("PID of SumOdd process is : ", os.getpid())
    print("PPID of SumOdd process is : ", os.getppid())

    sum = 0

    for i in range(1, no+1, 2):
        sum = sum + i

    print(sum)

def main():
    print("Demonstration of paralled execution (Multi processing) ...")

    print("PID of main process is : ", os.getpid())

    start_time = time.time()

    Process1 = multiprocessing.Process(target = SumEven, args = (900000000,))
    Process2 = multiprocessing.Process(target = SumOdd, args = (900000000,))

    Process1.start()
    Process2.start()

    Process1.join()
    Process2.join()

    end_time = time.time()

    print("Time taked to execute the code : ", end_time - start_time)

    print("End of main...")

if __name__ == "__main__":
    main()