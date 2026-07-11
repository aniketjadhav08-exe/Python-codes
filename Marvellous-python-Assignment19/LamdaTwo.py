def Main():
    MultiplyFun = lambda a, b: a * b
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    ret = MultiplyFun(no1, no2)
    print("Multiplication is : ", ret)

if __name__ == "__main__":
    Main()