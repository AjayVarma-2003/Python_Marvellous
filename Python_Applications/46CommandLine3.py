import sys

def main():
    print("Length of command line arguments is : ", len(sys.argv))

    print("List of command line arguments is : ")
    for i in sys.argv:
        print(i)

if __name__ == "__main__":
    main()