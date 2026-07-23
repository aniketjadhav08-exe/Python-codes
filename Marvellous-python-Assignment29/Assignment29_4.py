import sys

def CompareFiles(fname1, fname2):
    fobj1 = open(fname1, "r")
    fobj2 = open(fname2, "r")
    data1 = fobj1.read()
    data2 = fobj2.read()
    fobj1.close()
    fobj2.close()
    return data1 == data2

def Main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        return
    if CompareFiles(sys.argv[1], sys.argv[2]):
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    Main()