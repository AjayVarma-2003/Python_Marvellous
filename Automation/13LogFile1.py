import time

def main():
    timestamp = time.ctime()

    fobj = open("MarvellousLog.log", "w")

    Border = "-" * 54

    fobj.write(Border + "\n")
    fobj.write("This is log file of Marvellous Automation script \n")
    fobj.write(Border + "\n")

    fobj.write("\n\n\n\n\n")
    fobj.write("\n\n\n\n\n")

    fobj.write(Border +"\n")
    fobj.write("This is created at : \n"+timestamp+"\n")
    fobj.write(Border + "\n")

if __name__ == "__main__":
    main()