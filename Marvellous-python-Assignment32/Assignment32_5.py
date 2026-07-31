import schedule
import time
import os
from datetime import datetime

def DeleteEmptyFiles(DirPath):
    Now = datetime.now()

    for Root, Dirs, Files in os.walk(DirPath):
        for FileName in Files:
            FilePath = os.path.join(Root, FileName)
            try:
                if os.path.getsize(FilePath) == 0:
                    os.remove(FilePath)
                    with open("DeletedFilesLog.txt", "a") as fobj:
                        fobj.write("Deleted: " + FilePath + " at " + Now.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
                    print("Deleted empty file:", FilePath)
            except PermissionError:
                print("Permission denied for:", FilePath)
                continue
            except Exception as E:
                print("Error deleting", FilePath, ":", E)
                continue

def Main():
    DirPath = input("Enter directory path (use a sample/test directory): ")
    schedule.every(1).hours.do(DeleteEmptyFiles, DirPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()