import schedule
import datetime
import time

def MySchedule():
    print("Inside Myschedule function : ", datetime.datetime.now())

def main():
    print("Inside automation script ...")
    print("Current time is : ", datetime.datetime.now())

    schedule.every(20).seconds.do(MySchedule)

    print("Application is in waiting state : ")

    time.sleep(50)

    print("End of automation script ...")

if __name__ == "__main__":
    main()