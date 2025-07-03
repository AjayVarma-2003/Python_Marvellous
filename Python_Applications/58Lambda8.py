def Power(A, B):
    return A ** B

def main():
    print("Enter number : ")
    no = int(input())

    print("Enter power : ")
    pow = int(input())

    ret = Power(no, pow)
    print("Value is : ", ret)

if __name__ == "__main__":
    main()