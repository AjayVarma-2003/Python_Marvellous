import os
import hashlib

def main():
    print("Enter filename : ")
    filename = input()

    fobj = open(filename, "rb")
    
    hobj = hashlib.md5()
    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    print("Checksum of file is : ", hobj.hexdigest())

if __name__ == "__main__":
    main()