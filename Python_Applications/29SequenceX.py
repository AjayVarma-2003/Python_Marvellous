PI = 3.14

def CalculateArea(radius):
    Area = PI * radius * radius
    return Area

def main():
    print("Enter radius of circle : ")
    rad = float(input())

    result = CalculateArea(rad)

    print("Area of circle is : ", result)

if __name__ == "__main__":
    main()