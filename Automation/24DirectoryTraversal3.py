import os

def DirectoryWatcher(DirectoryName):
    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        print("Name of folder is : ", FolderName)

        for SubF in SubFolderNames:
            print("Sub folders are : ", SubF)

        for files in FileNames:
            print("Files are : ", files)

def main():
    print("Enter the name of directory that you want to travel : ")
    DirName = input()

    DirectoryWatcher(DirName)

if __name__ == "__main__":
    main()