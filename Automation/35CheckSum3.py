import hashlib

def CalculateCheckSum(File, blocksize = 1024):
    fobj = open(File, "rb")

    hobj = hashlib.md5()
    buffer = fobj.read(blocksize)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(blocksize)

    fobj.close()

    return hobj.hexdigest()

def main():
    print("Enter name of file : ")
    Filename = input()

    ret = CalculateCheckSum(Filename)
    print("CheckSum of file is : ", ret)

if __name__ == "__main__":
    main()