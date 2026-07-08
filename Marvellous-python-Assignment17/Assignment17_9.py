def CountDigits(n):
    count = 0
    while n != 0:
        n = n // 10
        count = count + 1
    return count

no = int(input("Enter a number: "))
print("Number of digits:", CountDigits(no))