import sys

def Addition(num1, num2):
    result = 0
    result = num1 + num2
    return result

def main():
    if(len(sys.argv) < 3):
        print("Insuffiecient arguments")
        return
    
    no1 = int((sys.argv[1]))
    no2 = int((sys.argv[2]))

    ans = Addition(no1, no2)
    print("Addition is : ", ans)

if __name__ == "__main__":
    main()