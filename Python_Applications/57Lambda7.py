def Power(A, B):
    result = 1

    for i in range(B):
        result = result * A

    return result

def main():
    print("Enter number : ")
    no = int(input())

    print("Enter power of number : ")
    pow = int(input())

    ret = Power(no, pow)
    print("Value is : ", ret)

if __name__ == "__main__":
    main()