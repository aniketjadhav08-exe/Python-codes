import threading

def EvenFactor(no):
    Sum = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            Sum += i
    print("Sum of even factors :", Sum)

def OddFactor(no):
    Sum = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            Sum += i
    print("Sum of odd factors :", Sum)

def Main():
    no = int(input("Enter number : "))

    t1 = threading.Thread(target=EvenFactor, args=(no,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(no,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    Main()