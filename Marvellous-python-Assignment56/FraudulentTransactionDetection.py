###############################################################################
# Marvellous Infosystems : Python - Automation & Machine Learning
#
# Assignment Name : Fraudulent Transaction Detection
#
# Description :
#   A financial institution wants to detect potentially fraudulent
#   transactions. Multiple ensemble approaches are investigated and compared
#   to recommend the most suitable model.
#
#   Features   : TransactionAmount, TransactionHour, AccountAgeMonths,
#                PreviousTransactions, LocationDifferenceKm, DeviceType,
#                FailedLoginAttempts
#   Target     : Fraud  (0 -> Normal Transaction, 1 -> Fraudulent Transaction)
#
# Tasks performed :
#   Build and compare :
#       1. Decision Tree
#       2. Bagging Classifier
#       3. Random Forest Classifier
#       4. AdaBoost Classifier
#       5. Voting Classifier
#   Evaluate each model using : Accuracy, Precision, Recall, F1 Score,
#   Confusion Matrix, and prepare a final comparison table.
#
# Author : Aniket Jadhav
###############################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

DatasetPath = "Fraudulent_Transaction_Detection.csv"


###############################################################################
# Function Name :   LoadDataset
# Description   :   Loads the fraudulent transaction dataset supplied for
#                    this assignment.
# Input         :   None
# Output        :   Pandas DataFrame
###############################################################################
def LoadDataset():
    Data = pd.read_csv(DatasetPath)
    print(f"Dataset loaded from {DatasetPath}")
    return Data


###############################################################################
# Function Name :   CheckMissingValues
# Description   :   Checks the dataset for missing / null values column-wise
#                    and reports the class balance of the target column.
# Input         :   Pandas DataFrame
# Output        :   None (prints summary)
###############################################################################
def CheckMissingValues(Data):
    print("\nMissing values in each column :")
    print(Data.isnull().sum())

    print("\nClass distribution (Fraud column) :")
    print(Data["Fraud"].value_counts())
    FraudRate = Data["Fraud"].mean() * 100
    print(f"Fraud rate in dataset : {FraudRate:.1f}%")


###############################################################################
# Function Name :   SplitInputOutput
# Description   :   Separates the dataset into input features (X) and the
#                    target column (Y).
# Input         :   Pandas DataFrame
# Output        :   X (features), Y (target)
###############################################################################
def SplitInputOutput(Data):
    X = Data.drop(columns=["Fraud"])
    Y = Data["Fraud"]
    return X, Y


###############################################################################
# Function Name :   EvaluateModel
# Description   :   Trains the given model, predicts on the test set and
#                    computes Accuracy, Precision, Recall, F1 Score and the
#                    Confusion Matrix. zero_division=0 guards Precision/Recall
#                    against undefined values when a class is never predicted
#                    (a realistic risk given the fraud class is a minority).
# Input         :   Model object, ModelName, training/testing data & labels
# Output        :   Dictionary of metric name -> value, fitted model
###############################################################################
def EvaluateModel(Model, ModelName, XTrain, XTest, YTrain, YTest):
    Model.fit(XTrain, YTrain)
    Predictions = Model.predict(XTest)

    Metrics = {
        "Accuracy": accuracy_score(YTest, Predictions),
        "Precision": precision_score(YTest, Predictions, zero_division=0),
        "Recall": recall_score(YTest, Predictions, zero_division=0),
        "F1": f1_score(YTest, Predictions, zero_division=0)
    }

    ConfusionMat = confusion_matrix(YTest, Predictions)
    print(f"\n--- {ModelName} ---")
    print(f"Accuracy  : {Metrics['Accuracy'] * 100:.2f}%")
    print(f"Precision : {Metrics['Precision'] * 100:.2f}%")
    print(f"Recall    : {Metrics['Recall'] * 100:.2f}%")
    print(f"F1 Score  : {Metrics['F1'] * 100:.2f}%")
    print("Confusion Matrix :")
    print(ConfusionMat)

    return Metrics, Model, ConfusionMat


