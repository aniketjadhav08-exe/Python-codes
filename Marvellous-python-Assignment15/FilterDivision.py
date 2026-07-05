numbers = [15, 10, 30, 7, 45, 9, 60, 22]
div_3_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))

def main():
    print("Original list:", numbers)
    print("Divisible by both 3 and 5:", div_3_5)


if __name__ == "__main__":
    main()
    