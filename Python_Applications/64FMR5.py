def Increase(A):
    return A + 1

def Demo(Task, Value):
    Result = []

    for i in Value:
        ret = Task(i)
        Result.append(ret)

    return Result

def main():
    Data = [13,17,10,14,11]

    Rdata = list(Demo(Increase, Data))
    print(Rdata) 

if __name__ == "__main__":
    main()