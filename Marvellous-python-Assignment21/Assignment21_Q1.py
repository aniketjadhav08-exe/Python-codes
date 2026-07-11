import threading

def ChkPrime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def Prime(List):
    PrimeList = [x for x in List if ChkPrime(x)]
    print("Prime numbers :", PrimeList)

def NonPrime(List):
    NonPrimeList = [x for x in List if not ChkPrime(x)]
    print("Non-prime numbers :", NonPrimeList)

def AcceptList():
    List = []
    Size = int(input("Enter number of elements : "))
    for i in range(Size):
        no = int(input("Enter number : "))
        List.append(no)
    return List

def Main():
    List = AcceptList()

    t1 = threading.Thread(target=Prime, args=(List,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(List,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    Main()
