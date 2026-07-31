import schedule
import time

def PrintJayGanesh():
    print("Jay Ganesh...")

def Main():
    schedule.every(2).seconds.do(PrintJayGanesh)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()
