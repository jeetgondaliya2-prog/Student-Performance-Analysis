def save_report(stats, filename="../report/report.txt"):

    with open(filename, "w") as file:

        file.write("===== STUDENT PERFORMANCE REPORT =====\n\n")

        for key, value in stats.items():
            file.write(f"{key}: {value:.2f}\n")

    print("Report generated successfully!")