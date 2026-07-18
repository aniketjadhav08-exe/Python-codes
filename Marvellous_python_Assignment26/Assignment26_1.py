class Demo:
    Value = 100  # class variable

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("no1 :", self.no1, "no2 :", self.no2)

    def Gun(self):
        print("no1 :", self.no1, "no2 :", self.no2)

def Main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    Main()
