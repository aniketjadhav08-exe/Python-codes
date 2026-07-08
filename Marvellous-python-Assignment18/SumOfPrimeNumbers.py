import MarvellousNum

def ListPrime(n):
    total = 0
    for i in range(n):
        num = int(input("Enter number: "))
        if MarvellousNum.ChkPrime(num):
            total = total + num
    return total

n = int(input("Enter number of elements: "))
print("Sum of prime numbers is:", ListPrime(n))