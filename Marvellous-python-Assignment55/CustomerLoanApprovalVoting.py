###############################################################################
# Marvellous Infosystems : Python - Automation & Machine Learning
#
# Assignment Name : Customer Loan Approval Using Voting Classification
#
# Description :
#   A bank wants to automate its loan approval process based on historical
#   customer data. Instead of relying on a single Machine Learning algorithm,
#   the bank wants predictions to be made using a Voting Classifier that
#   combines Logistic Regression, Decision Tree and K-Nearest Neighbors.
#
#   Features   : Age, Income, CreditScore, ExistingLoan, EmploymentExperience,
#                LoanAmount
#   Target     : LoanApproved  (0 -> Loan Rejected, 1 -> Loan Approved)
#
# Tasks performed :
#   1.  Load the dataset.
#   2.  Check for missing values.
#   3.  Separate input and output variables.
#   4.  Split the dataset into training and testing data.
#   5.  Train Logistic Regression.
#   6.  Train Decision Tree.
#   7.  Train KNN.
#   8.  Calculate the individual accuracy of all three algorithms.
#   9.  Create a Hard Voting Classifier.
#   10. Calculate its accuracy.
#   11. Create a Soft Voting Classifier.
#   12. Calculate its accuracy.
#   13. Compare all five models' accuracies.
#
# Author : Aniket Jadhav
###############################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

DatasetPath = "Customer_Loan_Approval.csv"


###############################################################################
# Function Name :   LoadDataset
# Description   :   Loads the real customer loan dataset (Customer_Loan_
#                    Approval.csv) supplied for this assignment.
# Input         :   None
# Output        :   Pandas DataFrame
###############################################################################
def LoadDataset():
    Data = pd.read_csv(DatasetPath)
    print(f"Dataset loaded from {DatasetPath}")
    return Data


###############################################################################
# Function Name :   CheckMissingValues
# Description   :   Checks the dataset for missing / null values column-wise.
# Input         :   Pandas DataFrame
# Output        :   None (prints the missing value summary)
###############################################################################
def CheckMissingValues(Data):
    print("\nMissing values in each column :")
    print(Data.isnull().sum())


###############################################################################
# Function Name :   SplitInputOutput
# Description   :   Separates the dataset into input features (X) and the
#                    target column (Y).
# Input         :   Pandas DataFrame
# Output        :   X (features), Y (target)
###############################################################################
def SplitInputOutput(Data):
    X = Data.drop(columns=["LoanApproved"])
    Y = Data["LoanApproved"]
    return X, Y


###############################################################################
# Function Name :   TrainIndividualModels
# Description   :   Trains Logistic Regression, Decision Tree and KNN on the
#                    scaled training data and evaluates each on the test set.
# Input         :   Scaled training/testing data and labels
# Output        :   Dictionary of trained models and a dictionary of their
#                    individual accuracies
###############################################################################
def TrainIndividualModels(XTrain, XTest, YTrain, YTest):
    LogisticModel = LogisticRegression()
    DecisionTreeModel = DecisionTreeClassifier(max_depth=5, random_state=42)
    KnnModel = KNeighborsClassifier(n_neighbors=5)

    LogisticModel.fit(XTrain, YTrain)
    DecisionTreeModel.fit(XTrain, YTrain)
    KnnModel.fit(XTrain, YTrain)

    LogisticAccuracy = accuracy_score(YTest, LogisticModel.predict(XTest))
    DecisionTreeAccuracy = accuracy_score(YTest, DecisionTreeModel.predict(XTest))
    KnnAccuracy = accuracy_score(YTest, KnnModel.predict(XTest))

    Models = {
        "Logistic Regression": LogisticModel,
        "Decision Tree": DecisionTreeModel,
        "KNN": KnnModel
    }

    Accuracies = {
        "Logistic Regression": LogisticAccuracy,
        "Decision Tree": DecisionTreeAccuracy,
        "KNN": KnnAccuracy
    }

    return Models, Accuracies


