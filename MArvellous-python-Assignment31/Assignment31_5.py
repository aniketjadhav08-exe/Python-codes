import schedule
import time
import os
from datetime import datetime

def CountFiles(DirPath):
    try:
        Entries = os.listdir(DirPath)
        FileCount = sum(1 for E in Entries if os.path.isfile(os.path.join(DirPath, E)))
        Now = datetime.now()

        with open("DirectoryCountLog.txt", "a") as fobj:
            fobj.write("Directory Path: " + DirPath + "\n")
            fobj.write("Number of Files: " + str(FileCount) + "\n")
            fobj.write("Date and Time: " + Now.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
            fobj.write("-" * 40 + "\n")

        print("Logged file count for", DirPath)
    except Exception as E:
        print("Error:", E)

def Main():
    DirPath = input("Enter directory name: ")
    schedule.every(5).minutes.do(CountFiles, DirPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()