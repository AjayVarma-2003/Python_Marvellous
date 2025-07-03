def Increase(A):
    return A + 1

def Demo(Task, Value):
    
    for i in Value:
        print(Task(i))

def main():
    Data = [13, 17, 10, 14, 11]

    Demo(Increase, Data)

if __name__ == "__main__":
    main()