def CalculateConfusionValues(Actual, Predicted):
    TP = TN = FP = FN = 0

    for i in range(len(Actual)):
        if Actual[i] == 1 and Predicted[i] == 1:
            TP = TP + 1
        elif Actual[i] == 0 and Predicted[i] == 0:
            TN = TN + 1
        elif Actual[i] == 0 and Predicted[i] == 1:
            FP = FP + 1
        elif Actual[i] == 1 and Predicted[i] == 0:
            FN = FN + 1

    return TP, TN, FP, FN

def Main():
    Actual = [1, 1, 1, 1, 0, 0, 0, 0]
    Predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    TP, TN, FP, FN = CalculateConfusionValues(Actual, Predicted)

    print("True Positive (TP) : ", TP)
    print("True Negative (TN) : ", TN)
    print("False Positive (FP) : ", FP)
    print("False Negative (FN) : ", FN)

if __name__ == "__main__":
    Main()
    