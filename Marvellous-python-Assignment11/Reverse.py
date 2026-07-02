def ReverseNumber(n):
    rev = 0
    n = abs(n)
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

n = int(input("Enter a number: "))
print("Reverse:", ReverseNumber(n))