def main():
    print("Enter the name of file that you want to create : ")
    Filename = input()

    fobj = open(Filename, "x")

if __name__ == "__main__":
    main()