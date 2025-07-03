def main():
    Ans = 0

    try:
        print("Enter first number : ")
        no1 = int(input())

        print("Enter second number : ")
        no2 = int(input())

        Ans = no1 / no2

    except ZeroDivisionError as Zobj:
        print("Exception due to second input.", Zobj)
    except ValueError as Vobj:
        print("Invalid data type of input.", Vobj)
    except Exception as Eobj:
        print("Exception occured.", Eobj)

    finally:
        print("Inside finally block.")

    print("Division of numbers is : ", Ans)

if __name__ == "__main__":
    main()