import os
import sys
import time

def CreateLogFile(TotalCount, EmptyCount):
    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    fobj = open(filename,"w")

    Border = "-" * 54

    fobj.write(Border + "\n")
    fobj.write("This is log file of Marvellous Automation script \n")
    fobj.write(Border + "\n")

    fobj.write("\n\n\n\n\n")
    fobj.write("Total number of files scanned : " + str(TotalCount) + "\n")
    fobj.write("Total number of empty files found : " + str(EmptyCount) + "\n")
    fobj.write("Total number of empty files removed are : " + str(EmptyCount) + "\n")
    fobj.write("\n\n\n\n\n")

    fobj.write(Border +"\n")
    fobj.write("This is created at : \n"+timestamp+"\n")
    fobj.write(Border + "\n")


def DirectoryWatcher(DirectoryName):
    TotalCount = 0
    EmptyCount = 0

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

    print("Absolute path of directory is : ", DirectoryName)

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for subf in SubFolderNames:
            print("Sub folder names is : ", subf)

        for files in FileNames:
            TotalCount += 1
            NewPath = os.path.join(FolderName, files)

            if(os.path.getsize(NewPath) == 0):
                EmptyCount += 1
                print("Name of file is : ", files)
                os.remove(NewPath)
            print()

    CreateLogFile(TotalCount, EmptyCount)

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