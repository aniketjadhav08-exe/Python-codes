########################################################################
# Marvellous Infosystems : Python - Automation & Machine Learning
# Machine Learning Assignment - Advertising Dataset
# Linear Regression to predict Sales from TV, Radio, Newspaper spend
########################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

########################################################################
# Function name :  GetData
# Description   :  Load the advertising dataset from CSV file
# Input         :  Path of CSV file
# Output        :  Pandas DataFrame containing the dataset
########################################################################
def GetData(Path):
    Dataset = pd.read_csv(Path)
    return Dataset

########################################################################
# Function name :  PrepareData
# Description   :  Separate the dataset into Features (X) and Label (y)
# Input         :  Pandas DataFrame
# Output        :  Feature matrix X, Label vector y
########################################################################
def PrepareData(Dataset):
    X = Dataset[["TV", "radio", "newspaper"]]
    Y = Dataset["sales"]
    return X, Y

########################################################################
# Function name :  TrainData
# Description   :  Split dataset into training and testing halves and
#                   train a Linear Regression model on the training half
# Input         :  Feature matrix X, Label vector Y
# Output        :  Trained model, X_test, Y_test
########################################################################
def TrainData(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state = 42)

    Model = LinearRegression()
    Model.fit(X_train, Y_train)

    return Model, X_test, Y_test

########################################################################
# Function name :  TestData
# Description   :  Test the trained model using the remaining half
#                   of the dataset and return the predictions
# Input         :  Trained model, X_test
# Output        :  Predicted values array
########################################################################
def TestData(Model, X_test):
    Predicted = Model.predict(X_test)
    return Predicted

########################################################################
# Function name :  DisplayResult
# Description   :  Display predicted values against expected(actual)
#                   values and print evaluation metrics
# Input         :  Y_test (expected), Predicted (predicted by model)
# Output        :  None (prints to console / log)
########################################################################
def DisplayResult(Y_test, Predicted):
    ResultFrame = pd.DataFrame({"Expected Sales": Y_test.values, "Predicted Sales": Predicted})
    ResultFrame["Predicted Sales"] = ResultFrame["Predicted Sales"].round(2)

    print("Expected vs Predicted Sales Values")
    print(ResultFrame.to_string(index = False))

    MSE = mean_squared_error(Y_test, Predicted)
    R2Score = r2_score(Y_test, Predicted)

    print("\nMean Squared Error is : ", round(MSE, 2))
    print("R Square Score is : ", round(R2Score, 2))

########################################################################
# Function name :  PlotResult
# Description   :  Plot Expected vs Predicted sales values and save
#                   the plot as a PNG image
# Input         :  Y_test (expected), Predicted (predicted by model)
# Output        :  None (saves PNG file)
########################################################################
def PlotResult(Y_test, Predicted):
    plt.figure(figsize = (8, 6))
    plt.scatter(Y_test, Predicted, color = "blue")
    plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color = "red", linewidth = 2)
    plt.xlabel("Expected Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Expected vs Predicted Sales - Linear Regression")
    plt.tight_layout()
    plt.savefig("AdvertisingLinearRegression.png")
    plt.close()
    print("\nPlot saved as AdvertisingLinearRegression.png")

########################################################################
# Function name :  Main
# Description   :  Entry point function which drives complete flow of
#                   Linear Regression application on Advertising dataset
# Input         :  None
# Output        :  None
########################################################################
def Main():
    Path = "Advertising.csv"

    # Step 1 : Get Data
    Dataset = GetData(Path)
    print("Dataset loaded successfully. Total records : ", len(Dataset))

    # Step 2 : Clean, Prepare and Manipulate data
    X, Y = PrepareData(Dataset)

    # Step 3 : Train Data
    Model, X_test, Y_test = TrainData(X, Y)
    print("Model trained successfully.")

    # Step 4 : Test the data
    Predicted = TestData(Model, X_test)

    # Step 5 : Display predicted vs expected values
    DisplayResult(Y_test, Predicted)

    # Extra : Save comparison plot
    PlotResult(Y_test, Predicted)

########################################################################
# Application starter
########################################################################
if __name__ == "__main__":
    Main()
