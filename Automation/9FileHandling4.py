import os

def main():
    print("Enter the name of file you want to create : ")
    Filename = input()

    ret = os.path.exists(Filename)

    if(ret == True):
        print("File is present in the current directory.")
    else:
        print("There is no such file.")

if __name__ == "__main__":
    main()