def Table(num):
    for i in range(1, 11):
        print(num * i, end=" ")
    print()

n = int(input("Enter a number: "))
Table(n)
