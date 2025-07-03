no = 11

def fun(no):
    # global no    # this will generate erro
    print("fun no : ", no)

def main():
    print("main no : ", no)
    fun(21)

if __name__ == "__main__":
    main()