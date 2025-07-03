def ChechEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False

def main():
    print("Enter number : ")
    no = int(input())

    ret = ChechEven(no)
    if(ret == True):
        print("Number is even.")
    else:
        print("Number is odd.")

if __name__ == "__main__":
    main()