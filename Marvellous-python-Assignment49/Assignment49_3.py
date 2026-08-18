import numpy as np
from sklearn.preprocessing import StandardScaler

def ScaleData(Data):
    Scaler = StandardScaler()
    ScaledData = Scaler.fit_transform(Data)
    return ScaledData

def Main():
    Dataset = np.array([[25, 20000], [30, 40000], [35, 80000]])
    ScaledDataset = ScaleData(Dataset)
    print("Original dataset :\n", Dataset)
    print("Scaled dataset :\n", ScaledDataset)

if __name__ == "__main__":
    Main()