def CalculatePercentage(Obtained, Total = 500):    # Default argument
    output = ((Obtained/Total) * 100)
    return output

def main():
    print("Enter marks obtained : ")
    obt_marks = int(input())

    result = CalculatePercentage(obt_marks)
    
    print("Percentage is : ", result)

if __name__ == "__main__":
    main()