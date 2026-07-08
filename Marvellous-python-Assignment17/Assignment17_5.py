def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

no = int(input("Enter a number: "))
if IsPrime(no):
    print("It is Prime Number")
else:
    print("It is not Prime Number")