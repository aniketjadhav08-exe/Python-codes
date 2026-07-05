from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)

def main():
    print("Original list:", numbers)
    print("Product of all elements:", product)


if __name__ == "__main__":
    main()
   