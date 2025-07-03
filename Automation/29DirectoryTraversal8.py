import os

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
                print("Size of file is : ", os.path.getsize(NewPath), "bytes.")
            print()

    print("Total number of files scanned : ", TotalCount)
    print("Total number of empty files found : ", EmptyCount)

def main():
    print("Enter the name of directory that you want to travel : ")
    DirName = input()

    DirectoryWatcher(DirName)

if __name__ == "__main__":
    main()