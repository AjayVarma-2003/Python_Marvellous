import schedule
import datetime
import time

def MySchedule():
    print("Inside MySchedule function at : ", datetime.datetime.now())

def main():
    print("Inside automation script ...")
    print("Current time is : ", datetime.datetime.now())

    schedule.every(10).seconds.do(MySchedule)

    print("Program is in waiting state : ")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()