def Display1():
    for i in range(1, 100, 2):
        print("Display1 : ", i, end = " ")

def Display2():
    for i in range(1, 200, 3):
        print("Display2 : ", i, end = " ")

def main():
    Display1()
    Display2()

if __name__ == "__main__":
    main()