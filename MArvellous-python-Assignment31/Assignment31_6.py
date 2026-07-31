import schedule
import time

def StartWeeklyGoals():
    print("Start your weekly goals")

def ReviewWeeklyProgress():
    print("Review your weekly progress")

def WeeklyWorkCompleted():
    print("Weekly work completed")

def Main():
    schedule.every().monday.at("09:00").do(StartWeeklyGoals)
    schedule.every().wednesday.at("17:00").do(ReviewWeeklyProgress)
    schedule.every().friday.at("18:00").do(WeeklyWorkCompleted)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    Main()