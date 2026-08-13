import math

def EuclideanDistance(X1, Y1, X2, Y2):
    return math.sqrt((X1 - X2) ** 2 + (Y1 - Y2) ** 2)

def GetDataset():
    Dataset = [
        {"Point": "A", "X": 1, "Y": 2, "Label": "Red"},
        {"Point": "B", "X": 2, "Y": 3, "Label": "Red"},
        {"Point": "C", "X": 3, "Y": 1, "Label": "Blue"},
        {"Point": "D", "X": 6, "Y": 5, "Label": "Blue"}
    ]
    return Dataset

def CalculateDistances(Dataset, NewX, NewY):
    Distances = []
    for Row in Dataset:
        Dist = EuclideanDistance(NewX, NewY, Row["X"], Row["Y"])
        Distances.append({"Point": Row["Point"], "Distance": round(Dist, 2), "Label": Row["Label"]})
    return Distances

def SortDistances(Distances):
    return sorted(Distances, key=lambda Item: Item["Distance"])

def PredictForK(SortedDistances, K):
    Neighbors = SortedDistances[:K]
    Votes = {}
    for Neighbor in Neighbors:
        Label = Neighbor["Label"]
        Votes[Label] = Votes.get(Label, 0) + 1
    PredictedClass = max(Votes, key=Votes.get)
    return PredictedClass, Neighbors

def Main():
    print("----- KNN: Effect of K on Prediction -----")

    Dataset = GetDataset()

    NewX = int(input("Enter X coordinate: "))
    NewY = int(input("Enter Y coordinate: "))

    Distances = CalculateDistances(Dataset, NewX, NewY)
    SortedDistances = SortDistances(Distances)

    KValues = [1, 3, 5]

    print("\nPrediction Results")
    for K in KValues:
        if K > len(Dataset):
            print(f"K = {K} -> Not enough data points (only {len(Dataset)} available)")
            continue
        PredictedClass, Neighbors = PredictForK(SortedDistances, K)
        print(f"K = {K} -> {PredictedClass}")

if __name__ == "__main__":
    Main()