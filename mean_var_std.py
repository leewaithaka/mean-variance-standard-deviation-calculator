import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(numbers).reshape(3, 3)
    
    result = {
        'mean': [list(matrix.mean(axis=1)), list(matrix.mean(axis=0)), matrix.mean()],
        'variance': [list(matrix.var(axis=1)), list(matrix.var(axis=0)), matrix.var()],
        'standard deviation': [list(matrix.std(axis=1)), list(matrix.std(axis=0)), matrix.std()],
        'max': [list(matrix.max(axis=1)), list(matrix.max(axis=0)), matrix.max()],
        'min': [list(matrix.min(axis=1)), list(matrix.min(axis=0)), matrix.min()],
        'sum': [list(matrix.sum(axis=1)), list(matrix.sum(axis=0)), matrix.sum()]
    }
    
    return result
