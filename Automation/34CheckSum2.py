import hashlib

def CalculateCheckSum(File):
    fobj = open(File, "rb")

    hobj = hashlib.md5()
    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def main():
    print("Enter name of file : ")
    Filename = input()

    ret = CalculateCheckSum(Filename)
    print("CheckSum of file is : ", ret)

if __name__ == "__main__":
    main()