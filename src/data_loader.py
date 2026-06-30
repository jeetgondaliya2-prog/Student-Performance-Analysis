import numpy as np

def load_data(file_path):
    data = np.genfromtxt(
        file_path,
        delimiter=',',
        names=True,
        dtype=None,
        encoding='utf-8'
    )
    return data