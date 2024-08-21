import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    new_matrix = np.array(list).reshape(3, 3)

    calculations = {
        "mean": [new_matrix.mean(axis=0).tolist(), new_matrix.mean(axis=1).tolist(), new_matrix.mean().tolist()],
        "variance": [new_matrix.var(axis=0).tolist(), new_matrix.var(axis=1).tolist(), new_matrix.var().tolist()],
        "standard deviation": [new_matrix.std(axis=0).tolist(), new_matrix.std(axis=1).tolist(), new_matrix.std().tolist()],
        "max": [new_matrix.max(axis=0).tolist(), new_matrix.max(axis=1).tolist(), new_matrix.max().tolist()],
        "min": [new_matrix.min(axis=0).tolist(), new_matrix.min(axis=1).tolist(), new_matrix.min().tolist()],
        "sum": [new_matrix.sum(axis=0).tolist(), new_matrix.sum(axis=1).tolist(), new_matrix.sum().tolist()]
    }



    return calculations