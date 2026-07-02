def CheckDivisible(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

n = int(input("Enter a number: "))
CheckDivisible(n)