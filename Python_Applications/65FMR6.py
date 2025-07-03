CheckEven = lambda A: (A % 2 == 0)
Increase = lambda A: (A + 1)
Sum = lambda A, B: (A + B)

def FilterX(Task, Values):
    Result = []

    for i in Values:
        ret = Task(i)
        if(ret == True):
            Result.append(i)

    return Result

def MapX(Task, Values):
    Result = []

    for i in Values:
        ret = Task(i)
        Result.append(ret)

    return Result

def ReduceX(Task, Values):
    Result = 0

    for i in Values:
        Result = Task(Result, i)

    return Result

def main():
    print("Enter number of elements : ")
    size = int(input())

    Data = []

    print("Enter numbers : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input data is : ", Data)

    Fdata = list(FilterX(CheckEven, Data))
    print("Filter output : ", Fdata)

    Mdata = list(MapX(Increase, Fdata))
    print("Map output : ", Mdata)

    Rdata = ReduceX(Sum, Mdata)
    print("Reduce output : ", Rdata)

if __name__ == "__main__":
    main()