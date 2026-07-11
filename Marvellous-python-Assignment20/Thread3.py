import threading

def EvenList(List):
    EList = [x for x in List if x % 2 == 0]
    print("Even elements :", EList)
    print("Sum of even elements :", sum(EList))

def OddList(List):
    OList = [x for x in List if x % 2 != 0]
    print("Odd elements :", OList)
    print("Sum of odd elements :", sum(OList))

def AcceptList():
    List = []
    Size = int(input("Enter number of elements : "))
    for i in range(Size):
        no = int(input("Enter number : "))
        List.append(no)
    return List

def Main():
    List = AcceptList()

    t1 = threading.Thread(target=EvenList, args=(List,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(List,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    Main()