def SumOfDigits(n):
    total = 0
    while n != 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total

no = int(input("Enter a number: "))
print("Sum of digits:", SumOfDigits(no))