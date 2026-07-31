import schedule
import time
from datetime import datetime

def CreateTextFile():
    Now = datetime.now()
    Timestamp = Now.strftime("%d_%m_%Y_%H_%M_%S")
    FileName = "File_" + Timestamp + ".txt"

    with open(FileName, "w") as fobj:
        fobj.write("Filename: " + FileName + "\n")
        fobj.write("Creation Date: " + Now.strftime("%d-%m-%Y") + "\n")
        fobj.write("Creation Time: " + Now.strftime("%I:%M:%S %p") + "\n")

    print(FileName, "created.")

def Main():
    schedule.every(1).minutes.do(CreateTextFile)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()
