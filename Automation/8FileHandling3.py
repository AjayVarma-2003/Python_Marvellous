def main():
    print("Enter the name of file you want to create : ")
    Filename = input()

    fobj = open(Filename,  "w")

    print("Enter the data that you want to write in the file : ")
    data = input()

    fobj.write(data)

    fobj.close()

if __name__ == "__main__":
    main()