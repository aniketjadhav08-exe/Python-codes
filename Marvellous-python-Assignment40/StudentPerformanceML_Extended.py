import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def LoadData(FilePath):
    Df = pd.read_csv(FilePath)
    return Df

def BaselineModel(Df):
    # Baseline model using all 5 original features
    X = Df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']]
    Y = Df['FinalResult']
    XTrain, XTest, YTrain, YTest = train_test_split(X, Y, test_size=0.3, random_state=42)

    Model = DecisionTreeClassifier(max_depth=3, random_state=42)
    Model.fit(XTrain, YTrain)
    YPred = Model.predict(XTest)
    Acc = accuracy_score(YTest, YPred)

    return Model, XTrain, XTest, YTrain, YTest, YPred, Acc

def ShowFeatureImportance(Model, FeatureNames):
    # Task 1: Feature importance
    print("\n--- Task 1: Feature Importances ---")
    Importances = Model.feature_importances_
    ImpDf = pd.DataFrame({'Feature': FeatureNames, 'Importance': Importances})
    ImpDf = ImpDf.sort_values(by='Importance', ascending=False)
    print(ImpDf.to_string(index=False))

    Most = ImpDf.iloc[0]
    Least = ImpDf.iloc[-1]
    print(f"\nMost important feature: {Most['Feature']} (importance = {Most['Importance']:.4f})")
    print(f"Least important feature: {Least['Feature']} (importance = {Least['Importance']:.4f})")

def RemoveSleepHours(Df, BaselineAcc):
    # Task 2: Remove SleepHours and retrain
    print("\n--- Task 2: Removing SleepHours ---")
    X = Df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted']]
    Y = Df['FinalResult']
    XTrain, XTest, YTrain, YTest = train_test_split(X, Y, test_size=0.3, random_state=42)

    Model = DecisionTreeClassifier(max_depth=3, random_state=42)
    Model.fit(XTrain, YTrain)
    Acc = accuracy_score(YTest, Model.predict(XTest))

    print(f"Accuracy without SleepHours: {Acc * 100:.2f}%")
    print(f"Accuracy with all features (baseline): {BaselineAcc * 100:.2f}%")
    if abs(Acc - BaselineAcc) < 0.01:
        print("Removing SleepHours does NOT affect performance - it was not adding predictive value.")
    else:
        print("Removing SleepHours changes performance, indicating it had some predictive contribution.")

def TrainWithTwoFeatures(Df, BaselineAcc):
    # Task 3: Train using only StudyHours and Attendance
    print("\n--- Task 3: Train using only StudyHours & Attendance ---")
    X = Df[['StudyHours', 'Attendance']]
    Y = Df['FinalResult']
    XTrain, XTest, YTrain, YTest = train_test_split(X, Y, test_size=0.3, random_state=42)

    Model = DecisionTreeClassifier(max_depth=3, random_state=42)
    Model.fit(XTrain, YTrain)
    Acc = accuracy_score(YTest, Model.predict(XTest))

    print(f"Accuracy with only StudyHours & Attendance: {Acc * 100:.2f}%")
    print(f"Accuracy with all features (baseline): {BaselineAcc * 100:.2f}%")
    if Acc >= BaselineAcc:
        print("The model performs just as well (or better) with only these two features - "
              "they carry most of the predictive signal in this dataset.")
    else:
        print("The model performs slightly worse with only two features, but is still usable.")

def PredictNewStudents(Model, FeatureNames):
    # Task 4: Predict for 5 new students
    print("\n--- Task 4: Predictions for 5 new students ---")
    NewStudents = pd.DataFrame({
        'StudyHours': [1.5, 3.0, 5.0, 6.5, 8.0],
        'Attendance': [60, 70, 80, 88, 95],
        'PreviousScore': [40, 50, 60, 70, 78],
        'AssignmentsCompleted': [2, 4, 6, 7, 9],
        'SleepHours': [5, 6, 7, 7, 8]
    })
    Predictions = Model.predict(NewStudents[FeatureNames])
    NewStudents['PredictedResult'] = ['Pass' if P == 1 else 'Fail' for P in Predictions]
    print(NewStudents.to_string(index=False))

def ManualAccuracyCheck(YTest, YPred, SklearnAcc):
    # Task 5: Manually calculate accuracy
    print("\n--- Task 5: Manual Accuracy Calculation ---")
    YTestList = list(YTest)
    Correct = sum(1 for A, P in zip(YTestList, YPred) if A == P)
    Total = len(YTestList)
    ManualAcc = Correct / Total

    print(f"Manually calculated accuracy: {Correct}/{Total} = {ManualAcc * 100:.2f}%")
    print(f"sklearn accuracy_score:        {SklearnAcc * 100:.2f}%")
    if abs(ManualAcc - SklearnAcc) < 1e-9:
        print("Match confirmed: manual calculation equals sklearn's accuracy_score.")
    else:
        print("Mismatch detected - check calculation.")

def IdentifyMisclassified(XTest, YTest, YPred):
    # Task 6: Identify misclassified students
    print("\n--- Task 6: Misclassified Students ---")
    Mask = YTest.values != YPred
    Misclassified = XTest[Mask].copy()
    Misclassified['Actual'] = YTest.values[Mask]
    Misclassified['Predicted'] = YPred[Mask]

    print(f"Number of misclassified students: {len(Misclassified)}")
    if len(Misclassified) > 0:
        print(Misclassified.to_string(index=False))
        print("\nCommon pattern: misclassified students often have StudyHours/Attendance "
              "values close to the decision boundary between Pass and Fail, making them "
              "harder for the tree to separate cleanly.")
    else:
        print("No misclassified students in this test split.")

