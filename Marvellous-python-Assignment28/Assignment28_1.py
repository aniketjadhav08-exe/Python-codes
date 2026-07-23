def CountLines(fname):
    fobj = open(fname, "r")
    count = 0
    for line in fobj:
        count += 1
    fobj.close()
    return count

def Main():
    fname = input("Enter file name : ")
    print("Total number of lines :", CountLines(fname))

if __name__ == "__main__":
    Main()
