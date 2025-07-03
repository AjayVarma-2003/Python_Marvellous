import os

def DirectoryWatcher(DirectoryName):
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
        print("Folder name is : ", FolderName)

        for subf in SubFolderNames:
            print("Sub folder names is : ", subf)

        for files in FileNames:
            print("Files are : ", files)

def main():
    print("Enter the name of directory that you want to travel : ")
    DirName = input()

    DirectoryWatcher(DirName)

if __name__ == "__main__":
    main()