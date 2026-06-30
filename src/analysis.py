import numpy as np

def calculate_statistics(data):

    math = data['Math']
    science = data['Science']
    english = data['English']

    stats = {
        "Math Average": np.mean(math),
        "Science Average": np.mean(science),
        "English Average": np.mean(english),

        "Math Highest": np.max(math),
        "Science Highest": np.max(science),
        "English Highest": np.max(english),

        "Math Lowest": np.min(math),
        "Science Lowest": np.min(science),
        "English Lowest": np.min(english)
    }

    return stats