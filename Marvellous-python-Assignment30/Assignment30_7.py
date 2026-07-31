import schedule
import time
import shutil
import os
from datetime import datetime

def BackupFile(SourcePath, DestDir):
    try:
        Now = datetime.now()
        Timestamp = Now.strftime("%d_%m_%Y_%H_%M_%S")
        Base = os.path.splitext(os.path.basename(SourcePath))[0]
        Ext = os.path.splitext(SourcePath)[1]
        BackupName = Base + "_" + Timestamp + Ext
        DestPath = os.path.join(DestDir, BackupName)

        shutil.copy(SourcePath, DestPath)

        with open("backup_log.txt", "a") as fobj:
            fobj.write("Backup completed successfully at " + Now.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

        print("Backup completed:", BackupName)
    except Exception as E:
        print("Error during backup:", E)

def Main():
    SourcePath = input("Enter source file path: ")
    DestDir = input("Enter destination directory path: ")

    schedule.every(1).hours.do(BackupFile, SourcePath, DestDir)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()