###############################################################################
# Function Name :   BuildAndCompareModels
# Description   :   Builds Decision Tree, Bagging, Random Forest, AdaBoost
#                    and a Voting Classifier, evaluates each with
#                    EvaluateModel(), and collects results for comparison.
# Input         :   Scaled training/testing data and labels
# Output        :   Dictionary of ModelName -> Metrics,
#                    Dictionary of ModelName -> Confusion Matrix
###############################################################################
def BuildAndCompareModels(XTrain, XTest, YTrain, YTest):
    AllMetrics = {}
    AllConfusionMats = {}

    # 1. Decision Tree
    DecisionTreeModel = DecisionTreeClassifier(max_depth=5, random_state=42)
    Metrics, _, ConfMat = EvaluateModel(
        DecisionTreeModel, "Decision Tree", XTrain, XTest, YTrain, YTest)
    AllMetrics["Decision Tree"] = Metrics
    AllConfusionMats["Decision Tree"] = ConfMat

    # 2. Bagging Classifier (base estimator = Decision Tree)
    BaggingModel = BaggingClassifier(
        estimator=DecisionTreeClassifier(max_depth=5, random_state=42),
        n_estimators=50, random_state=42)
    Metrics, _, ConfMat = EvaluateModel(
        BaggingModel, "Bagging", XTrain, XTest, YTrain, YTest)
    AllMetrics["Bagging"] = Metrics
    AllConfusionMats["Bagging"] = ConfMat

    # 3. Random Forest Classifier
    RandomForestModel = RandomForestClassifier(
        n_estimators=100, max_depth=5, random_state=42)
    Metrics, _, ConfMat = EvaluateModel(
        RandomForestModel, "Random Forest", XTrain, XTest, YTrain, YTest)
    AllMetrics["Random Forest"] = Metrics
    AllConfusionMats["Random Forest"] = ConfMat

    # 4. AdaBoost Classifier
    AdaBoostModel = AdaBoostClassifier(n_estimators=100, random_state=42)
    Metrics, _, ConfMat = EvaluateModel(
        AdaBoostModel, "AdaBoost", XTrain, XTest, YTrain, YTest)
    AllMetrics["AdaBoost"] = Metrics
    AllConfusionMats["AdaBoost"] = ConfMat

    # 5. Voting Classifier (soft voting over Logistic Regression,
    #    Decision Tree and KNN - a mix of different model families)
    VotingModel = VotingClassifier(
        estimators=[
            ("lr", LogisticRegression(max_iter=1000)),
            ("dt", DecisionTreeClassifier(max_depth=5, random_state=42)),
            ("knn", KNeighborsClassifier(n_neighbors=5))
        ],
        voting="soft"
    )
    Metrics, _, ConfMat = EvaluateModel(
        VotingModel, "Voting", XTrain, XTest, YTrain, YTest)
    AllMetrics["Voting"] = Metrics
    AllConfusionMats["Voting"] = ConfMat

    return AllMetrics, AllConfusionMats


###############################################################################
# Function Name :   DisplayComparisonTable
# Description   :   Prints the final comparison table (Algorithm / Accuracy /
#                    Precision / Recall / F1) and recommends the most
#                    suitable model based on F1 Score (a better indicator
#                    than Accuracy for imbalanced fraud data).
# Input         :   Dictionary of ModelName -> Metrics
# Output        :   None (prints table and recommendation)
###############################################################################
def DisplayComparisonTable(AllMetrics):
    print("\n" + "=" * 65)
    print(f"{'Algorithm':<16}{'Accuracy':>12}{'Precision':>12}{'Recall':>12}{'F1':>12}")
    print("=" * 65)
    for ModelName, Metrics in AllMetrics.items():
        print(f"{ModelName:<16}"
              f"{Metrics['Accuracy'] * 100:>11.2f}%"
              f"{Metrics['Precision'] * 100:>11.2f}%"
              f"{Metrics['Recall'] * 100:>11.2f}%"
              f"{Metrics['F1'] * 100:>11.2f}%")
    print("=" * 65)

    # F1 Score balances Precision and Recall, which matters more than raw
    # Accuracy here since the Fraud class is the minority class.
    BestModel = max(AllMetrics, key=lambda Name: AllMetrics[Name]["F1"])
    print(f"\nRecommended model (highest F1 Score) : {BestModel} "
          f"(F1 = {AllMetrics[BestModel]['F1'] * 100:.2f}%)")


