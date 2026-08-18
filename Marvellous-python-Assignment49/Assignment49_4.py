import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance

def CalculateDistance(PointA, PointB):
    return distance.euclidean(PointA, PointB)

def Main():
    Dataset = np.array([[25, 20000], [30, 40000], [35, 80000]])

    PointA = Dataset[0]
    PointB = Dataset[1]
    DistanceBefore = CalculateDistance(PointA, PointB)

    Scaler = StandardScaler()
    ScaledDataset = Scaler.fit_transform(Dataset)
    DistanceAfter = CalculateDistance(ScaledDataset[0], ScaledDataset[1])

    print("Euclidean distance before scaling : ", DistanceBefore)
    print("Euclidean distance after scaling : ", DistanceAfter)

if __name__ == "__main__":
    Main()