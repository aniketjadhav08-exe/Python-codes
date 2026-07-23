def SearchWord(fname, word):
    fobj = open(fname, "r")
    for line in fobj:
        words = line.split()
        if word in words:
            fobj.close()
            return True
    fobj.close()
    return False

def Main():
    fname = input("Enter file name : ")
    word = input("Enter word to search : ")
    if SearchWord(fname, word):
        print(word, "is present in", fname)
    else:
        print(word, "is not present in", fname)

if __name__ == "__main__":
    Main()