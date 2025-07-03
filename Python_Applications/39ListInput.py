def main():
    print("Enter number of elements : ")
    size = int(input())

    Data = []

    print("Enter elements :")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Entered values are : ")
    for i in Data:
        print(i, end = " ")

if __name__ == "__main__": 
    main()