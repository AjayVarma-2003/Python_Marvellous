def CalculatePercentage(Obtained = 400, Total = 500):
    output = ((Obtained / Total) * 100)
    return output

def main():
    result = CalculatePercentage(250, 450)
    print("Result is : ", result)

    result = CalculatePercentage(350)
    print("Result is : ", result)

    result = CalculatePercentage()
    print("Result is : ", result)

if __name__ == "__main__":
    main()