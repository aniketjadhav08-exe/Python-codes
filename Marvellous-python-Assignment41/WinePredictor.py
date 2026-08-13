import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def GetData(Path):
    DataFrame = pd.read_csv(Path)
    return DataFrame

def PrepareData(DataFrame):
    X = DataFrame.drop('Class', axis=1)
    Y = DataFrame['Class']

    Scaler = StandardScaler()
    XScaled = Scaler.fit_transform(X)

    return XScaled, Y

def TrainModel(XTrain, YTrain):
    Model = DecisionTreeClassifier(random_state=42)
    Model.fit(XTrain, YTrain)
    return Model

def TestModel(Model, XTest, YTest):
    Predictions = Model.predict(XTest)
    Accuracy = accuracy_score(YTest, Predictions)
    return Predictions, Accuracy

def Main():
    print("----- Wine Classification Application -----")

    # Step 1: Get Data
    Path = "WinePredictor.csv"   # change this to your actual file name/path
    DataFrame = GetData(Path)

    print("\nDataset Shape:", DataFrame.shape)
    print("\nColumns:\n", DataFrame.columns.tolist())
    print("\nFirst 5 records:\n", DataFrame.head())

    # Step 2: Clean, Prepare & Manipulate Data
    X, Y = PrepareData(DataFrame)
    XTrain, XTest, YTrain, YTest = train_test_split(X, Y, test_size=0.2, random_state=42)
    print("\nTraining Samples:", len(XTrain))
    print("Testing Samples:", len(XTest))

    # Step 3: Train Model
    Model = TrainModel(XTrain, YTrain)

    # Step 4: Test Data
    Predictions, Accuracy = TestModel(Model, XTest, YTest)

    # Step 5: Calculate Accuracy
    print("\nPredictions:", Predictions)
    print("\nAccuracy of Model is:", Accuracy * 100, "%")
    print("\nConfusion Matrix:\n", confusion_matrix(YTest, Predictions))
    print("\nClassification Report:\n", classification_report(YTest, Predictions))

    # Feature Importance
    Importance = pd.Series(Model.feature_importances_, index=DataFrame.columns[:-1])
    print("\nFeature Importance:\n", Importance.sort_values(ascending=False))

if __name__ == "__main__":
    Main()


