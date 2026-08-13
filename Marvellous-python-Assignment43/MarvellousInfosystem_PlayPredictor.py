import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def GetData(Path):
    DataFrame = pd.read_csv(Path)
    DataFrame = DataFrame.loc[:, ~DataFrame.columns.str.contains('^Unnamed')]
    return DataFrame

def PrepareData(DataFrame):
    WetherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    DataFrame['Wether'] = WetherEncoder.fit_transform(DataFrame['Wether'])
    DataFrame['Temperature'] = TemperatureEncoder.fit_transform(DataFrame['Temperature'])
    DataFrame['Play'] = PlayEncoder.fit_transform(DataFrame['Play'])

    X = DataFrame[['Wether', 'Temperature']]
    Y = DataFrame['Play']

    return X, Y, WetherEncoder, TemperatureEncoder, PlayEncoder

def TrainModel(X, Y, K=3):
    Model = KNeighborsClassifier(n_neighbors=K)
    Model.fit(X, Y)
    return Model

def TestModel(Model, WetherEncoder, TemperatureEncoder, PlayEncoder, WetherValue, TemperatureValue):
    WetherEncoded = WetherEncoder.transform([WetherValue])
    TemperatureEncoded = TemperatureEncoder.transform([TemperatureValue])

    TestData = pd.DataFrame([[WetherEncoded[0], TemperatureEncoded[0]]], columns=['Wether', 'Temperature'])
    Prediction = Model.predict(TestData)

    ResultLabel = PlayEncoder.inverse_transform(Prediction)
    return ResultLabel[0]

def CheckAccuracy(X, Y, K=3):
    XTrain, XTest, YTrain, YTest = train_test_split(X, Y, test_size=0.5, random_state=42)

    Model = KNeighborsClassifier(n_neighbors=K)
    Model.fit(XTrain, YTrain)

    Predictions = Model.predict(XTest)
    Accuracy = accuracy_score(YTest, Predictions)

    return Accuracy

def Main():
    print("----- Marvellous Infosystems Play Predictor -----")

    # Step 1: Get Data
    Path = "MarvellousInfosystems_PlayPredictor.csv"
    DataFrame = GetData(Path)
    print("\nDataset Shape:", DataFrame.shape)
    print("\nDataset:\n", DataFrame)

    # Step 2: Clean, Prepare and Manipulate data
    X, Y, WetherEncoder, TemperatureEncoder, PlayEncoder = PrepareData(DataFrame)
    print("\nEncoded Features:\n", X)
    print("\nEncoded Labels:\n", Y.tolist())

    # Step 3: Train Data
    Model = TrainModel(X, Y, K=3)

    # Step 4: Test Data
    WetherValue = "Sunny"
    TemperatureValue = "Cool"
    Result = TestModel(Model, WetherEncoder, TemperatureEncoder, PlayEncoder, WetherValue, TemperatureValue)
    print(f"\nFor Wether = {WetherValue}, Temperature = {TemperatureValue}")
    print("Predicted Result of Play:", Result)

    # Step 5: Calculate Accuracy
    print("\n----- Accuracy for Different K values -----")
    for K in [1, 3, 5]:
        Accuracy = CheckAccuracy(X, Y, K)
        print(f"K = {K} -> Accuracy: {Accuracy * 100:.2f} %")

if __name__ == "__main__":
    Main()
