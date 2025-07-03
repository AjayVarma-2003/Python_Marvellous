def CalculatePercentage(Total, Obtained):
    output = ((Obtained/Total) * 100)
    return output

def main():
    print("Enter marks obtained : ")
    obt_marks = int(input())

    print("Enter total marks : ")
    total_marks = int(input())

    result = CalculatePercentage(Obtained = obt_marks, Total = total_marks)    # keyword arguments
    print("Percentage is : ", result)

if __name__ == "__main__":
    main()