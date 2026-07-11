import threading

Result = {}

def SumOfList(List):
    Result["Sum"] = sum(List)

def ProductOfList(List):
    Product = 1
    for x in List:
        Product *= x
    Result["Product"] = Product

def AcceptList():
    List = []
    Size = int(input("Enter number of elements : "))
    for i in range(Size):
        no = int(input("Enter number : "))
        List.append(no)
    return List

def Main():
    List = AcceptList()

    t1 = threading.Thread(target=SumOfList, args=(List,), name="Thread1")
    t2 = threading.Thread(target=ProductOfList, args=(List,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements :", Result["Sum"])
    print("Product of elements :", Result["Product"])
    print("Exit from main")

if __name__ == "__main__":
    Main()