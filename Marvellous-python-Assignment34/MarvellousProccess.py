import psutil
import logging
import smtplib
import os
from email.message import EmailMessage

def ConfigureLog(LogFile):
    logging.basicConfig(filename=LogFile, level=logging.INFO,
                         format='%(asctime)s - %(levelname)s - %(message)s')

def GetAllProcessInfo():
    ProcessList = []
    try:
        for Proc in psutil.process_iter(['pid', 'name', 'username']):
            ProcessList.append(Proc.info)
    except Exception as E:
        logging.error("Error while fetching process info: %s", E)
    return ProcessList

def GetProcessInfoByName(Name):
    ProcessList = []
    try:
        for Proc in psutil.process_iter(['pid', 'name', 'username']):
            if Proc.info['name'] and Name.lower() in Proc.info['name'].lower():
                ProcessList.append(Proc.info)
    except Exception as E:
        logging.error("Error while searching process: %s", E)
    return ProcessList

def LogProcessList(ProcessList):
    if not ProcessList:
        logging.info("No matching process found")
        return
    for Info in ProcessList:
        logging.info("Name: %s | PID: %s | Username: %s",
                      Info.get('name'), Info.get('pid'), Info.get('username'))

def ValidateDirectory(Directory):
    if not os.path.exists(Directory):
        os.makedirs(Directory)
    return True

def SendMail(Sender, Password, Receiver, LogFile):
    try:
        Msg = EmailMessage()
        Msg['Subject'] = "Process Info Log File"
        Msg['From'] = Sender
        Msg['To'] = Receiver
        Msg.set_content("Please find attached the process info log file.")

        with open(LogFile, 'rb') as F:
            FileData = F.read()
            FileName = os.path.basename(LogFile)
        Msg.add_attachment(FileData, maintype='application', subtype='octet-stream', filename=FileName)

        with smtplib.SMTP('smtp.gmail.com', 587) as Server:
            Server.starttls()
            Server.login(Sender, Password)
            Server.send_message(Msg)
        logging.info("Mail sent successfully to %s", Receiver)
    except Exception as E:
        logging.error("Error while sending mail: %s", E)
