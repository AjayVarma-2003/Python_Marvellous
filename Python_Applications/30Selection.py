def main():
    print("Enter your age : ")
    age = int(input())

    if(age < 18):
        print("You can not vote.")
    else:
        print("You can vote.")

if __name__ == "__main__":
    main()