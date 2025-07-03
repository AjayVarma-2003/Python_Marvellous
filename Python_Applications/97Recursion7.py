# input = 4
# output = * * * *

def Display(no):
    while(no >= 0):
        print("*", end = " ")
        no = no - 1

    print()

def main():
    Display(4)
    

if __name__ == "__main__":
    main()