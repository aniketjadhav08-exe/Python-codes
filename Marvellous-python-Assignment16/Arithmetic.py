def Arithmetic(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Not defined (division by zero)")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
Arithmetic(num1, num2)