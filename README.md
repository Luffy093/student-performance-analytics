# Student Performance Analytics System

## Project Overview

The Student Performance Analytics System is a simple Python project developed to analyze student marks and attendance data.

The project uses **Python, Pandas, and NumPy** to calculate student performance, assign grades, check pass/fail results, and identify top-performing students.

## Objective

The main objective of this project is to understand how Python can be used to read, process, and analyze student data.

The project helps to:

* Calculate total and average marks
* Assign grades to students
* Check pass/fail status
* Find the highest and lowest performers
* Analyze subject-wise performance
* Find the top-performing students
* Analyze student attendance

## Technologies Used

* Python
* Pandas
* NumPy

## Dataset

The project uses a CSV file named `students.csv`.

The dataset contains information such as:

* Student ID
* Student Name
* Department
* Python Marks
* Mathematics Marks
* Data Analysis Marks
* Computer Fundamentals Marks
* Communication Marks
* Attendance

The dataset contains 20 student records.

## Project Structure

```text
student-performance-analytics/
│
├── main.py
├── functions.py
├── students.csv
└── README.md
```

## Main Features

### 1. Student Data Analysis

The program reads student information from the CSV file using Pandas.

### 2. Total and Average Marks

The program calculates the total marks and average marks of each student.

### 3. Grade Calculation

Grades are assigned according to the student's average marks.

* 90 and above → A+
* 80–89 → A
* 70–79 → B
* 60–69 → C
* 50–59 → D
* Below 50 → F

### 4. Pass/Fail Result

A student is considered **Pass** if they score at least 40 marks in every subject.

### 5. Class Performance

The program finds:

* Class average
* Highest-performing student
* Lowest-performing student
* Number of students who passed
* Number of students who failed

### 6. Subject-wise Analysis

The program calculates the average marks for each subject and identifies the best and lowest-performing subjects.

### 7. Top 5 Students

The program sorts students according to their average marks and displays the top 5 performers.

### 8. Attendance Analysis

The program calculates the average attendance and identifies students whose attendance is below 75%.

## How to Run the Project

### Step 1: Install Required Libraries

Open the VS Code terminal and run:

```bash
python -m pip install pandas numpy
```

### Step 2: Run the Program

Make sure the terminal is inside the project folder and run:

```bash
python main.py
```

### Step 3: View the Output

The program displays the student performance analysis directly in the terminal.

## What I Learned

Through this project, I learned how to:

* Work with Python functions
* Use loops and conditions
* Read CSV files using Pandas
* Work with Pandas DataFrames
* Perform numerical calculations using NumPy
* Analyze and sort data
* Organize a Python project into multiple files

## Conclusion

The Student Performance Analytics System helped me understand the basic process of collecting, processing, and analyzing data using Python.

It also helped me practice Python fundamentals along with Pandas and NumPy in a practical project.
