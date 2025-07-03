from functools import reduce

def CheckEven(no):
    return (no % 2 == 0)

def Increase(no):
    return no + 1

def Sum(A, B):
    return A + B

def main():
    data = [7, 10, 15, 12, 4, 6, 9, 8, 12, 16]
    print("Input data is : ", data)

    Fdata = list(filter(CheckEven, data))
    print("Filter output : ", Fdata)

    Mdata = list(map(Increase, Fdata))
    print("Map output : ", Mdata)

    Rdata = reduce(Sum, Mdata)
    print("Reduce output : ", Rdata)

if __name__ == "__main__":
    main()