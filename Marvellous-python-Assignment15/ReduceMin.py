from functools import reduce

numbers = [3, 7, 2, 9, 4]
minimum = reduce(lambda a, b: a if a < b else b, numbers)

def main():
    print("Original list:", numbers)
    print("Minimum element:", minimum)


if __name__ == "__main__":
    main()
    