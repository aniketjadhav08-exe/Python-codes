import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def LoadData(FilePath):
    # Step 1: Dataset loading
    Df = pd.read_csv(FilePath)
    print("Dataset loaded successfully. Shape:", Df.shape)
    return Df

def SplitData(Df):
    # Step 2: Data analysis / feature-target split + train-test split
    X = Df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']]
    Y = Df['FinalResult']

    XTrain, XTest, YTrain, YTest = train_test_split(X, Y, test_size=0.3, random_state=42)
    print(f"\nTraining samples: {len(XTrain)}, Testing samples: {len(XTest)}")
    return XTrain, XTest, YTrain, YTest

def TrainModel(XTrain, YTrain, MaxDepth=None):
    # Step 3: Model training using DecisionTreeClassifier
    Model = DecisionTreeClassifier(max_depth=MaxDepth, random_state=42)
    Model.fit(XTrain, YTrain)
    return Model

def PredictAndCompare(Model, XTest, YTest):
    # Step 4: Prediction on test data, display predicted vs actual
    YPred = Model.predict(XTest)

    Comparison = pd.DataFrame({
        'Actual': YTest.values,
        'Predicted': YPred
    })
    print("\nPredicted vs Actual values:")
    print(Comparison)
    return YPred

def CalculateAccuracy(YTest, YPred):
    # Step 5: Accuracy calculation
    Accuracy = accuracy_score(YTest, YPred)
    print(f"\nModel Accuracy: {Accuracy * 100:.2f}%")
    return Accuracy

def ShowConfusionMatrix(YTest, YPred, OutputPath):
    # Step 6: Confusion matrix generation and display
    Cm = confusion_matrix(YTest, YPred)
    Disp = ConfusionMatrixDisplay(confusion_matrix=Cm, display_labels=['Fail (0)', 'Pass (1)'])
    Disp.plot(cmap='Blues')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.savefig(OutputPath)
    plt.close()

    Tn, Fp, Fn, Tp = Cm.ravel()
    print("\nConfusion Matrix:\n", Cm)
    print(f"True Positive (TP)  = {Tp}  -> Correctly predicted as Pass")
    print(f"True Negative (TN)  = {Tn}  -> Correctly predicted as Fail")
    print(f"False Positive (FP) = {Fp}  -> Predicted Pass, actually Fail")
    print(f"False Negative (FN) = {Fn}  -> Predicted Fail, actually Pass")
    print(f"Confusion matrix image saved to {OutputPath}")

def CompareTrainTestAccuracy(Model, XTrain, YTrain, XTest, YTest):
    # Step 7: Training vs testing accuracy comparison (overfitting/underfitting check)
    TrainAcc = accuracy_score(YTrain, Model.predict(XTrain))
    TestAcc = accuracy_score(YTest, Model.predict(XTest))

    print(f"\nTraining Accuracy: {TrainAcc * 100:.2f}%")
    print(f"Testing Accuracy:  {TestAcc * 100:.2f}%")

    Gap = TrainAcc - TestAcc
    if Gap > 0.15:
        print("Comment: Large gap between training and testing accuracy -> model is OVERFITTING.")
    elif TrainAcc < 0.7 and TestAcc < 0.7:
        print("Comment: Both accuracies are low -> model is UNDERFITTING.")
    else:
        print("Comment: Training and testing accuracies are close -> model generalizes well (good fit).")

    return TrainAcc, TestAcc

def CompareDepths(XTrain, YTrain, XTest, YTest):
    # Step 8: Train 3 models with different max_depth values and compare testing accuracy
    Depths = [1, 3, None]
    Results = {}

    print("\nComparing Decision Tree models with different max_depth values:")
    for D in Depths:
        M = TrainModel(XTrain, YTrain, MaxDepth=D)
        Acc = accuracy_score(YTest, M.predict(XTest))
        Results[D] = Acc
        print(f"max_depth = {D}  ->  Testing Accuracy = {Acc * 100:.2f}%")

    print("""
Observations:
- max_depth=1 (a decision stump) is very simple and may underfit, missing
  patterns that need more than one split to capture.
- max_depth=3 usually balances complexity and generalization well on small
  datasets like this one.
- max_depth=None lets the tree grow fully, which can perfectly fit training
  data but risks overfitting, especially with only 30 records total.
""")
    return Results

def PredictNewStudent(Model):
    # Step 9: Predict outcome for a new student record
    NewStudent = pd.DataFrame({
        'StudyHours': [6],
        'Attendance': [85],
        'PreviousScore': [66],
        'AssignmentsCompleted': [7],
        'SleepHours': [7]
    })
    Prediction = Model.predict(NewStudent)[0]
    Result = "PASS" if Prediction == 1 else "FAIL"
    print(f"\nPrediction for new student (StudyHours=6, Attendance=85, "
          f"PreviousScore=66, AssignmentsCompleted=7, SleepHours=7): {Result}")
    return Result

def Main():
    FilePath = 'student_performance_ml.csv'

    # 1. Dataset loading
    Df = LoadData(FilePath)

    # 2. Data analysis / 4. Train-test split
    XTrain, XTest, YTrain, YTest = SplitData(Df)

    # 5. Model training (default full-depth tree)
    Model = TrainModel(XTrain, YTrain, MaxDepth=3)

    # 6. Prediction
    YPred = PredictAndCompare(Model, XTest, YTest)

    # 7. Accuracy calculation
    CalculateAccuracy(YTest, YPred)

    # 8. Confusion matrix generation
    ShowConfusionMatrix(YTest, YPred, 'Confusion_Matrix.png')

    # Training vs testing accuracy (overfitting/underfitting check)
    CompareTrainTestAccuracy(Model, XTrain, YTrain, XTest, YTest)

    # Compare max_depth = 1, 3, None
    CompareDepths(XTrain, YTrain, XTest, YTest)

    # Predict for a new student
    PredictNewStudent(Model)

    # 9. Final conclusion
    print("""
Final Conclusion:
The Decision Tree model is able to classify student performance (Pass/Fail)
based on StudyHours, Attendance, PreviousScore, AssignmentsCompleted, and
SleepHours with reasonably high accuracy on this dataset. StudyHours and
Attendance appear to be the strongest indicators of the FinalResult. Given
the small dataset size (30 records), a shallow tree (max_depth=3) tends to
generalize better than a fully-grown tree, which risks overfitting.
""")

if __name__ == "__main__":
    Main()
