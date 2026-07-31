import schedule
import time
from datetime import datetime

def DisplayDateTime():
    Now = datetime.now()
    print("Current Date and Time:", Now.strftime("%d-%m-%Y %I:%M:%S %p"))

def Main():
    schedule.every(1).minutes.do(DisplayDateTime)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()