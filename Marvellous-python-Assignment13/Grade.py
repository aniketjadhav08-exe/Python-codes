def CheckGrade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"

marks = float(input("Enter marks: "))
print("Grade:", CheckGrade(marks))