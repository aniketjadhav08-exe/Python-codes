import sys
import logging
import MarvellousProcess as MP

def Main():
    MP.ConfigureLog("ProcInfo.log")
    logging.info("ProcInfo.py execution started")

    if len(sys.argv) == 1:
        # Usage: ProcInfo.py
        ProcessList = MP.GetAllProcessInfo()
        MP.LogProcessList(ProcessList)

    elif len(sys.argv) == 2:
        # Usage: ProcInfo.py <ProcessName>
        Name = sys.argv[1]
        ProcessList = MP.GetProcessInfoByName(Name)
        MP.LogProcessList(ProcessList)

    else:
        logging.error("Invalid arguments. Usage: ProcInfo.py OR ProcInfo.py <ProcessName>")
        return

    logging.info("ProcInfo.py execution completed")

if __name__ == "__main__":
    Main()