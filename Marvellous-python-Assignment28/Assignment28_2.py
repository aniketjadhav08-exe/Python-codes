def CountWords(fname):
    fobj = open(fname, "r")
    count = 0
    for line in fobj:
        words = line.split()
        count += len(words)
    fobj.close()
    return count

def Main():
    fname = input("Enter file name : ")
    print("Total number of words :", CountWords(fname))

if __name__ == "__main__":
    Main()