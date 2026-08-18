import numpy as np

def CalculateVariance(Data):
    return np.var(Data)

def CalculateStdDev(Data):
    return np.std(Data)

def Main():
    Dataset = [6, 7, 8, 9, 10, 11, 12]
    Variance = CalculateVariance(Dataset)
    StdDev = CalculateStdDev(Dataset)
    print("Variance of dataset is : ", Variance)
    print("Standard Deviation of dataset is : ", StdDev)

if __name__ == "__main__":
    Main()