def FrequencyInList(n):
    lst = []
    for i in range(n):
        num = int(input("Enter number: "))
        lst.append(num)

    search = int(input("Enter element to search: "))
    count = 0
    for element in lst:
        if element == search:
            count = count + 1
    return count

n = int(input("Enter number of elements: "))
print("Frequency is:", FrequencyInList(n))