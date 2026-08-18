########################################################################
# Marvellous Infosystems : Python - Automation & Machine Learning
# Machine Learning Project : Breast Cancer Prediction
# Dataset : Breast Cancer Wisconsin (via sklearn load_breast_cancer)
# Target  : 0 = Malignant , 1 = Benign
########################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

########################################################################
# Function name :  GetData
# Description   :  Load the Breast Cancer dataset using sklearn's
#                   built-in loader and convert it into a DataFrame
# Input         :  None
# Output        :  DataFrame containing features and target column
########################################################################
def GetData():
    Cancer = load_breast_cancer()
    Dataset = pd.DataFrame(Cancer.data, columns = Cancer.feature_names)
    Dataset["target"] = Cancer.target
    return Dataset, Cancer.target_names

########################################################################
# Function name :  ExploreData
# Description   :  Display basic exploratory details about the dataset
# Input         :  DataFrame
# Output        :  None (prints information to console)
########################################################################
def ExploreData(Dataset):
    print("Shape of dataset : ", Dataset.shape)
    print("\nFirst 5 records :\n", Dataset.head())
    print("\nDataset info :")
    print(Dataset.info())
    print("\nSummary statistics :\n", Dataset.describe())
    print("\nTarget class distribution :\n", Dataset["target"].value_counts())

########################################################################
# Function name :  CheckMissingValues
# Description   :  Check whether the dataset contains any missing /
#                   null values in any column
# Input         :  DataFrame
# Output        :  None (prints missing value count)
########################################################################
def CheckMissingValues(Dataset):
    MissingValues = Dataset.isnull().sum()
    print("\nMissing values per column :\n", MissingValues[MissingValues > 0])
    print("Total missing values in dataset : ", Dataset.isnull().sum().sum())

########################################################################
# Function name :  PlotCorrelation
# Description   :  Visualize correlation between a subset of features
#                   and save the heatmap as a PNG image
# Input         :  DataFrame
# Output        :  None (saves PNG file)
########################################################################
def PlotCorrelation(Dataset):
    # Use first 10 mean features for a readable heatmap
    SubsetColumns = list(Dataset.columns[0:10]) + ["target"]
    CorrMatrix = Dataset[SubsetColumns].corr()

    plt.figure(figsize = (10, 8))
    sns.heatmap(CorrMatrix, annot = True, fmt = ".2f", cmap = "coolwarm")
    plt.title("Feature Correlation Heatmap (Mean Features)")
    plt.tight_layout()
    plt.savefig("BreastCancerCorrelationHeatmap.png")
    plt.close()
    print("\nCorrelation heatmap saved as BreastCancerCorrelationHeatmap.png")

########################################################################
# Function name :  PrepareData
# Description   :  Separate features and target, then split into
#                   training and testing sets, and scale the features
# Input         :  DataFrame
# Output        :  X_train, X_test, Y_train, Y_test (scaled)
########################################################################
def PrepareData(Dataset):
    X = Dataset.drop(columns = ["target"])
    Y = Dataset["target"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

    Scaler = StandardScaler()
    X_train_Scaled = Scaler.fit_transform(X_train)
    X_test_Scaled = Scaler.transform(X_test)

    return X_train_Scaled, X_test_Scaled, Y_train, Y_test

########################################################################
# Function name :  TrainModel
# Description   :  Build and train a Decision Tree classification model
# Input         :  X_train, Y_train
# Output        :  Trained model
########################################################################
def TrainModel(X_train, Y_train):
    Model = DecisionTreeClassifier(random_state = 42)
    Model.fit(X_train, Y_train)
    return Model

########################################################################
# Function name :  EvaluateModel
# Description   :  Evaluate the trained model using Accuracy,
#                   Confusion Matrix, and Classification Report
# Input         :  Model, X_test, Y_test, TargetNames
# Output        :  None (prints evaluation results, saves confusion
#                   matrix plot)
########################################################################
def EvaluateModel(Model, X_test, Y_test, TargetNames):
    Predicted = Model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Predicted)
    ConfMatrix = confusion_matrix(Y_test, Predicted)
    Report = classification_report(Y_test, Predicted, target_names = TargetNames)

    print("\nAccuracy of the model is : ", round(Accuracy * 100, 2), "%")
    print("\nConfusion Matrix :\n", ConfMatrix)
    print("\nClassification Report :\n", Report)

    plt.figure(figsize = (6, 5))
    sns.heatmap(ConfMatrix, annot = True, fmt = "d", cmap = "Blues",
                xticklabels = TargetNames, yticklabels = TargetNames)
    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")
    plt.title("Confusion Matrix - Breast Cancer Prediction")
    plt.tight_layout()
    plt.savefig("BreastCancerConfusionMatrix.png")
    plt.close()
    print("\nConfusion matrix plot saved as BreastCancerConfusionMatrix.png")

########################################################################
# Function name :  Main
# Description   :  Entry point function which drives the complete
#                   Breast Cancer Prediction ML pipeline
# Input         :  None
# Output        :  None
########################################################################
def Main():
    # Step 1 : Load and explore the dataset
    Dataset, TargetNames = GetData()
    ExploreData(Dataset)

    # Step 2 : Data preprocessing - missing values
    CheckMissingValues(Dataset)

    # Step 3 : Exploratory Data Analysis - correlation visualization
    PlotCorrelation(Dataset)

    # Step 4 : Split into training/testing sets and scale features
    X_train, X_test, Y_train, Y_test = PrepareData(Dataset)

    # Step 5 : Build classification model
    Model = TrainModel(X_train, Y_train)
    print("\nModel trained successfully using Decision Tree Classifier.")

    # Step 6 : Evaluate the model
    EvaluateModel(Model, X_test, Y_test, TargetNames)

    # Step 7 : Observations and Conclusions
    print("\n----------------------- Observations -----------------------")
    print("1. The dataset is clean with no missing values.")
    print("2. Features like 'mean radius', 'mean perimeter', and 'mean area'")
    print("   are strongly correlated with each other and with the target.")
    print("3. Feature scaling was applied since the features vary widely in range")
    print("   (e.g. area vs smoothness), which helps distance/threshold-based models.")
    print("4. The Decision Tree model achieved good accuracy on the test set,")
    print("   indicating the selected features are strong predictors of tumor type.")
    print("5. Precision and Recall values (see classification report above) indicate")
    print("   how reliably the model distinguishes Malignant vs Benign cases.")
    print("---------------------------------------------------------------")

########################################################################
# Application starter
########################################################################
if __name__ == "__main__":
    Main()
