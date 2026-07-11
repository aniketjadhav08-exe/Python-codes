import threading

def MaxElement(List):
    print("Maximum element :", max(List))

def MinElement(List):
    print("Minimum element :", min(List))

def AcceptList():
    List = []
    Size = int(input("Enter number of elements : "))
    for i in range(Size):
        no = int(input("Enter number : "))
        List.append(no)
    return List

def Main():
    List = AcceptList()

    t1 = threading.Thread(target=MaxElement, args=(List,), name="Thread1")
    t2 = threading.Thread(target=MinElement, args=(List,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    Main()