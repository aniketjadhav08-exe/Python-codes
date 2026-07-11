import threading

Counter = 0
CounterLock = threading.Lock()

def IncrementCounter(times):
    global Counter
    for i in range(times):
        with CounterLock:
            Counter += 1

def Main():
    Threads = []
    for i in range(5):
        t = threading.Thread(target=IncrementCounter, args=(100,))
        Threads.append(t)
        t.start()

    for t in Threads:
        t.join()

    print("Final value of counter :", Counter)
    print("Exit from main")

if __name__ == "__main__":
    Main()