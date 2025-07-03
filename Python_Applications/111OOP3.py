class Employees:
    CompanyName = "Marvellous"

    def __init__(self, A, B, C):
        self.name = A
        self.Salary = B
        self.City = C

    def __del__(self):
        print("Inside destructor")

def main():
    print("Class variable is : ", Employees.CompanyName)

    emp1 = Employees('Rahul', 15000, 'Pune')
    emp2 = Employees('Pooja', 25000, 'Mumbai')

    print("Employee name is : ", emp1.name)
    print("Employee salary is : ", emp1.Salary)
    print("Employee city is : ", emp1.City)

if __name__ == "__main__":
    main()