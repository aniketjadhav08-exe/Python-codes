def DisplayFile(fname):
    fobj = open(fname, "r")
    for line in fobj:
        print(line, end="")
    fobj.close()

def Main():
    fname = input("Enter file name : ")
    DisplayFile(fname)

if __name__ == "__main__":
    Main()