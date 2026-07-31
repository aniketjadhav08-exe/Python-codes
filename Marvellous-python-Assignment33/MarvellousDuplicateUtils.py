"""
MarvellousDuplicateUtils.py

User-defined module containing all helper functions used by
DuplicateFileRemoval.py

Marvellous Infosystems : Python - Automation & Machine Learning
"""

import os
import re
import smtplib
import hashlib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


###############################################################################
# Validation Functions
###############################################################################

def ValidateDirectory(DirPath):
    """
    Validates that the supplied directory path is:
        - provided
        - absolute
        - existing
        - actually a directory
        - accessible (readable)
    Returns (True, "") on success, (False, "Reason") on failure.
    """
    if DirPath is None or DirPath.strip() == "":
        return False, "Directory path is not provided."

    if not os.path.isabs(DirPath):
        return False, "Directory path must be absolute. Provided: " + DirPath

    if not os.path.exists(DirPath):
        return False, "Directory does not exist: " + DirPath

    if not os.path.isdir(DirPath):
        return False, "Supplied path is not a directory: " + DirPath

    if not os.access(DirPath, os.R_OK):
        return False, "Application does not have permission to access: " + DirPath

    return True, ""


def ValidateInterval(IntervalStr):
    """
    Validates that the supplied interval is:
        - provided
        - a valid numeric value
        - greater than zero
    Returns (True, IntervalValue) on success, (False, "Reason") on failure.
    """
    if IntervalStr is None or IntervalStr.strip() == "":
        return False, "Time interval is not provided."

    try:
        IntervalValue = int(IntervalStr)
    except ValueError:
        return False, "Time interval must be a valid numeric value: " + IntervalStr

    if IntervalValue <= 0:
        return False, "Time interval must be greater than zero."

    return True, IntervalValue


def ValidateEmail(EmailAddress):
    """
    Validates the basic format of an email address.
    Returns (True, "") on success, (False, "Reason") on failure.
    """
    if EmailAddress is None or EmailAddress.strip() == "":
        return False, "Receiver email address is not provided."

    Pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.match(Pattern, EmailAddress):
        return False, "Invalid email address format: " + EmailAddress

    return True, ""


def ValidateFile(FilePath):
    """
    Validates that a file:
        - exists
        - is a regular file
        - is readable
    Returns (True, "") on success, (False, "Reason") on failure.
    """
    if not os.path.exists(FilePath):
        return False, "File does not exist: " + FilePath

    if not os.path.isfile(FilePath):
        return False, "Path does not represent a regular file: " + FilePath

    if not os.access(FilePath, os.R_OK):
        return False, "File is not readable: " + FilePath

    return True, ""


###############################################################################
# Checksum / Duplicate Detection Functions
###############################################################################

def CalculateChecksum(FilePath, Algorithm="sha256", ChunkSize=65536):
    """
    Calculates the checksum of a file using the specified hashing algorithm.
    Returns the hex digest string, or None if the file could not be read.
    """
    try:
        Hasher = hashlib.new(Algorithm)
        with open(FilePath, "rb") as FileObj:
            while True:
                Chunk = FileObj.read(ChunkSize)
                if not Chunk:
                    break
                Hasher.update(Chunk)
        return Hasher.hexdigest()
    except (PermissionError, OSError, IOError):
        return None


def ScanDirectoryRecursively(DirPath):
    """
    Recursively scans a directory and returns a list of all file paths
    found inside it and its subdirectories.
    """
    AllFiles = []
    for Root, SubDirs, Files in os.walk(DirPath):
        for FileName in Files:
            FullPath = os.path.join(Root, FileName)
            AllFiles.append(FullPath)
    return AllFiles


def GroupFilesByChecksum(FileList, LogFunction):
    """
    Groups files by their checksum value.
    Returns a dictionary: { Checksum : [FilePath1, FilePath2, ...] }
    Files that could not be checksummed are skipped and logged.
    """
    ChecksumMap = {}

    for FilePath in FileList:
        IsValid, Reason = ValidateFile(FilePath)
        if not IsValid:
            LogFunction("Skipped file (validation failed): " + FilePath + " | Reason: " + Reason)
            continue

        Checksum = CalculateChecksum(FilePath)
        if Checksum is None:
            LogFunction("Skipped file (checksum could not be calculated): " + FilePath)
            continue

        if Checksum not in ChecksumMap:
            ChecksumMap[Checksum] = []
        ChecksumMap[Checksum].append(FilePath)

    return ChecksumMap


