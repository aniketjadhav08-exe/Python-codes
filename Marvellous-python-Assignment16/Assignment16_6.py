def CheckNumber(number):
    if number > 0:
        print("Positive Number")
    elif number < 0:
        print("Negative Number")
    else:
        print("Zero")

no = int(input("Enter a number: "))
CheckNumber(no)