###############################################################################
# Function Name :   PlotComparisonChart
# Description   :   Saves a grouped bar chart comparing all four metrics
#                    across all five models.
# Input         :   Dictionary of ModelName -> Metrics
# Output        :   None (saves FraudDetectionMetricsComparison.png)
###############################################################################
def PlotComparisonChart(AllMetrics):
    ModelNames = list(AllMetrics.keys())
    MetricNames = ["Accuracy", "Precision", "Recall", "F1"]

    import numpy as np
    XPositions = np.arange(len(ModelNames))
    BarWidth = 0.2

    plt.figure(figsize=(11, 6))
    for Index, MetricName in enumerate(MetricNames):
        Values = [AllMetrics[Name][MetricName] * 100 for Name in ModelNames]
        plt.bar(XPositions + Index * BarWidth, Values, width=BarWidth, label=MetricName)

    plt.xticks(XPositions + BarWidth * 1.5, ModelNames, rotation=15)
    plt.ylabel("Score (%)")
    plt.title("Fraud Detection - Ensemble Model Comparison")
    plt.ylim(0, 105)
    plt.legend()
    plt.tight_layout()
    plt.savefig("FraudDetectionMetricsComparison.png")
    print("\nComparison chart saved as FraudDetectionMetricsComparison.png")


###############################################################################
# Function Name :   PlotConfusionMatrices
# Description   :   Saves a single figure containing the confusion matrix
#                    heatmap for every model, for visual comparison.
# Input         :   Dictionary of ModelName -> Confusion Matrix
# Output        :   None (saves FraudDetectionConfusionMatrices.png)
###############################################################################
def PlotConfusionMatrices(AllConfusionMats):
    ModelNames = list(AllConfusionMats.keys())
    Figure, Axes = plt.subplots(1, len(ModelNames), figsize=(20, 4))

    for Index, ModelName in enumerate(ModelNames):
        sns.heatmap(
            AllConfusionMats[ModelName], annot=True, fmt="d", cmap="Blues",
            xticklabels=["Normal", "Fraud"], yticklabels=["Normal", "Fraud"],
            ax=Axes[Index], cbar=False
        )
        Axes[Index].set_title(ModelName)
        Axes[Index].set_xlabel("Predicted")
        Axes[Index].set_ylabel("Actual")

    plt.tight_layout()
    plt.savefig("FraudDetectionConfusionMatrices.png")
    print("Confusion matrices saved as FraudDetectionConfusionMatrices.png")


###############################################################################
# Function Name :   Main
# Description   :   Entry point that drives the complete Fraudulent
#                    Transaction Detection ensemble comparison pipeline.
# Input         :   None
# Output        :   None
###############################################################################
def Main():
    print("---------- Fraudulent Transaction Detection ----------")

    Data = LoadDataset()
    print(f"\nDataset shape : {Data.shape}")
    print("\nFirst 5 records :")
    print(Data.head())

    CheckMissingValues(Data)

    X, Y = SplitInputOutput(Data)

    # Stratified split preserves the Fraud/Normal ratio in both train & test,
    # important since Fraud is the minority class here.
    XTrain, XTest, YTrain, YTest = train_test_split(
        X, Y, test_size=0.2, random_state=42, stratify=Y)

    Scaler = StandardScaler()
    XTrainScaled = Scaler.fit_transform(XTrain)
    XTestScaled = Scaler.transform(XTest)

    AllMetrics, AllConfusionMats = BuildAndCompareModels(
        XTrainScaled, XTestScaled, YTrain, YTest)

    DisplayComparisonTable(AllMetrics)
    PlotComparisonChart(AllMetrics)
    PlotConfusionMatrices(AllConfusionMats)


if __name__ == "__main__":
    Main()
