def CalculatePercentage(Total, Obtained):
    output = ((Obtained/Total) * 100)
    return output

def main():
    print("Enter marks obtained : ")
    obt_marks = int(input())

    print("Enter total marks : ")
    total_marks = int(input())

    result = CalculatePercentage(total_marks, obt_marks)    # Positional arguments
    print("Percentage is : ", result)

if __name__ == "__main__":
    main()