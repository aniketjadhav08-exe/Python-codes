import threading

def EvenThread():
    for i in range(2, 21, 2):
        print("Even :", i)

def OddThread():
    for i in range(1, 20, 2):
        print("Odd :", i)

def Main():
    t1 = threading.Thread(target=EvenThread, name="Even")
    t2 = threading.Thread(target=OddThread, name="Odd")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    Main()
