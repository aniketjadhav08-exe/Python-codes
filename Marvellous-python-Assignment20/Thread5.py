import threading

def Thread1Fun():
    for i in range(1, 51):
        print("Thread1 :", i)

def Thread2Fun():
    for i in range(50, 0, -1):
        print("Thread2 :", i)

def Main():
    t1 = threading.Thread(target=Thread1Fun, name="Thread1")
    t2 = threading.Thread(target=Thread2Fun, name="Thread2")

    t1.start()
    t1.join()   # Thread2 waits until Thread1 completes

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    Main()