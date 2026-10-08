import pandas as pd
import numpy as np

from functions import calculate_total, calculate_average
from functions import assign_grade, check_result 

# Load the student dataset
df = pd.read_csv("students.csv")

# Display basic information
print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 45)

print("\nStudent Records:")
print(df)

print("\nNumber of students:", len(df))
print("\nColumns in dataset:")
print(df.columns.tolist())

# Subject columns
subject_columns = [
    "Python",
    "Mathematics",
    "Data_Analysis",
    "Computer_Fundamentals",
    "Communication"
]

# Calculate total, average, grade and result for each student
totals = []
averages = []
grades = []
results = []

for index, row in df.iterrows():

    marks = row[subject_columns].tolist()

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = assign_grade(average)
    result = check_result(marks)

    totals.append(total)
    averages.append(average)
    grades.append(grade)
    results.append(result)

# Add calculated values to the DataFrame
df["Total_Marks"] = totals
df["Average_Marks"] = np.round(averages, 2)
df["Grade"] = grades
df["Result"] = results

print("\nStudent Performance Analysis:")
print("=" * 45)

print(df[
    ["Student_ID", "Name", "Total_Marks",
     "Average_Marks", "Grade", "Result"]
].to_string(index=False))

# Overall class performance
class_average = np.mean(df["Average_Marks"])

highest_student = df.loc[df["Average_Marks"].idxmax()]
lowest_student = df.loc[df["Average_Marks"].idxmin()]

print("\nOverall Class Analysis:")
print("=" * 45)

print(f"Class Average: {class_average:.2f}")

print(
    f"Highest Performer: {highest_student['Name']} "
    f"({highest_student['Average_Marks']:.2f})"
)

print(
    f"Lowest Performer: {lowest_student['Name']} "
    f"({lowest_student['Average_Marks']:.2f})"
)

# Pass and fail statistics
pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("\nPass/Fail Statistics:")
print("=" * 45)
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)

# Subject-wise average performance
subject_averages = df[subject_columns].mean()

best_subject = subject_averages.idxmax()
best_subject_average = subject_averages.max()

lowest_subject = subject_averages.idxmin()
lowest_subject_average = subject_averages.min()

print("\nSubject-wise Performance:")
print("=" * 45)

for subject, average in subject_averages.items():
    print(f"{subject}: {average:.2f}")

print(f"\nBest Performing Subject: {best_subject}")
print(f"Average Marks: {best_subject_average:.2f}")

print(f"\nLowest Performing Subject: {lowest_subject}")
print(f"Average Marks: {lowest_subject_average:.2f}")

# Top-performing students
top_students = df.sort_values(
    by="Average_Marks",
    ascending=False
).head(5)

print("\nTop 5 Performing Students:")
print("=" * 45)

print(
    top_students[
        ["Student_ID", "Name", "Department", "Average_Marks", "Grade"]
    ].to_string(index=False)
)

# Attendance analysis
average_attendance = np.mean(df["Attendance"])
low_attendance_students = df[df["Attendance"] < 75]

print("\nAttendance Analysis:")
print("=" * 45)

print(f"Average Attendance: {average_attendance:.2f}%")
print(f"Students with attendance below 75%: {len(low_attendance_students)}")

if len(low_attendance_students) > 0:
    print("\nStudents with low attendance:")
    print(
        low_attendance_students[
            ["Student_ID", "Name", "Attendance"]
        ].to_string(index=False)
    )
else:
    print("No students have attendance below 75%.")

