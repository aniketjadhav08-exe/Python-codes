def MaxOfList(n):
    lst = []
    for i in range(n):
        num = int(input("Enter number: "))
        lst.append(num)
    return max(lst)

n = int(input("Enter number of elements: "))
print("Maximum number is:", MaxOfList(n))