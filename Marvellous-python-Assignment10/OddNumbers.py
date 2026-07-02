def PrintOdd(n):
    for i in range(1, n + 1, 2):
        print(i, end=" ")
    print()

n = int(input("Enter a number: "))
PrintOdd(n)