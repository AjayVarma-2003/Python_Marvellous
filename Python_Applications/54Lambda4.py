CheckEven = lambda A: (A % 2 == 0)

def main():
    print("Enter number : ")
    no = int(input())

    ret = CheckEven(no)

    if(ret == True):
        print("Number is even.")
    else:
        print("Number is odd.")

if __name__ == "__main__":
    main()