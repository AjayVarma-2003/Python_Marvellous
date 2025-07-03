class Circle:
    PI = 3.14

    def __init__(self, A):
        self.Radius = A

    def CalculateArea(self):
        Ans = 0.0
        Ans = Circle.PI * self.Radius * self.Radius
        return Ans
    
class CircleX(Circle):
    def __init__(self, B):
        print("Inside CircleX constructor.")
        super().__init__(B)

    def CalculateCircumference(self):
        result = 0
        result = Circle.PI * 2 * self.Radius
        return result

def main():
    obj = CircleX(10.5)
    Ret = obj.CalculateArea()
    print("Area of circle is : ",Ret)

    Ret = obj.CalculateCircumference()
    print("Circumference of circle is : ", Ret)

if __name__ == "__main__":
    main()