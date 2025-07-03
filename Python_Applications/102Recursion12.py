# input = 4
# output = 24 (4 * 3 * 2 * 1)

def Factorial(no):
    fact = 1
    while(no > 0):
        fact = fact * no
        no = no - 1

    return fact

def main():
    ret = Factorial(4)
    print(ret)

if __name__ == "__main__":
    main()