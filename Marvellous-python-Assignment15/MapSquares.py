numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))

def main():
    print("Original list:", numbers)
    print("Squares:", squares)


if __name__ == "__main__":
    main()
