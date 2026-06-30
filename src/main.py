from data_loader import load_data
from analysis import calculate_statistics
from visualization import (
    plot_subject_average,
    plot_score_distribution,
    plot_attendance_vs_score
)
from report_generator import save_report

# Load data
data = load_data("../data/student_data.csv")

# Calculate statistics
stats = calculate_statistics(data)

# Print report on terminal
print("\n===== STUDENT PERFORMANCE REPORT =====\n")

for key, value in stats.items():
    print(f"{key}: {value:.2f}")

# Save report to report/report.txt
save_report(stats)

# Generate graphs
plot_subject_average(data)
plot_score_distribution(data)
plot_attendance_vs_score(data)

print("\nReport saved in report folder.")
print("Graphs saved successfully in image folder.")