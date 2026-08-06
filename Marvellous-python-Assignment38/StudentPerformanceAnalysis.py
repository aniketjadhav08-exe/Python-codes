import pandas as pd
import matplotlib.pyplot as plt

def LoadAndExplore(FilePath):
    Df = pd.read_csv(FilePath)

    print("First 5 records:")
    print(Df.head())
    print("\nLast 5 records:")
    print(Df.tail())
    print("\nTotal rows and columns:", Df.shape)
    print("\nColumn names:", list(Df.columns))
    print("\nData types:\n", Df.dtypes)

    return Df

def PassFailCounts(Df):
    Total = len(Df)
    Passed = (Df['FinalResult'] == 1).sum()
    Failed = (Df['FinalResult'] == 0).sum()

    print("\nTotal number of students:", Total)
    print("Students Passed:", Passed)
    print("Students Failed:", Failed)

    return Total, Passed, Failed

def BasicStatistics(Df):
    AvgStudyHours = Df['StudyHours'].mean()
    AvgAttendance = Df['Attendance'].mean()
    MaxPreviousScore = Df['PreviousScore'].max()
    MinSleepHours = Df['SleepHours'].min()

    print("\nAverage StudyHours:", round(AvgStudyHours, 2))
    print("Average Attendance:", round(AvgAttendance, 2))
    print("Maximum PreviousScore:", MaxPreviousScore)
    print("Minimum SleepHours:", MinSleepHours)

def ResultDistribution(Df):
    Counts = Df['FinalResult'].value_counts()
    PassPct = (Counts.get(1, 0) / len(Df)) * 100
    FailPct = (Counts.get(0, 0) / len(Df)) * 100

    print("\nFinalResult value counts:\n", Counts)
    print(f"Pass percentage: {PassPct:.2f}%")
    print(f"Fail percentage: {FailPct:.2f}%")

    if abs(PassPct - FailPct) <= 10:
        print("The dataset is fairly balanced (difference <= 10%).")
    else:
        print("The dataset is imbalanced - Pass and Fail counts differ significantly.")

def StudyAttendanceObservations(Df):
    CorrStudy = Df['StudyHours'].corr(Df['FinalResult'])
    CorrAttendance = Df['Attendance'].corr(Df['FinalResult'])

    print("\nCorrelation of StudyHours with FinalResult:", round(CorrStudy, 2))
    print("Correlation of Attendance with FinalResult:", round(CorrAttendance, 2))
    print("""
Observations:
1. StudyHours shows a strong positive correlation with FinalResult, meaning
   students who study more hours per day are considerably more likely to pass.
2. Attendance also shows a strong positive correlation with FinalResult,
   indicating regular class attendance improves the chance of passing.
3. Students with low StudyHours and low Attendance together tend to fail,
   suggesting these two factors may be reinforcing each other.
4. Neither factor alone guarantees a pass/fail outcome, but both are strong
   individual predictors based on this dataset.
5. This supports focusing on both consistent study habits and attendance
   for improving student outcomes.
""")

def PlotStudyHoursHistogram(Df, OutputPath):
    plt.figure(figsize=(7, 5))
    plt.hist(Df['StudyHours'], bins=8, color='steelblue', edgecolor='black')
    plt.title('Distribution of Study Hours')
    plt.xlabel('Study Hours per Day')
    plt.ylabel('Number of Students')
    plt.tight_layout()
    plt.savefig(OutputPath)
    plt.close()
    print(f"\nHistogram saved to {OutputPath}")
    print("The distribution shows most students study between 3-8 hours per day, "
          "roughly spread across a moderate range with no extreme outliers.")

def PlotStudyVsPreviousScore(Df, OutputPath):
    plt.figure(figsize=(7, 5))
    plt.scatter(Df['StudyHours'], Df['PreviousScore'], color='darkorange', edgecolor='black')
    plt.title('StudyHours vs PreviousScore')
    plt.xlabel('Study Hours per Day')
    plt.ylabel('Previous Exam Score')
    plt.tight_layout()
    plt.savefig(OutputPath)
    plt.close()
    print(f"Scatter plot saved to {OutputPath}")

def PlotAttendanceBoxplot(Df, OutputPath):
    plt.figure(figsize=(5, 6))
    plt.boxplot(Df['Attendance'], vert=True)
    plt.title('Boxplot of Attendance')
    plt.ylabel('Attendance (%)')
    plt.tight_layout()
    plt.savefig(OutputPath)
    plt.close()

    Q1 = Df['Attendance'].quantile(0.25)
    Q3 = Df['Attendance'].quantile(0.75)
    IQR = Q3 - Q1
    Lower = Q1 - 1.5 * IQR
    Upper = Q3 + 1.5 * IQR
    Outliers = Df[(Df['Attendance'] < Lower) | (Df['Attendance'] > Upper)]

    print(f"\nBoxplot saved to {OutputPath}")
    if len(Outliers) == 0:
        print("No outliers detected in Attendance.")
    else:
        print(f"{len(Outliers)} outlier(s) detected in Attendance:\n", Outliers)

def PlotAssignmentsVsResult(Df, OutputPath):
    Colors = Df['FinalResult'].map({1: 'green', 0: 'red'})
    plt.figure(figsize=(7, 5))
    plt.scatter(Df['AssignmentsCompleted'], Df['FinalResult'], c=Colors, edgecolor='black')
    plt.title('AssignmentsCompleted vs FinalResult')
    plt.xlabel('Assignments Completed')
    plt.ylabel('Final Result (0=Fail, 1=Pass)')
    plt.yticks([0, 1])
    plt.tight_layout()
    plt.savefig(OutputPath)
    plt.close()
    print(f"\nPlot saved to {OutputPath}")
    print("Observation: Students who completed more assignments are heavily "
          "concentrated in the Pass category, while those completing fewer "
          "assignments mostly fall in the Fail category.")

def PlotSleepVsResult(Df, OutputPath):
    Colors = Df['FinalResult'].map({1: 'green', 0: 'red'})
    plt.figure(figsize=(7, 5))
    plt.scatter(Df['SleepHours'], Df['FinalResult'], c=Colors, edgecolor='black')
    plt.title('SleepHours vs FinalResult')
    plt.xlabel('Sleep Hours per Day')
    plt.ylabel('Final Result (0=Fail, 1=Pass)')
    plt.yticks([0, 1])
    plt.tight_layout()
    plt.savefig(OutputPath)
    plt.close()
    print(f"\nPlot saved to {OutputPath}")
    print("Observation: Passing students tend to have moderately higher sleep "
          "hours on average, but sleep alone does not guarantee success - some "
          "students with decent sleep still failed, showing StudyHours and "
          "Attendance are stronger predictors than SleepHours by itself.")

def Main():
    FilePath = 'student_performance_ml.csv'
    Df = LoadAndExplore(FilePath)
    PassFailCounts(Df)
    BasicStatistics(Df)
    ResultDistribution(Df)
    StudyAttendanceObservations(Df)

    PlotStudyHoursHistogram(Df, 'StudyHours_Histogram.png')
    PlotStudyVsPreviousScore(Df, 'StudyHours_vs_PreviousScore.png')
    PlotAttendanceBoxplot(Df, 'Attendance_Boxplot.png')
    PlotAssignmentsVsResult(Df, 'Assignments_vs_FinalResult.png')
    PlotSleepVsResult(Df, 'SleepHours_vs_FinalResult.png')

if __name__ == "__main__":
    Main()
