"""
Employee_Attrition_MLP.py

Marvellous Infosystems : Python - Automation & Machine Learning
Deep Learning Assignment - Employee Attrition Prediction System

Problem Statement:
A software company is experiencing high employee turnover. Management wants
an intelligent system that can identify employees who are likely to leave
the company, using historical HR data stored in Employee_Attrition.csv.

This script builds a Deep Learning based Employee Attrition Prediction
System using sklearn's MLPClassifier (Multi Layer Perceptron), covering
data loading, preprocessing, model training, evaluation and prediction
on new/unseen employee records.

Target:
    0 -> Employee is likely to stay
    1 -> Employee is likely to leave
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

CSV_PATH = "Employee_Attrition.csv"


def LoadDataset(Path):
    """
    Task 1: Load the dataset using Pandas.
    """
    DataFrame = pd.read_csv(Path)
    return DataFrame


def DisplayDatasetInfo(DataFrame):
    """
    Task 2: Display the shape, columns and first five records.
    """
    print("\n--- Dataset Shape ---")
    print(DataFrame.shape)

    print("\n--- Dataset Columns ---")
    print(list(DataFrame.columns))

    print("\n--- First Five Records ---")
    print(DataFrame.head())


def CheckMissingValues(DataFrame):
    """
    Task 3: Check for missing values.
    """
    print("\n--- Missing Values Per Column ---")
    MissingCounts = DataFrame.isnull().sum()
    print(MissingCounts)
    return MissingCounts


def IdentifyFeatureTypes(DataFrame):
    """
    Task 4: Identify numerical and categorical features.
    """
    NumericalFeatures = DataFrame.select_dtypes(include=[np.number]).columns.tolist()
    CategoricalFeatures = DataFrame.select_dtypes(include=["object", "category"]).columns.tolist()

    print("\n--- Numerical Features ---")
    print(NumericalFeatures)

    print("\n--- Categorical Features ---")
    print(CategoricalFeatures)

    return NumericalFeatures, CategoricalFeatures


def EncodeOverTime(DataFrame):
    """
    Task 5: Convert categorical features such as OverTime into numerical
    representation (Yes -> 1, No -> 0).
    """
    DataFrame["OverTime"] = DataFrame["OverTime"].map({"Yes": 1, "No": 0})
    return DataFrame


def EncodeTarget(DataFrame):
    """
    Task 6: Convert the target Attrition into 0 and 1.
    Yes -> 1 (likely to leave), No -> 0 (likely to stay)
    """
    DataFrame["Attrition"] = DataFrame["Attrition"].map({"Yes": 1, "No": 0})
    return DataFrame


def SeparateFeaturesAndTarget(DataFrame):
    """
    Task 7: Separate independent and dependent variables.
    """
    XFeatures = DataFrame.drop(columns=["Attrition"])
    YTarget = DataFrame["Attrition"]
    return XFeatures, YTarget


def SplitDataset(XFeatures, YTarget, TestSize=0.2, RandomState=42):
    """
    Task 8: Divide the dataset into training and testing data.
    """
    XTrain, XTest, YTrain, YTest = train_test_split(
        XFeatures, YTarget, test_size=TestSize, random_state=RandomState, stratify=YTarget
    )
    return XTrain, XTest, YTrain, YTest


def ApplyFeatureScaling(XTrain, XTest):
    """
    Task 9: Apply appropriate feature scaling.
    MLPClassifier (like most neural networks) is sensitive to feature
    magnitude, so StandardScaler is used to standardize features to
    zero mean and unit variance.
    """
    Scaler = StandardScaler()
    XTrainScaled = Scaler.fit_transform(XTrain)
    XTestScaled = Scaler.transform(XTest)
    return XTrainScaled, XTestScaled, Scaler


def BuildAndTrainModel(XTrainScaled, YTrain):
    """
    Task 10: Design an MLP with at least two hidden layers.
    Task 11: Train the network.
    """
    Model = MLPClassifier(
        hidden_layer_sizes=(16, 8),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42,
    )
    Model.fit(XTrainScaled, YTrain)
    return Model


def DisplayIterations(Model):
    """
    Task 12: Display the number of iterations required for training.
    """
    print("\n--- Training Iterations ---")
    print("Number of iterations used:", Model.n_iter_)


def CalculateAccuracies(Model, XTrainScaled, YTrain, XTestScaled, YTest):
    """
    Task 13: Calculate training accuracy.
    Task 14: Calculate testing accuracy.
    """
    TrainPredictions = Model.predict(XTrainScaled)
    TestPredictions = Model.predict(XTestScaled)

    TrainingAccuracy = accuracy_score(YTrain, TrainPredictions)
    TestingAccuracy = accuracy_score(YTest, TestPredictions)

    print("\n--- Accuracy ---")
    print("Training Accuracy :", round(TrainingAccuracy * 100, 2), "%")
    print("Testing Accuracy  :", round(TestingAccuracy * 100, 2), "%")

    return TrainingAccuracy, TestingAccuracy, TestPredictions


def GenerateConfusionMatrix(YTest, TestPredictions):
    """
    Task 15: Generate a confusion matrix.
    """
    Matrix = confusion_matrix(YTest, TestPredictions)
    print("\n--- Confusion Matrix ---")
    print(Matrix)

    Display = ConfusionMatrixDisplay(confusion_matrix=Matrix, display_labels=["Stay", "Leave"])
    Display.plot(cmap="Blues")
    plt.title("Employee Attrition - Confusion Matrix")
    plt.savefig("EmployeeAttritionConfusionMatrix.png")
    plt.close()
    print("Confusion matrix plot saved as EmployeeAttritionConfusionMatrix.png")

    return Matrix


def PlotLossCurve(Model):
    """
    Task 16: Plot the loss curve.
    """
    plt.figure()
    plt.plot(Model.loss_curve_)
    plt.title("MLPClassifier Training Loss Curve")
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.savefig("EmployeeAttritionLossCurve.png")
    plt.close()
    print("Loss curve plot saved as EmployeeAttritionLossCurve.png")


def PredictAttrition(EmployeeData, Model, Scaler, ColumnOrder):
    """
    Task 17: Create a function PredictAttrition(employee_data) that accepts
    a dictionary of employee features, scales it using the fitted scaler,
    and returns the predicted attrition label.

    EmployeeData: dict with keys matching the original feature columns.
    """
    InputFrame = pd.DataFrame([EmployeeData])
    InputFrame = InputFrame[ColumnOrder]
    InputScaled = Scaler.transform(InputFrame)

    Prediction = Model.predict(InputScaled)[0]
    Probability = Model.predict_proba(InputScaled)[0][1]

    Label = "Likely to LEAVE" if Prediction == 1 else "Likely to STAY"
    return Prediction, Label, Probability


def TestNewEmployeeRecords(Model, Scaler, ColumnOrder):
    """
    Task 18: Test the system using at least five new employee records.
    """
    NewEmployees = [
        {
            "Age": 29, "MonthlyIncome": 28000, "YearsAtCompany": 1,
            "TotalWorkingYears": 3, "DistanceFromHome": 32,
            "JobSatisfaction": 1, "WorkLifeBalance": 1, "OverTime": 1,
            "NumCompaniesWorked": 4, "TrainingTimesLastYear": 0,
        },
        {
            "Age": 45, "MonthlyIncome": 95000, "YearsAtCompany": 18,
            "TotalWorkingYears": 22, "DistanceFromHome": 5,
            "JobSatisfaction": 4, "WorkLifeBalance": 4, "OverTime": 0,
            "NumCompaniesWorked": 1, "TrainingTimesLastYear": 4,
        },
        {
            "Age": 34, "MonthlyIncome": 42000, "YearsAtCompany": 4,
            "TotalWorkingYears": 8, "DistanceFromHome": 18,
            "JobSatisfaction": 2, "WorkLifeBalance": 2, "OverTime": 1,
            "NumCompaniesWorked": 3, "TrainingTimesLastYear": 1,
        },
        {
            "Age": 51, "MonthlyIncome": 68000, "YearsAtCompany": 20,
            "TotalWorkingYears": 25, "DistanceFromHome": 3,
            "JobSatisfaction": 3, "WorkLifeBalance": 4, "OverTime": 0,
            "NumCompaniesWorked": 2, "TrainingTimesLastYear": 3,
        },
        {
            "Age": 24, "MonthlyIncome": 19000, "YearsAtCompany": 0,
            "TotalWorkingYears": 1, "DistanceFromHome": 37,
            "JobSatisfaction": 1, "WorkLifeBalance": 1, "OverTime": 1,
            "NumCompaniesWorked": 2, "TrainingTimesLastYear": 0,
        },
    ]

    print("\n--- Predictions On New Employee Records ---")
    for Index, Employee in enumerate(NewEmployees, start=1):
        Prediction, Label, Probability = PredictAttrition(Employee, Model, Scaler, ColumnOrder)
        print(f"Employee {Index}: {Label}  (Probability of leaving: {round(Probability * 100, 1)}%)")


def AnalyzeFitting(TrainingAccuracy, TestingAccuracy):
    """
    Task 19: Explain whether the model is suffering from overfitting or
    underfitting, based on the gap between training and testing accuracy.
    """
    Gap = TrainingAccuracy - TestingAccuracy

    print("\n--- Overfitting / Underfitting Analysis ---")
    print("Training Accuracy :", round(TrainingAccuracy * 100, 2), "%")
    print("Testing Accuracy  :", round(TestingAccuracy * 100, 2), "%")
    print("Gap (Train - Test):", round(Gap * 100, 2), "%")

    if TrainingAccuracy < 0.75 and TestingAccuracy < 0.75:
        Verdict = (
            "The model shows UNDERFITTING: both training and testing accuracy "
            "are low, meaning the network has not learned the underlying "
            "patterns well enough (consider more hidden units, more training "
            "iterations, or better features)."
        )
    elif Gap > 0.12:
        Verdict = (
            "The model shows signs of OVERFITTING: training accuracy is "
            "notably higher than testing accuracy, meaning the network has "
            "memorized the training data rather than generalizing well."
        )
    else:
        Verdict = (
            "The model appears to be a GOOD FIT: training and testing "
            "accuracy are close to each other, indicating the network "
            "generalizes reasonably well to unseen data."
        )

    print(Verdict)
    return Verdict


def Main():
    DataFrame = LoadDataset(CSV_PATH)
    DisplayDatasetInfo(DataFrame)
    CheckMissingValues(DataFrame)
    IdentifyFeatureTypes(DataFrame)

    DataFrame = EncodeOverTime(DataFrame)
    DataFrame = EncodeTarget(DataFrame)

    XFeatures, YTarget = SeparateFeaturesAndTarget(DataFrame)
    ColumnOrder = list(XFeatures.columns)

    XTrain, XTest, YTrain, YTest = SplitDataset(XFeatures, YTarget)
    XTrainScaled, XTestScaled, Scaler = ApplyFeatureScaling(XTrain, XTest)

    Model = BuildAndTrainModel(XTrainScaled, YTrain)
    DisplayIterations(Model)

    TrainingAccuracy, TestingAccuracy, TestPredictions = CalculateAccuracies(
        Model, XTrainScaled, YTrain, XTestScaled, YTest
    )

    GenerateConfusionMatrix(YTest, TestPredictions)
    PlotLossCurve(Model)

    TestNewEmployeeRecords(Model, Scaler, ColumnOrder)
    AnalyzeFitting(TrainingAccuracy, TestingAccuracy)


if __name__ == "__main__":
    Main()
