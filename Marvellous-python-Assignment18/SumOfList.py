def SumOfList(n):
    lst = []
    for i in range(n):
        num = int(input("Enter number: "))
        lst.append(num)
    return sum(lst)

n = int(input("Enter number of elements: "))
print("Sum of list is:", SumOfList(n))
