def ToBinary(n):
    if n == 0:
        return "0"
    binary = ""
    n = abs(n)
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

n = int(input("Enter a number: "))
print("Binary equivalent:", ToBinary(n))