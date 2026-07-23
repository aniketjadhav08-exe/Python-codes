def DisplayContents(fname):
    fobj = open(fname, "r")
    data = fobj.read()
    print(data)
    fobj.close()

def Main():
    fname = input("Enter file name : ")
    DisplayContents(fname)

if __name__ == "__main__":
    Main()