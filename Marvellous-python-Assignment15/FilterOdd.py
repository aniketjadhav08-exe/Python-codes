numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

def main():
    print("Original list:", numbers)
    print("Odd numbers:", odd_numbers)


if __name__ == "__main__":
    main()
    