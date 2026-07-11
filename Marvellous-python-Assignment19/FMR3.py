from functools import reduce

def ChkPrime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def AcceptList():
    List = []
    Size = int(input("Enter number of elements : "))
    for i in range(Size):
        no = int(input("Enter number : "))
        List.append(no)
    return List

def ProcessList(List):
    FilterList = list(filter(ChkPrime, List))
    MapList = list(map(lambda x: x * 2, FilterList))
    ReduceOutput = reduce(lambda x, y: x if x > y else y, MapList)

    print("List after filter = ", FilterList)
    print("List after map = ", MapList)
    print("Output of reduce = ", ReduceOutput)

def Main():
    List = AcceptList()
    ProcessList(List)

if __name__ == "__main__":
    Main()