largest = lambda a, b, c: max(a, b, c)

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print("Largest:", largest(a, b, c))


if __name__ == "__main__":
    main()
    
    