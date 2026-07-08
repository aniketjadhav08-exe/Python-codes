def MinOfList(n):
    lst = []
    for i in range(n):
        num = int(input("Enter number: "))
        lst.append(num)
    return min(lst)

n = int(input("Enter number of elements: "))
print("Minimum number is:", MinOfList(n))