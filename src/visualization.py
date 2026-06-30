import matplotlib.pyplot as plt
import numpy as np

def plot_subject_average(data):

    averages = [
        np.mean(data['Math']),
        np.mean(data['Science']),
        np.mean(data['English'])
    ]

    subjects = ['Math', 'Science', 'English']

    plt.figure(figsize=(8,5))
    plt.bar(subjects, averages)
    plt.title("Average Marks by Subject")
    plt.ylabel("Marks")

    plt.savefig("../image/subject_average.png")
    plt.close()


def plot_score_distribution(data):

    total_marks = (
        data['Math']
        + data['Science']
        + data['English']
    )

    plt.figure(figsize=(8,5))
    plt.hist(total_marks, bins=5)

    plt.title("Total Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Students")

    plt.savefig("../image/score_distribution.png")
    plt.close()


def plot_attendance_vs_score(data):

    attendance = data['Attendance']

    total_marks = (
        data['Math']
        + data['Science']
        + data['English']
    )

    plt.figure(figsize=(8,5))
    plt.scatter(attendance, total_marks)

    plt.title("Attendance vs Total Marks")
    plt.xlabel("Attendance %")
    plt.ylabel("Total Marks")

    plt.savefig("../image/attendance_vs_score.png")
    plt.close()