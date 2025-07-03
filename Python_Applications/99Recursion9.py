# input = 4
# output = 10 (4+3+2+1)

def Add(no):
    sum = 0
    for i in range(no+1):
        sum = sum + i
    return sum

def main():
    ret = Add(4)
    print(ret)

if __name__ == "__main__":
    main()