def DeleteDuplicateFiles(ChecksumMap, LogFunction):
    """
    For every group of files sharing the same checksum:
        - Keeps the first file
        - Deletes all remaining duplicate copies
        - Logs the checksum and the complete path of every deleted file

    Returns a tuple: (TotalDuplicatesFound, TotalDuplicatesDeleted, DeletedPathsList)
    """
    TotalDuplicatesFound = 0
    TotalDuplicatesDeleted = 0
    DeletedPathsList = []

    for Checksum, PathsList in ChecksumMap.items():
        if len(PathsList) <= 1:
            continue

        TotalDuplicatesFound += (len(PathsList) - 1)

        OriginalFile = PathsList[0]
        LogFunction("Checksum: " + Checksum)
        LogFunction("Original file kept: " + OriginalFile)

        for DuplicatePath in PathsList[1:]:
            try:
                os.remove(DuplicatePath)
                TotalDuplicatesDeleted += 1
                DeletedPathsList.append(DuplicatePath)
                LogFunction("Deleted duplicate file: " + DuplicatePath)
            except PermissionError:
                LogFunction("Permission denied while deleting: " + DuplicatePath)
            except OSError as ErrorObj:
                LogFunction("Error deleting file: " + DuplicatePath + " | " + str(ErrorObj))

    return TotalDuplicatesFound, TotalDuplicatesDeleted, DeletedPathsList


###############################################################################
# Directory / Log File Functions
###############################################################################

def CreateLogDirectory(DirName="Marvellous"):
    """
    Creates the log directory if it does not already exist.
    Returns the absolute path of the directory.
    """
    LogDirPath = os.path.join(os.getcwd(), DirName)

    if not os.path.exists(LogDirPath):
        os.makedirs(LogDirPath)

    return LogDirPath


def CreateLogFile(LogDirPath):
    """
    Creates a new timestamped log file inside the log directory.
    Returns the full path of the created log file.
    """
    Now = datetime.now()
    Timestamp = Now.strftime("%d_%m_%Y_%H_%M_%S")
    LogFileName = "DuplicateRemovalLog_" + Timestamp + ".log"
    LogFilePath = os.path.join(LogDirPath, LogFileName)

    # Create an empty log file
    with open(LogFilePath, "w") as FileObj:
        FileObj.write("Duplicate File Removal - Log Started at " +
                       Now.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
        FileObj.write("-" * 60 + "\n")

    return LogFilePath


def WriteLog(LogFilePath, Message):
    """
    Appends a single message line to the log file, prefixed with a timestamp.
    All operational messages must be written here instead of the console.
    """
    Now = datetime.now()
    Timestamp = Now.strftime("%d-%m-%Y %I:%M:%S %p")
    with open(LogFilePath, "a") as FileObj:
        FileObj.write("[" + Timestamp + "] " + Message + "\n")


###############################################################################
# Email Functions
###############################################################################

def SendEmailWithLog(SenderEmail, SenderPassword, ReceiverEmail, Subject, Body, AttachmentPath):
    """
    Sends an email with the log file attached.
    Returns (True, "") on success, (False, "Reason") on failure.

    NOTE: SenderEmail and SenderPassword should be supplied via environment
    variables (MARVELLOUS_SENDER_EMAIL / MARVELLOUS_SENDER_PASSWORD) and
    must never be hard-coded inside the script.
    """
    try:
        Message = MIMEMultipart()
        Message["From"] = SenderEmail
        Message["To"] = ReceiverEmail
        Message["Subject"] = Subject

        Message.attach(MIMEText(Body, "plain"))

        if AttachmentPath is not None and os.path.exists(AttachmentPath):
            with open(AttachmentPath, "rb") as AttachFileObj:
                Part = MIMEBase("application", "octet-stream")
                Part.set_payload(AttachFileObj.read())
            encoders.encode_base64(Part)
            Part.add_header(
                "Content-Disposition",
                "attachment; filename=" + os.path.basename(AttachmentPath),
            )
            Message.attach(Part)

        Server = smtplib.SMTP("smtp.gmail.com", 587)
        Server.starttls()
        Server.login(SenderEmail, SenderPassword)
        Server.sendmail(SenderEmail, ReceiverEmail, Message.as_string())
        Server.quit()

        return True, ""
    except smtplib.SMTPAuthenticationError:
        return False, "Email authentication failed. Check sender credentials."
    except smtplib.SMTPConnectError:
        return False, "Could not connect to the SMTP server."
    except Exception as ErrorObj:
        return False, "Failed to send email: " + str(ErrorObj)


###############################################################################
# Help / Usage Text Functions
###############################################################################

def GetHelpText():
    return """
Duplicate File Removal Automation

This script scans a directory, identifies duplicate files using checksums,
deletes duplicate files, creates a log file, and sends the log file
through email.

Usage:
    python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>

Example:
    python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

Arguments:
    DirectoryPath       Absolute path of the directory to scan for duplicates.
    IntervalInMinutes   Time interval (in minutes) after which the operation repeats.
    ReceiverEmail       Email address that will receive the operation report and log.
"""


def GetUsageText():
    return """
Usage:
    python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>
"""
