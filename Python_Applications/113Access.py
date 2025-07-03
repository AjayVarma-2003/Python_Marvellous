class Student:
    def __init__(self, A, B, C):
        self.name = A
        self._age = B
        self.__marks = C

    def Display(self):
        print(self.name)
        print(self._age)
        print(self.__marks)

def main():
    obj = Student('Rahul', 21, 87.80)

if __name__ == "__main__":
    main()