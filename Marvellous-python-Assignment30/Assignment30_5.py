import schedule
import time
from datetime import datetime

def WriteToFile():
    Now = datetime.now()
    with open("Marvellous.txt", "a") as fobj:
        fobj.write("Task executed at: " + Now.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

def Main():
    schedule.every(5).minutes.do(WriteToFile)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()