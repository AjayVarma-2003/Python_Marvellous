import os

def ReadFile(Filename):
    fobj = open(Filename, "r")

    data = fobj.read()

    print("Data in file is : ")
    print(data)

    fobj.close()

def WriteFile(Filename):
    fobj = open(Filename, "w")

    print("File created successfully.")

    fobj.close()

def AppendFile(Filename):
    fobj = open(Filename, "a")

    print("Enter the data in file : ")
    data = input()

    fobj.write(data + "\n")

    fobj.close()

def main():
    print("Enter the name of file you want to create : ")
    Filename = input()

    ret = os.path.exists(Filename)

    if(ret == True):
        print("This file already exists in directory.")
        print("Opening file in read mode.")

        ReadFile(Filename)
    
    elif(ret == False):
        WriteFile(Filename)

    print("Do you want to write any data in file (yes/no) : ")
    user = input().lower()
    if(user == "yes"):
        AppendFile(Filename)
        ReadFile(Filename)

    print("Do you want to delete the file (yes/no) : ")
    user = input().lower()
    if(user == "yes"):
        os.remove(Filename)

if __name__ == "__main__":
    main()