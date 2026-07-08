def RepeatedRow(n):
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

RepeatedRow(5)