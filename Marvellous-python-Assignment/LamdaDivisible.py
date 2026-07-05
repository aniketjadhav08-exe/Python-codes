div_by_5 = lambda x: True if x % 5 == 0 else False

def main():
    num = int(input("Enter a number: "))
    print("Divisible by 5:", div_by_5(num))


if __name__ == "__main__":
    main()
    