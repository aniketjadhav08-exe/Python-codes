class BankAccount:
    ROI = 10.5  # class variable

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder : {self.Name}, Balance : {self.Amount}")

    def Deposit(self):
        amt = float(input("Enter amount to deposit : "))
        self.Amount += amt

    def Withdraw(self):
        amt = float(input("Enter amount to withdraw : "))
        if amt <= self.Amount:
            self.Amount -= amt
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

def Main():
    Obj1 = BankAccount("Aniket", 5000)
    Obj1.Display()
    Obj1.Deposit()
    Obj1.Withdraw()
    print("Interest :", Obj1.CalculateInterest())
    Obj1.Display()

if __name__ == "__main__":
    Main()