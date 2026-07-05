numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))


def main():
    print("Original list:", numbers)
    print("Count of even numbers:", even_count)


if __name__ == "__main__":
    main()
    