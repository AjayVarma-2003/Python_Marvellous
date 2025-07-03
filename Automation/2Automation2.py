import schedule
import datetime

def Myschedule():
    print("Inside Myschedule function at : ", datetime.datetime.now())

def main():
    print("Inside automation script...")
    print("Current time is : ", datetime.datetime.now())

    schedule.every(20).seconds.do(Myschedule)

    print("End of automation script...")

if __name__ == "__main__":
    main()