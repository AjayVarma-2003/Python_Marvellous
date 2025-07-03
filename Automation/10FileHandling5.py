import os

def main():
    print("Enter the name of file you want to create : ")
    FileName = input()

    ret = os.path.exists(FileName)

    if(ret == True):
        print("File already exists in current directory.")
        print("Opening file in read mode...")

        fobj = open(FileName, "r")
        data = fobj.read()

        print("Data in file is : ")
        print(data)
    else:
        print("There is no such file.")

if __name__ == "__main__":
    main()