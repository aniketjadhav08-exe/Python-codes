from sklearn.metrics import classification_report

def GenerateReport(Actual, Predicted):
    Report = classification_report(Actual, Predicted)
    return Report

def Main():
    Actual = [1, 1, 1, 1, 0, 0, 0, 0]
    Predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    Report = GenerateReport(Actual, Predicted)
    print("Classification Report :\n")
    print(Report)

if __name__ == "__main__":
    Main()