import os
import sys
import time

def DirectoryWatcher(DirectoryName):
    flag = os.path.isabs(DirectoryName)
    if(flag == True):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("This named file does not exists...")
        exit()

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("There is no such directory.")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            if(fname.endswith(".py")):
                print(fname)

def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory")
            print("Please provide valid absolute path")

        else:
            DirectoryWatcher(sys.argv[1])

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

if __name__ == "__main__":
    main()