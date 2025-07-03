def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    Ans = 0
    
    try:
        Ans = no1 / no2
    
    except ZeroDivisionError:
        print("Exception occured due to second input.")

    print("Divison of numbers is : ", Ans)

if __name__ == "__main__":
    main()