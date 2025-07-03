import sys

def main():
    print("Number of command line arguments are : ", len(sys.argv))

    print("List of command line arguments : ")
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])

if __name__ == "__main__":
    main()