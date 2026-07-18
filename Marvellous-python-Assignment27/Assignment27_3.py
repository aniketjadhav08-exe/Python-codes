class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
        return sum == self.Value

    def Factors(self):
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i
        return sum

def Main():
    Obj1 = Numbers(28)
    print("Is Prime :", Obj1.ChkPrime())
    print("Is Perfect :", Obj1.ChkPerfect())
    Obj1.Factors()
    print("Sum of Factors :", Obj1.SumFactors())

if __name__ == "__main__":
    Main()