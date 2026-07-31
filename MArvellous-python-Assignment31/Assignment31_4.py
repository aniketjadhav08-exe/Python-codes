import schedule
import time
from datetime import datetime

def CreateLogFile():
    Now = datetime.now()
    Timestamp = Now.strftime("%d_%m_%Y_%H_%M_%S")
    FileName = "MarvellousLog_" + Timestamp + ".txt"

    with open(FileName, "w") as fobj:
        fobj.write("Log file created successfully.\n")
        fobj.write("Creation Time: " + Now.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    print(FileName, "created.")

def Main():
    schedule.every(10).minutes.do(CreateLogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()