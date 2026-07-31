import schedule
import time

def PrintNamskar():
    print("Namskar...")

def Main():
    schedule.every().day.at("09:00").do(PrintNamskar)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()