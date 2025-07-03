import sys

def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This application is used to perform ---------")
            print("This is automation script ")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py Argument1 Argument2")

        else:
            print("--h : used to display help section.")
            print("--u : used to display use section.")

    else:
        print("Invalid number of arguments.")
        print("Type following to get the help about usage")
        print("--h : used to display help section.")
        print("--u : used to display use section.")

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

if __name__ == "__main__":
    main()