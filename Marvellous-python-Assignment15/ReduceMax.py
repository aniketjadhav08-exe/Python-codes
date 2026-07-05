from functools import reduce

numbers = [3, 7, 2, 9, 4]
maximum = reduce(lambda a, b: a if a > b else b, numbers)

def main():
    print("Original list:", numbers)
    print("Maximum element:", maximum)


if __name__ == "__main__":
    main()
    