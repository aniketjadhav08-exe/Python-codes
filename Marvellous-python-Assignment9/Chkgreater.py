def ChkGreater(a, b):
    if a > b:
        print(f"{a} is greater")
    elif b > a:
        print(f"{b} is greater")
    else:
        print("Both numbers are equal")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
ChkGreater(num1, num2)