import os

def main():
    for FolderName, SubFolderNames, FileNames in os.walk("Marvellous"):
        print("Name of folder is : ", FolderName)

        for SubF in SubFolderNames:
            print("Sub folders are : ", SubF)

        for files in FileNames:
            print("Files are : ", files)

if __name__ == "__main__":
    main()