def SumOfDigits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

n = int(input("Enter a number: "))
print("Sum of digits:", SumOfDigits(n))