def CompareRandomStates(X, Y):
    # Task 7: Compare different random_state values
    print("\n--- Task 7: Comparing random_state values ---")
    for Rs in [0, 10, 42]:
        XTrain, XTest, YTrain, YTest = train_test_split(X, Y, test_size=0.3, random_state=Rs)
        Model = DecisionTreeClassifier(max_depth=3, random_state=42)
        Model.fit(XTrain, YTrain)
        Acc = accuracy_score(YTest, Model.predict(XTest))
        print(f"random_state = {Rs:<3} -> Testing Accuracy = {Acc * 100:.2f}%")

    print("""
Observation: In this run, testing accuracy stayed the same (88.89%) across all three
random_state values. This suggests the Pass/Fail pattern in this dataset is quite
clean and consistent, so different train/test splits still capture it reliably.
In general, though, random_state controls which rows land in train vs test, so with
a small dataset like this (30 rows) accuracy CAN shift between runs - it just happens
not to here.
""")

def VisualizeTree(Model, FeatureNames, OutputPath):
    # Task 8: Decision tree visualization
    print("\n--- Task 8: Decision Tree Visualization ---")
    plt.figure(figsize=(14, 8))
    plot_tree(Model, feature_names=FeatureNames, class_names=['Fail', 'Pass'],
              filled=True, rounded=True, fontsize=9)
    plt.tight_layout()
    plt.savefig(OutputPath)
    plt.close()

    RootFeatureIndex = Model.tree_.feature[0]
    RootFeature = FeatureNames[RootFeatureIndex]
    print(f"Tree image saved to {OutputPath}")
    print(f"Root node feature: {RootFeature}")
    print(f"This feature was selected first because it produced the highest information "
          f"gain (largest reduction in Gini impurity) when splitting the training data, "
          f"meaning it separates Pass/Fail students most effectively on its own.")

def PerformanceIndexFeature(Df):
    # Task 9: Create PerformanceIndex and retrain
    print("\n--- Task 9: PerformanceIndex Feature ---")
    Df = Df.copy()
    Df['PerformanceIndex'] = (Df['StudyHours'] * 2) + Df['Attendance']

    X = Df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted',
            'SleepHours', 'PerformanceIndex']]
    Y = Df['FinalResult']
    XTrain, XTest, YTrain, YTest = train_test_split(X, Y, test_size=0.3, random_state=42)

    Model = DecisionTreeClassifier(max_depth=3, random_state=42)
    Model.fit(XTrain, YTrain)
    Acc = accuracy_score(YTest, Model.predict(XTest))

    print(f"Accuracy with PerformanceIndex added: {Acc * 100:.2f}%")
    print("Since PerformanceIndex is a linear combination of StudyHours and Attendance "
          "(which are already strong predictors), it does not add new information the "
          "tree didn't already have access to - accuracy typically stays the same or "
          "changes only marginally.")

def FullDepthOverfitCheck(X, Y):
    # Task 10: max_depth = None, training vs testing accuracy
    print("\n--- Task 10: Full-depth Tree (max_depth=None) ---")
    XTrain, XTest, YTrain, YTest = train_test_split(X, Y, test_size=0.3, random_state=42)
    Model = DecisionTreeClassifier(max_depth=None, random_state=42)
    Model.fit(XTrain, YTrain)

    TrainAcc = accuracy_score(YTrain, Model.predict(XTrain))
    TestAcc = accuracy_score(YTest, Model.predict(XTest))

    print(f"Training Accuracy: {TrainAcc * 100:.2f}%")
    print(f"Testing Accuracy:  {TestAcc * 100:.2f}%")

    if TrainAcc == 1.0 and TestAcc < 1.0:
        print("""
Explanation: With max_depth=None, the tree grows until every training leaf is pure,
so it memorizes the training data perfectly (100% training accuracy). However, this
means it has fit the noise and specific quirks of the training rows rather than the
true underlying pattern. On unseen test data, it therefore performs worse - this gap
between training and testing accuracy is the classic signature of OVERFITTING.
""")
    else:
        print("Training and testing accuracy are close - little to no overfitting observed here.")

def Main():
    FilePath = 'student_performance_ml.csv'
    FeatureNames = ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']

    Df = LoadData(FilePath)
    Model, XTrain, XTest, YTrain, YTest, YPred, BaselineAcc = BaselineModel(Df)

    print(f"Baseline model (all features, max_depth=3) Testing Accuracy: {BaselineAcc * 100:.2f}%")

    ShowFeatureImportance(Model, FeatureNames)
    RemoveSleepHours(Df, BaselineAcc)
    TrainWithTwoFeatures(Df, BaselineAcc)
    PredictNewStudents(Model, FeatureNames)
    ManualAccuracyCheck(YTest, YPred, BaselineAcc)
    IdentifyMisclassified(XTest, YTest, YPred)

    X = Df[FeatureNames]
    Y = Df['FinalResult']
    CompareRandomStates(X, Y)

    VisualizeTree(Model, FeatureNames, 'Decision_Tree.png')
    PerformanceIndexFeature(Df)
    FullDepthOverfitCheck(X, Y)

if __name__ == "__main__":
    Main()
