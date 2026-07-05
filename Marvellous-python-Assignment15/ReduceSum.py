from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)

def main():
    print("Original list:", numbers)
    print("Sum of all elements:", total)


if __name__ == "__main__":
    main()
    