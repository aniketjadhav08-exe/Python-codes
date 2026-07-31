import schedule
import time
import os
from datetime import datetime

def ScanDirectory(DirPath):
    try:
        Entries = os.listdir(DirPath)
        FileCount = sum(1 for E in Entries if os.path.isfile(os.path.join(DirPath, E)))
        DirCount = sum(1 for E in Entries if os.path.isdir(os.path.join(DirPath, E)))
        Now = datetime.now()

        print("Directory Scanned:", DirPath)
        print("Total Files:", FileCount)
        print("Total Subdirectories:", DirCount)
        print("Scan Time:", Now.strftime("%d-%m-%Y %I:%M:%S %p"))
    except Exception as E:
        print("Error scanning directory:", E)

def Main():
    DirPath = input("Enter directory path to scan: ")
    schedule.every(1).minutes.do(ScanDirectory, DirPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()