def CheckPerfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

n = int(input("Enter a number: "))
if CheckPerfect(n):
    print("Perfect Number")
else:
    print("Not a Perfect Number")