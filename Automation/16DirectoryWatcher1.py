import os

def main():
    print("Enter the name of directory : ")
    DirName = input()

    ret = os.path.isabs(DirName)

    if(ret == True):
        print("It is absolute path.")
    else:
        print("It is relative path.")

if __name__ == "__main__":
    main()

# Abs 
# /Users/marvellous/Desktop/Python_Marvellous/Automations/Marvellous/AI

# Rel
# Python_Marvellous/Automations/Marvellous/AI