import sys
import os
import logging
import MarvellousProcess as MP

def Main():
    if len(sys.argv) == 2:
        # Usage: ProcInfoLog.py <Directory>
        Directory = sys.argv[1]
        Receiver = None

    elif len(sys.argv) == 3:
        # Usage: ProcInfoLog.py <Directory> <EmailID>
        Directory = sys.argv[1]
        Receiver = sys.argv[2]

    else:
        print("Usage: ProcInfoLog.py <Directory> [EmailID]")
        return

    try:
        MP.ValidateDirectory(Directory)
        LogFile = os.path.join(Directory, "ProcInfoLog.log")
        MP.ConfigureLog(LogFile)
        logging.info("ProcInfoLog.py execution started")

        ProcessList = MP.GetAllProcessInfo()
        MP.LogProcessList(ProcessList)
        logging.info("ProcInfoLog.py execution completed")

        if Receiver:
            Sender = "aniket.jadhav.5120@gmail.com"
            Password = "kufrgculuzcxuuix"   
            MP.SendMail(Sender, Password, Receiver, LogFile)

    except Exception as E:
        print("Error:", E)

if __name__ == "__main__":
    Main()