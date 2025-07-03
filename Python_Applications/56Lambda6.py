CalculateCube = lambda A: (A ** 3)

def main():
    print("Enter number : ")
    no = int(input())

    ret = CalculateCube(no)
    print("Cube of number is : ", ret)

    

if __name__ == "__main__":
    main()