def CopyFile(fname1, fname2):
    fobj1 = open(fname1, "r")
    fobj2 = open(fname2, "w")
    for line in fobj1:
        fobj2.write(line)
    fobj1.close()
    fobj2.close()

def Main():
    fname1 = input("Enter existing file name : ")
    fname2 = input("Enter new file name : ")
    CopyFile(fname1, fname2)
    print("Contents copied successfully")

if __name__ == "__main__":
    Main()