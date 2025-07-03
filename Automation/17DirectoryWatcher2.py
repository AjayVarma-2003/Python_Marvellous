import os

def main():
    print("Enter name of directory : ")
    DirName = input()

    ret = os.path.isabs(DirName)

    if(ret == True):
        print("It is absolute path.")
    else:
        print("It is relative path.")
        NewPath =  os.path.abspath(DirName)
        print("Absolute path is : ", NewPath)

if __name__ == "__main__":
    main()