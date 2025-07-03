import time

def CreateLogFile():
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
    fobj.write("\n\n\n\n\n")

    fobj.write(Border +"\n")
    fobj.write("This is created at : \n"+timestamp+"\n")
    fobj.write(Border + "\n")

def main():
    CreateLogFile()

if __name__ == "__main__":
    main()