class Arithmatic:
    def __init__(self, A, B):
        self.no1 = A
        self.no2 = B

    def __del__(self):
        print("Inside destructor.")

    def Addition(self):
        result = 0
        result = self.no1 + self.no2
        return result

def main():
    print("Enter first number : ")
    num1 = int(input())

    print("Enter second number : ")
    num2 = int(input())

    obj = Arithmatic(num1, num2)

    ret = obj.Addition()
    print("Addition of numbers is : ", ret)

if __name__ == "__main__":
    main()