from functools import reduce

def AcceptList():
    List = []
    Size = int(input("Enter number of elements : "))
    for i in range(Size):
        no = int(input("Enter number : "))
        List.append(no)
    return List

def ProcessList(List):
    FilterList = list(filter(lambda x: (x >= 70 and x <= 90), List))
    MapList = list(map(lambda x: x + 10, FilterList))
    ReduceOutput = reduce(lambda x, y: x * y, MapList)

    print("List after filter = ", FilterList)
    print("List after map = ", MapList)
    print("Output of reduce = ", ReduceOutput)

def Main():
    List = AcceptList()
    ProcessList(List)

if __name__ == "__main__":
    Main()