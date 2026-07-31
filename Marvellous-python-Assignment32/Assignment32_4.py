import schedule
import time
import os
import shutil
from datetime import datetime

def CopyTxtFiles(SourceDir, DestDir):
    if not os.path.isdir(SourceDir):
        print("Error: Source directory is invalid -", SourceDir)
        return
    if not os.path.isdir(DestDir):
        print("Error: Destination directory is invalid -", DestDir)
        return

    Now = datetime.now()

    for FileName in os.listdir(SourceDir):
        if FileName.endswith(".txt"):
            SourcePath = os.path.join(SourceDir, FileName)
            DestPath = os.path.join(DestDir, FileName)
            try:
                shutil.copy(SourcePath, DestPath)
                with open("CopyLog.txt", "a") as fobj:
                    fobj.write("Copied: " + FileName + " at " + Now.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
                print("Copied:", FileName)
            except Exception as E:
                print("Error copying", FileName, ":", E)
                continue

def Main():
    SourceDir = input("Enter source directory path: ")
    DestDir = input("Enter destination directory path: ")

    schedule.every(10).minutes.do(CopyTxtFiles, SourceDir, DestDir)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()