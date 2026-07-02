def CountDigits(n):
    count = 0
    n = abs(n)
    if n == 0:
        return 1
    while n > 0:
        count += 1
        n = n // 10
    return count

n = int(input("Enter a number: "))
print("Count of digits:", CountDigits(n))