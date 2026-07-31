import schedule
import time

def DisplayMessage(Message):
    print(Message)

def Main():
    Message = input("Enter message: ")
    Interval = int(input("Enter interval in seconds: "))

    if Interval <= 0:
        print("Error: Interval must be greater than zero.")
        return

    schedule.every(Interval).seconds.do(DisplayMessage, Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()
