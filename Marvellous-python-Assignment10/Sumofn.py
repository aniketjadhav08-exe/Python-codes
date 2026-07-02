def SumOfN(n):
    return n * (n + 1) // 2

n = int(input("Enter a number: "))
print("Sum of first", n, "natural numbers:", SumOfN(n))