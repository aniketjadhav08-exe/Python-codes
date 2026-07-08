def DivBy5(number):
    if number % 5 == 0:
        return True
    else:
        return False

no = int(input("Enter a number: "))
print(DivBy5(no))