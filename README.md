# Student Performance Analysis

A beginner-friendly Python project that analyzes student performance data using NumPy and visualizes insights using Matplotlib.

## Features

- Load student data from a CSV file
- Calculate subject-wise statistics
  - Average marks
  - Highest marks
  - Lowest marks
- Generate visualizations
  - Average marks by subject
  - Score distribution
  - Attendance vs Total Marks
- Generate a text report automatically

## Technologies Used

- Python
- NumPy
- Matplotlib

## Project Structure

```text
Student-Performance-Analysis/
│
├── data/
│   └── student_data.csv
│
├── image/
│   ├── subject_average.png
│   ├── score_distribution.png
│   └── attendance_vs_score.png
│
├── report/
│   └── report.txt
│
└── src/
    ├── data_loader.py
    ├── analysis.py
    ├── visualization.py
    ├── report_generator.py
    └── main.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Student-Performance-Analysis.git
```

Move into the project folder:

```bash
cd Student-Performance-Analysis
```

Install dependencies:

```bash
pip install numpy matplotlib
```

## Run the Project

Navigate to the source folder:

```bash
cd src
```

Run the program:

```bash
python main.py
```

## Output

### Statistics Report

The program calculates:

- Average marks
- Highest marks
- Lowest marks

### Generated Graphs

- Subject Average Chart
- Score Distribution Histogram
- Attendance vs Total Marks Scatter Plot

### Generated Report

A text report is automatically saved in:

```text
report/report.txt
```

## Sample Dataset

| Name | Math | Science | English | Attendance |
|------|------|---------|---------|------------|
| Harsh | 85 | 78 | 90 | 92 |
| Rahul | 75 | 82 | 80 | 88 |
| Priya | 92 | 89 | 95 | 96 |

## Learning Outcomes

This project demonstrates:

- Working with CSV files
- NumPy data analysis
- Statistical calculations
- Data visualization using Matplotlib
- Multi-file Python project structure
- Report generation

## Future Improvements

- Student ranking system
- Pass/Fail analysis
- Top performer detection
- More visualization charts
- Machine Learning based score prediction

## Author

Jeet Gondaliya
