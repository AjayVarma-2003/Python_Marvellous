import sys

def main():
    print("Number of command line arguments are : ", len(sys.argv))
    print("Data type of argv is : ", type(sys.argv))
    print("First command line argument is : ", sys.argv[0])
    print("Second command line argument is : ", sys.argv[1])
    print("Third command line argument is : ", sys.argv[2])
    print("Fourth command line argument is : ", sys.argv[3])

if __name__ == "__main__":
    main()