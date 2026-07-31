import schedule
import time

def PrintCodingKar():
    print("Coding Kar..!")

def Main():
    schedule.every(30).minutes.do(PrintCodingKar)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()