# Duplicate File Removal Automation

## Project Description

This script periodically scans a specified directory, detects duplicate
files using checksums, deletes duplicate copies (keeping one original file
per group), creates a detailed timestamped log file, and sends that log
file through email along with operation statistics.

## Features

- Recursive directory scanning
- Checksum-based duplicate detection (SHA-256)
- Automatic duplicate-file deletion
- Timestamp-based log generation
- Periodic execution (repeats after a user-specified interval)
- Email notification with log-file attachment
- Command-line input validation
- Exception handling throughout
- Modular programming (logic separated into a user-defined module)

## Requirements

- **Python version:** 3.8 or higher
- **Required libraries:** `schedule` (install via `pip install schedule`).
  All other modules used (`os`, `sys`, `time`, `hashlib`, `re`, `smtplib`,
  `email`, `datetime`) are part of the Python standard library.
- **Internet connection** for sending email.
- **Email application password / SMTP credentials** (see Email
  Configuration below).

## Project Structure

| File                          | Purpose                                                        |
|-------------------------------|-----------------------------------------------------------------|
| `DuplicateFileRemoval.py`      | Main automation script: argument parsing, validation, scheduling|
| `MarvellousDuplicateUtils.py`  | User-defined module containing all reusable helper functions    |
| `Marvellous/`                  | Auto-created directory that stores all generated log files      |
| `README.md`                    | Project documentation                                            |

## Command-Line Options

The script requires three arguments:

```
Directory path        - absolute path of the directory to scan
Time interval          - in minutes, must be numeric and greater than zero
Receiver email address - address that receives the report and log
```

## Execution Command

```
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
```

## Help Command

```
python DuplicateFileRemoval.py --help
python DuplicateFileRemoval.py -h
```

## Usage Command

```
python DuplicateFileRemoval.py --usage
python DuplicateFileRemoval.py -u
```

## Log-File Information

Logs are stored inside the `Marvellous` directory, created in the current
working directory the first time the script runs (an existing directory
is reused rather than recreated). Each run generates a new log file named:

```
DuplicateRemovalLog_DD_MM_YYYY_HH_MM_SS.log
```

Every log file records: scan start/end time, directory scanned, total
files scanned, checksum values and full paths of duplicate files, files
deleted, any errors encountered, and the email delivery status.

## Email Configuration

Sender credentials must **never** be hard-coded in the script. Configure
them as environment variables before running the script:

```
setx MARVELLOUS_SENDER_EMAIL "youraddress@gmail.com"
setx MARVELLOUS_SENDER_PASSWORD "your_app_password"
```

(Use an app-specific password rather than your main account password —
Gmail and most providers require this for SMTP access.)

## Important Notes

- Deleted files may not be recoverable — **test first on a sample
  directory**, not production data.
- Email passwords should never be hard-coded.
- The first file encountered in each duplicate group is preserved; all
  other copies with the same checksum are deleted.
- Files are only considered duplicates when their checksums are
  identical — filenames are never used for duplicate detection.

## Expected Output

After every scheduled execution:

1. Duplicate files are removed from the supplied directory.
2. One original file remains from every duplicate group.
3. A timestamped log file is created inside `Marvellous/`.
4. The log file contains details of all deleted files.
5. Operation statistics are recorded.
6. The log file is emailed to the receiver.
7. The operation repeats after the specified interval.
