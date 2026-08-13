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
    DataFrame['Total'] = DataFrame['Math'] + DataFrame['Science'] + DataFrame['English']
    return DataFrame

def Q1_NormalizeMath(DataFrame):
    print("----- Q1: Normalize Math Scores (Min-Max Scaling) -----")
    MinValue = DataFrame['Math'].min()
    MaxValue = DataFrame['Math'].max()
    DataFrame['Math_Normalized'] = (DataFrame['Math'] - MinValue) / (MaxValue - MinValue)
    print(DataFrame[['Name', 'Math', 'Math_Normalized']])
    return DataFrame

def Q2_GenderOneHotEncoding(DataFrame):
    print("\n----- Q2: Gender Column with One-Hot Encoding -----")
    DataFrame['Gender'] = ['Male', 'Male', 'Female']
    print("\nWith Gender Column:\n", DataFrame[['Name', 'Gender']])

    OneHotEncoded = pd.get_dummies(DataFrame, columns=['Gender'])
    print("\nAfter One-Hot Encoding:\n", OneHotEncoded)
    return DataFrame, OneHotEncoded

def Q3_GroupByGender(DataFrame):
    print("\n----- Q3: Average Marks Grouped by Gender -----")
    GroupedData = DataFrame.groupby('Gender')[['Math', 'Science', 'English', 'Total']].mean()
    print(GroupedData)
    return GroupedData

def Q4_PieChartSagar(DataFrame):
    print("\n----- Q4: Pie Chart of Subject Marks for Sagar -----")
    SagarRow = DataFrame[DataFrame['Name'] == 'Sagar']
    Subjects = ['Math', 'Science', 'English']
    Marks = SagarRow[Subjects].values.flatten()

    plt.figure()
    plt.pie(Marks, labels=Subjects, autopct='%1.1f%%', startangle=90)
    plt.title("Sagar's Subject-wise Marks")
    plt.savefig('PieChart_Sagar.png')
    print("Pie chart saved as PieChart_Sagar.png")

def Q5_AddStatusColumn(DataFrame):
    print("\n----- Q5: Add Status Column (Pass/Fail) -----")
    DataFrame['Status'] = np.where(DataFrame['Total'] >= 250, 'Pass', 'Fail')
    print(DataFrame[['Name', 'Total', 'Status']])
    return DataFrame

def Q6_CountPassed(DataFrame):
    print("\n----- Q6: Count of Students Who Passed -----")
    PassCount = (DataFrame['Status'] == 'Pass').sum()
    print("Number of students passed:", PassCount)
    return PassCount

def Q7_ExportToCSV(DataFrame):
    print("\n----- Q7: Export Final DataFrame to CSV -----")
    DataFrame.to_csv('FinalStudentData.csv', index=False)
    print("Exported to FinalStudentData.csv")

def Q8_HistogramMath(DataFrame):
    print("\n----- Q8: Histogram of Math Marks -----")
    plt.figure()
    plt.hist(DataFrame['Math'], bins=5, color='orange', edgecolor='black')
    plt.xlabel('Math Marks')
    plt.ylabel('Frequency')
    plt.title('Histogram of Math Marks')
    plt.savefig('Histogram_Math.png')
    print("Histogram saved as Histogram_Math.png")

def Q9_RenameMathColumn(DataFrame):
    print("\n----- Q9: Rename Math Column to Mathematics -----")
    DataFrame = DataFrame.rename(columns={'Math': 'Mathematics'})
    print(DataFrame.columns.tolist())
    return DataFrame

def Q10_BoxplotEnglish(DataFrame):
    print("\n----- Q10: Boxplot for English Marks -----")
    plt.figure()
    plt.boxplot(DataFrame['English'])
    plt.ylabel('English Marks')
    plt.title('Boxplot of English Marks')
    plt.savefig('Boxplot_English.png')
    print("Boxplot saved as Boxplot_English.png")

def Main():
    print("----- Student Marks Advanced Pandas Assignment -----")

    DataFrame = CreateDataFrame()
    print("\nOriginal Dataset:\n", DataFrame)

    DataFrame = Q1_NormalizeMath(DataFrame)
    DataFrame, OneHotEncoded = Q2_GenderOneHotEncoding(DataFrame)
    Q3_GroupByGender(DataFrame)
    Q4_PieChartSagar(DataFrame)
    DataFrame = Q5_AddStatusColumn(DataFrame)
    Q6_CountPassed(DataFrame)
    Q7_ExportToCSV(DataFrame)
    Q8_HistogramMath(DataFrame)
    DataFrame = Q9_RenameMathColumn(DataFrame)
    Q10_BoxplotEnglish(DataFrame)

    print("\nFinal DataFrame:\n", DataFrame)

if __name__ == "__main__":
    Main()
