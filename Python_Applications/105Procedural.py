def Addition(A, B):
    ans = A + B
    return ans

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    ret = Addition(no1, no2)
    print("Addition is : ", ret)

if __name__ == "__main__":
    main()