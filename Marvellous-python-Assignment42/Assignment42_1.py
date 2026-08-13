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

def SelectKNearest(SortedDistances, K):
    return SortedDistances[:K]

def PredictClass(Neighbors):
    Votes = {}
    for Neighbor in Neighbors:
        Label = Neighbor["Label"]
        Votes[Label] = Votes.get(Label, 0) + 1

    PredictedClass = max(Votes, key=Votes.get)
    return PredictedClass

def Main():
    print("----- KNN Classifier (Manual Implementation) -----")

    Dataset = GetDataset()

    NewX = int(input("Enter X coordinate: "))
    NewY = int(input("Enter Y coordinate: "))

    K = 3

    Distances = CalculateDistances(Dataset, NewX, NewY)
    SortedDistances = SortDistances(Distances)
    Neighbors = SelectKNearest(SortedDistances, K)

    print("\nNearest Neighbors:")
    for Neighbor in Neighbors:
        print(Neighbor["Point"], "- Distance:", Neighbor["Distance"])

    PredictedClass = PredictClass(Neighbors)
    print("\nPredicted Class:", PredictedClass)

if __name__ == "__main__":
    Main()
