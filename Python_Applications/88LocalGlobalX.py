no = 11

def fun():
    global no
    print("Inside fun")
    x = 21
    print("Value of x is : ", x)
    no = no + 1
    print("Value of no is : ", no)

def main():
    print("Value of no before fun : ", no)
    fun()
    print("Value of no after fun : ", no)

if __name__ == "__main__":
    main()