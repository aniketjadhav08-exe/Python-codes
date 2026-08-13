import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def CreateDataFrame():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    DataFrame = pd.DataFrame(data)
    return DataFrame

def Q1_BasicInfo(DataFrame):
    print("----- Q1: Basic Information -----")
    print("\nShape:", DataFrame.shape)
    print("\nColumns:", DataFrame.columns.tolist())
    print("\nData Types:\n", DataFrame.dtypes)

def Q2_DescriptiveStats(DataFrame):
    print("\n----- Q2: Descriptive Statistics -----")
    print(DataFrame.describe())

def Q3_AddTotalColumn(DataFrame):
    print("\n----- Q3: Add Total Column -----")
    DataFrame['Total'] = DataFrame['Math'] + DataFrame['Science'] + DataFrame['English']
    print(DataFrame)
    return DataFrame

def Q4_ScienceAbove85(DataFrame):
    print("\n----- Q4: Students Scoring More Than 85 in Science -----")
    Result = DataFrame[DataFrame['Science'] > 85]
    print(Result)

def Q5_ReplaceName(DataFrame):
    print("\n----- Q5: Replace Pooja with Puja -----")
    DataFrame['Name'] = DataFrame['Name'].replace('Pooja', 'Puja')
    print(DataFrame)
    return DataFrame

def Q6_SortByTotal(DataFrame):
    print("\n----- Q6: Sort by Total (Descending) -----")
    SortedDataFrame = DataFrame.sort_values(by='Total', ascending=False)
    print(SortedDataFrame)
    return SortedDataFrame

def Q7_BarPlot(DataFrame):
    print("\n----- Q7: Bar Plot - Names vs Total Marks -----")
    plt.figure()
    plt.bar(DataFrame['Name'], DataFrame['Total'], color='skyblue')
    plt.xlabel('Student Name')
    plt.ylabel('Total Marks')
    plt.title('Student Names vs Total Marks')
    plt.savefig('BarPlot.png')
    print("Bar plot saved as BarPlot.png")

def Q8_LineChartAmit(DataFrame):
    print("\n----- Q8: Line Chart - Amit's Marks Across Subjects -----")
    AmitRow = DataFrame[DataFrame['Name'] == 'Amit']
    Subjects = ['Math', 'Science', 'English']
    Marks = AmitRow[Subjects].values.flatten()

    plt.figure()
    plt.plot(Subjects, Marks, marker='o', color='green')
    plt.xlabel('Subject')
    plt.ylabel('Marks')
    plt.title("Amit's Marks Across Subjects")
    plt.savefig('LineChart_Amit.png')
    print("Line chart saved as LineChart_Amit.png")

def Q9_FillMissingWithMean():
    print("\n----- Q9: Fill Missing Values with Column Mean -----")
    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }
    DataFrame2 = pd.DataFrame(data2)
    print("\nBefore Filling:\n", DataFrame2)

    DataFrame2['Math'] = DataFrame2['Math'].fillna(DataFrame2['Math'].mean())
    DataFrame2['Science'] = DataFrame2['Science'].fillna(DataFrame2['Science'].mean())

    print("\nAfter Filling:\n", DataFrame2)
    return DataFrame2

def Q10_DropEnglish(DataFrame):
    print("\n----- Q10: Drop English Column -----")
    DataFrame = DataFrame.drop('English', axis=1)
    print(DataFrame)
    return DataFrame

def Main():
    print("----- Student Marks Pandas Assignment -----")

    DataFrame = CreateDataFrame()

    Q1_BasicInfo(DataFrame)
    Q2_DescriptiveStats(DataFrame)
    DataFrame = Q3_AddTotalColumn(DataFrame)
    Q4_ScienceAbove85(DataFrame)
    DataFrame = Q5_ReplaceName(DataFrame)
    SortedDataFrame = Q6_SortByTotal(DataFrame)
    Q7_BarPlot(DataFrame)
    Q8_LineChartAmit(DataFrame)
    Q9_FillMissingWithMean()
    DataFrame = Q10_DropEnglish(DataFrame)

if __name__ == "__main__":
    Main()
