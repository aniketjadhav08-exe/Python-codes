def PrintEven(n):
    for i in range(2, n + 1, 2):
        print(i, end=" ")
    print()

n = int(input("Enter a number: "))
PrintEven(n)