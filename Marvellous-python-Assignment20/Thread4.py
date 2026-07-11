import threading

def Small(Str):
    Count = sum(1 for ch in Str if ch.islower())
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Number of lowercase characters :", Count)

def Capital(Str):
    Count = sum(1 for ch in Str if ch.isupper())
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Number of uppercase characters :", Count)

def Digits(Str):
    Count = sum(1 for ch in Str if ch.isdigit())
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Number of numeric digits :", Count)

def Main():
    Str = input("Enter string : ")

    t1 = threading.Thread(target=Small, args=(Str,), name="Small")
    t2 = threading.Thread(target=Capital, args=(Str,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(Str,), name="Digits")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    Main()