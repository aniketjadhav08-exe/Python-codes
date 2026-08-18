import numpy as np

def CalculateMean(Data):
    return np.mean(Data)

def Main():
    Dataset = [6, 7, 8, 9, 10, 11, 12]
    Mean = CalculateMean(Dataset)
    print("Mean of dataset is : ", Mean)

if __name__ == "__main__":
    Main()
