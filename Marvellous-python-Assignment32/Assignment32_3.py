import schedule
import time
import os

def DisplayFileContents(FilePath):
    try:
        if not os.path.exists(FilePath):
            print("Error: File does not exist -", FilePath)
            return

        if os.path.getsize(FilePath) == 0:
            print("Error: File is empty -", FilePath)
            return

        with open(FilePath, "r") as fobj:
            Content = fobj.read()
            print("Contents of", FilePath, ":")
            print(Content)

    except PermissionError:
        print("Error: Permission denied for file -", FilePath)
    except IOError:
        print("Error: File cannot be opened -", FilePath)
    except Exception as E:
        print("Unexpected error:", E)

def Main():
    FilePath = input("Enter file path to read: ")
    schedule.every(1).minutes.do(DisplayFileContents, FilePath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()