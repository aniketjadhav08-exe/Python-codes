import sys

def CopyFile(fname):
    fobj1 = open(fname, "r")
    fobj2 = open("Demo.txt", "w")
    data = fobj1.read()
    fobj2.write(data)
    fobj1.close()
    fobj2.close()

def Main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return
    CopyFile(sys.argv[1])
    print("Contents copied into Demo.txt")

if __name__ == "__main__":
    Main()