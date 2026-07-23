def FrequencyOfString(fname, word):
    fobj = open(fname, "r")
    count = 0
    for line in fobj:
        words = line.split()
        count += words.count(word)
    fobj.close()
    return count

def Main():
    fname = input("Enter file name : ")
    word = input("Enter string to search : ")
    print(f'"{word}" appears', FrequencyOfString(fname, word), "times in", fname)

if __name__ == "__main__":
    Main()