from functools import reduce

CheckEven = lambda A: (A % 2 == 0)

Increase = lambda A: (A + 1)

Sum = lambda A, B: (A + B)

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