from functools import reduce

def main():
    data = [7, 10, 15, 12, 4, 6, 9, 8, 12, 16]
    print("Input data is : ", data)

    Fdata = list(filter((lambda A: (A % 2 == 0)), data))
    print("Filter output : ", Fdata)

    Mdata = list(map((lambda A: (A + 1)), Fdata))
    print("Map output : ", Mdata)

    Rdata = reduce((lambda A, B: (A + B)), Mdata)
    print("Reduce output : ", Rdata)

if __name__ == "__main__":
    main()