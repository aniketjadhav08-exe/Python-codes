minimum = lambda a, b: a if a < b else b

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Minimum:", minimum(a, b))


if __name__ == "__main__":
    main()
    