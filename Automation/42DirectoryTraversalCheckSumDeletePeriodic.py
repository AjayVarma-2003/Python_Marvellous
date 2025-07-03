import os
import sys
import time
import hashlib
import schedule

def CalculateCheckSum(File):
    fobj = open(File, "rb")

    hobj = hashlib.md5()
    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def FindDuplicate(DirectoryName):
    Duplicate = {}
    
    flag = os.path.isabs(DirectoryName)
    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("This named directory does not exists.")
        exit()

    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("This named directory is not available.")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):

        for fname in FileNames:
            fname = os.path.join(FolderName, fname)

            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate


def DeleteDuplicate(path):
    MyDict = FindDuplicate(path)

    Check = lambda X: (len(X) > 1)

    Result = list(filter(Check, MyDict.values()))

    Count = 0
    cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                print("Deleted file is : ", subvalue)
                cnt += 1
                os.remove(subvalue)
        Count = 0     # resetting value.

    print("Total deleted files are : ", cnt)

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
            schedule.every(2).minutes.do(DeleteDuplicate, sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)

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