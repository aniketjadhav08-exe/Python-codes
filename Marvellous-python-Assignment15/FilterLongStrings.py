words = ["Python", "Java", "JavaScript", "C", "Programming", "SQL"]
long_words = list(filter(lambda s: len(s) > 5, words))

def main():
    print("Original list:", words)
    print("Strings with length > 5:", long_words)


if __name__ == "__main__":
    main()
    