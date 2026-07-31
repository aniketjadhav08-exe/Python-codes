import schedule
import time
import os
from datetime import datetime

def MonitorFileSize(FilePath):
    Now = datetime.now()
    try:
        if not os.path.exists(FilePath):
            print("Error: File does not exist -", FilePath)
            return

        Size = os.path.getsize(FilePath)

        with open("FileSizeLog.txt", "a") as fobj:
            fobj.write("File Path: " + FilePath + "\n")
            fobj.write("File Size (bytes): " + str(Size) + "\n")
            fobj.write("Date and Time: " + Now.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
            fobj.write("-" * 40 + "\n")

        print("Logged size for", FilePath)
    except Exception as E:
        print("Error monitoring file:", E)

def Main():
    FilePath = input("Enter file path to monitor: ")
    schedule.every(30).seconds.do(MonitorFileSize, FilePath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()