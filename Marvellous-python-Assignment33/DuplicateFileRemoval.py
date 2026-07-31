"""
DuplicateFileRemoval.py

Marvellous Infosystems : Python - Automation & Machine Learning

Objective:
    Periodically scans a specified directory, identifies duplicate files
    using file checksums, deletes the duplicate files, generates a
    detailed log file, and sends the log file through email.

Execution:
    python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>

Example:
    python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

Help:
    python DuplicateFileRemoval.py --help
    python DuplicateFileRemoval.py -h

Usage:
    python DuplicateFileRemoval.py --usage
    python DuplicateFileRemoval.py -u
"""

import os
import sys
import time
import schedule
from datetime import datetime

import MarvellousDuplicateUtils as MUtils


###############################################################################
# Core Operation Function
###############################################################################

def PerformDuplicateRemoval(DirPath, ReceiverEmail, LogDirPath):
    """
    Performs one complete cycle of the duplicate-file removal operation:
        1. Creates a new log file.
        2. Recursively scans the directory.
        3. Identifies duplicate files using checksums.
        4. Deletes duplicate files (keeping the first copy of each group).
        5. Records operation statistics in the log file.
        6. Sends the log file and statistics through email.
    """
    LogFilePath = MUtils.CreateLogFile(LogDirPath)

    StartTime = datetime.now()
    MUtils.WriteLog(LogFilePath, "Starting time of scanning: " +
                     StartTime.strftime("%d %B %Y, %I:%M:%S %p"))
    MUtils.WriteLog(LogFilePath, "Directory scanned: " + DirPath)

    # Step 1: Recursively scan all files
    AllFiles = MUtils.ScanDirectoryRecursively(DirPath)
    TotalFilesScanned = len(AllFiles)
    MUtils.WriteLog(LogFilePath, "Total number of files scanned: " + str(TotalFilesScanned))

    # Step 2: Group files by checksum to identify duplicates
    ChecksumMap = MUtils.GroupFilesByChecksum(AllFiles, lambda Msg: MUtils.WriteLog(LogFilePath, Msg))

    # Step 3: Delete duplicate files, keeping the first of each group
    TotalDuplicatesFound, TotalDuplicatesDeleted, DeletedPathsList = MUtils.DeleteDuplicateFiles(
        ChecksumMap, lambda Msg: MUtils.WriteLog(LogFilePath, Msg)
    )

    EndTime = datetime.now()
    MUtils.WriteLog(LogFilePath, "Total number of duplicate files found: " + str(TotalDuplicatesFound))
    MUtils.WriteLog(LogFilePath, "Total number of duplicate files deleted: " + str(TotalDuplicatesDeleted))
    MUtils.WriteLog(LogFilePath, "Completion time of scanning: " +
                     EndTime.strftime("%d %B %Y, %I:%M:%S %p"))

    # Step 4: Build and send the email
    SenderEmail = os.environ.get("MARVELLOUS_SENDER_EMAIL")
    SenderPassword = os.environ.get("MARVELLOUS_SENDER_PASSWORD")

    EmailBody = BuildEmailBody(StartTime, EndTime, DirPath, TotalFilesScanned,
                               TotalDuplicatesFound, TotalDuplicatesDeleted)

    if SenderEmail is None or SenderPassword is None:
        MUtils.WriteLog(
            LogFilePath,
            "Email not sent: sender credentials not configured. "
            "Set MARVELLOUS_SENDER_EMAIL and MARVELLOUS_SENDER_PASSWORD environment variables."
        )
        return

    EmailSent, Reason = MUtils.SendEmailWithLog(
        SenderEmail,
        SenderPassword,
        ReceiverEmail,
        "Duplicate File Removal Report",
        EmailBody,
        LogFilePath,
    )

    if EmailSent:
        MUtils.WriteLog(LogFilePath, "Email delivery status: Success. Sent to " + ReceiverEmail)
    else:
        MUtils.WriteLog(LogFilePath, "Email delivery status: Failed. Reason: " + Reason)


def BuildEmailBody(StartTime, EndTime, DirPath, TotalFilesScanned,
                    TotalDuplicatesFound, TotalDuplicatesDeleted):
    """
    Builds the required email body text containing operation statistics.
    """
    Body = "Jay Ganesh,\n\n"
    Body += "The duplicate-file removal operation has been completed successfully.\n\n"
    Body += "Operation Statistics:\n\n"
    Body += "Starting time of scanning: " + StartTime.strftime("%d %B %Y, %I:%M:%S %p") + "\n"
    Body += "Completion time of scanning: " + EndTime.strftime("%d %B %Y, %I:%M:%S %p") + "\n"
    Body += "Directory scanned: " + DirPath + "\n"
    Body += "Total number of files scanned: " + str(TotalFilesScanned) + "\n"
    Body += "Total number of duplicate files found: " + str(TotalDuplicatesFound) + "\n"
    Body += "Total number of duplicate files deleted: " + str(TotalDuplicatesDeleted) + "\n\n"
    Body += "Please find the detailed log file attached to this email.\n\n"
    Body += "Regards,\n"
    Body += "Marvellous Automation System\n"
    return Body


###############################################################################
# Command-Line Handling
###############################################################################

def Main():
    Arguments = sys.argv

    # Handle Help / Usage options first
    if len(Arguments) == 2 and Arguments[1] in ("--help", "-h"):
        print(MUtils.GetHelpText())
        return

    if len(Arguments) == 2 and Arguments[1] in ("--usage", "-u"):
        print(MUtils.GetUsageText())
        return

    # Validate total number of command-line arguments
    # Expected: script name + directory + interval + email = 4
    if len(Arguments) != 4:
        print("Error: Invalid number of command-line arguments.")
        print(MUtils.GetUsageText())
        return

    DirPath = Arguments[1]
    IntervalStr = Arguments[2]
    ReceiverEmail = Arguments[3]

    # Validate directory
    IsDirValid, DirReason = MUtils.ValidateDirectory(DirPath)
    if not IsDirValid:
        print("Error: " + DirReason)
        return

    # Validate time interval
    IsIntervalValid, IntervalOrReason = MUtils.ValidateInterval(IntervalStr)
    if not IsIntervalValid:
        print("Error: " + IntervalOrReason)
        return
    IntervalMinutes = IntervalOrReason

    # Validate receiver email
    IsEmailValid, EmailReason = MUtils.ValidateEmail(ReceiverEmail)
    if not IsEmailValid:
        print("Error: " + EmailReason)
        return

    # Create the Marvellous log directory (reuse if it already exists)
    LogDirPath = MUtils.CreateLogDirectory("Marvellous")

    # Schedule the operation to repeat after the specified interval
    schedule.every(IntervalMinutes).minutes.do(
        PerformDuplicateRemoval, DirPath, ReceiverEmail, LogDirPath
    )

    # Run once immediately, then continue on schedule
    PerformDuplicateRemoval(DirPath, ReceiverEmail, LogDirPath)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    Main()