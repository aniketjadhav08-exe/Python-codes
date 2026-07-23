import os

def ChkFile(fname):
    return os.path.exists(fname)

def Main():
    fname = input("Enter file name : ")
    if ChkFile(fname):
        print(fname, "exists in current directory")
    else:
        print(fname, "does not exist in current directory")

if __name__ == "__main__":
    Main()
