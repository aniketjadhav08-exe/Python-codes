def SumOfFactors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    return total

no = int(input("Enter a number: "))
print("Sum of factors is:", SumOfFactors(no))