###############################################################################
# Function Name :   BuildVotingClassifiers
# Description   :   Builds a Hard Voting Classifier and a Soft Voting
#                    Classifier using the same three base estimators, trains
#                    both and evaluates their accuracy on the test set.
# Input         :   Scaled training/testing data and labels
# Output        :   Dictionary containing HardVoting and SoftVoting accuracy
###############################################################################
def BuildVotingClassifiers(XTrain, XTest, YTrain, YTest):
    Estimators = [
        ("lr", LogisticRegression()),
        ("dt", DecisionTreeClassifier(max_depth=5, random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ]

    HardVotingModel = VotingClassifier(estimators=Estimators, voting="hard")
    HardVotingModel.fit(XTrain, YTrain)
    HardVotingAccuracy = accuracy_score(YTest, HardVotingModel.predict(XTest))

    SoftVotingModel = VotingClassifier(estimators=Estimators, voting="soft")
    SoftVotingModel.fit(XTrain, YTrain)
    SoftVotingAccuracy = accuracy_score(YTest, SoftVotingModel.predict(XTest))

    VotingAccuracies = {
        "Hard Voting": HardVotingAccuracy,
        "Soft Voting": SoftVotingAccuracy
    }

    return HardVotingModel, SoftVotingModel, VotingAccuracies


###############################################################################
# Function Name :   DisplayComparison
# Description   :   Prints a comparison table of all five models' accuracies
#                    and saves a bar chart comparing them visually.
# Input         :   Dictionary of all model accuracies
# Output        :   None (prints table, saves LoanApprovalAccuracyComparison.png)
###############################################################################
def DisplayComparison(AllAccuracies):
    print("\n" + "=" * 45)
    print(f"{'Model':<20}{'Accuracy':>15}")
    print("=" * 45)
    for ModelName, Accuracy in AllAccuracies.items():
        print(f"{ModelName:<20}{Accuracy * 100:>14.2f}%")
    print("=" * 45)

    BestModel = max(AllAccuracies, key=AllAccuracies.get)
    print(f"\nBest performing model : {BestModel} "
          f"({AllAccuracies[BestModel] * 100:.2f}% accuracy)")

    plt.figure(figsize=(8, 5))
    plt.bar(AllAccuracies.keys(), [Value * 100 for Value in AllAccuracies.values()],
            color=["#4C72B0", "#55A868", "#C44E52", "#8172B2", "#CCB974"])
    plt.ylabel("Accuracy (%)")
    plt.title("Model Accuracy Comparison - Loan Approval")
    plt.ylim(0, 100)
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("LoanApprovalAccuracyComparison.png")
    print("\nComparison chart saved as LoanApprovalAccuracyComparison.png")


###############################################################################
# Function Name :   Main
# Description   :   Entry point that drives the complete Customer Loan
#                    Approval Voting Classification pipeline end to end.
# Input         :   None
# Output        :   None
###############################################################################
def Main():
    print("---------- Customer Loan Approval Using Voting Classification ----------")

    # Step 1 : Load the dataset
    Data = LoadDataset()
    print(f"\nDataset shape : {Data.shape}")
    print("\nFirst 5 records :")
    print(Data.head())

    # Step 2 : Check for missing values
    CheckMissingValues(Data)

    # Step 3 : Separate input and output variables
    X, Y = SplitInputOutput(Data)

    # Step 4 : Split the dataset into training and testing data
    XTrain, XTest, YTrain, YTest = train_test_split(
        X, Y, test_size=0.2, random_state=42, stratify=Y)

    # Feature scaling (helps Logistic Regression & KNN converge/perform well)
    Scaler = StandardScaler()
    XTrainScaled = Scaler.fit_transform(XTrain)
    XTestScaled = Scaler.transform(XTest)

    # Step 5, 6, 7, 8 : Train individual models & get their accuracy
    Models, IndividualAccuracies = TrainIndividualModels(
        XTrainScaled, XTestScaled, YTrain, YTest)

    # Step 9, 10, 11, 12 : Build Hard & Soft Voting Classifiers
    HardVotingModel, SoftVotingModel, VotingAccuracies = BuildVotingClassifiers(
        XTrainScaled, XTestScaled, YTrain, YTest)

    # Step 13 : Compare all models
    AllAccuracies = {**IndividualAccuracies, **VotingAccuracies}
    DisplayComparison(AllAccuracies)


if __name__ == "__main__":
    Main()
