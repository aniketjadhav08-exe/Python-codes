class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Value1 : "))
        self.Value2 = int(input("Enter Value2 : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not possible"
        return self.Value1 / self.Value2

def Main():
    Obj1 = Arithmetic()
    Obj1.Accept()
    print("Addition :", Obj1.Addition())
    print("Subtraction :", Obj1.Subtraction())
    print("Multiplication :", Obj1.Multiplication())
    print("Division :", Obj1.Division())

    Obj2 = Arithmetic()
    Obj2.Accept()
    print("Addition :", Obj2.Addition())
    print("Subtraction :", Obj2.Subtraction())
    print("Multiplication :", Obj2.Multiplication())
    print("Division :", Obj2.Division())

if __name__ == "__main__":
    Main()