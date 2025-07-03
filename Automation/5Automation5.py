import schedule
import datetime
import time

def Myschedule():
    print("Inside Myschedule function at : ", datetime.datetime.now())

def main():
    print("Inside automation script ...")
    print("Current time is : ", datetime.datetime.now())

    schedule.every(10).seconds.do(Myschedule)
    # schedule.every(1).minutes.do(Myschedule)
    # schedule.every(1).hours.do(Myschedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()