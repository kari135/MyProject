import math


def fill_matrix_formula(rows, cols):
    """Заполнение матрицы по формуле sin(j + 2)."""
    matrix = []
    for i in range(rows):
        row = [math.sin(j + 2) for j in range(cols)]
        matrix.append(row)
    return matrix


def count_positive_rows(matrix):
    """Подсчёт строк, содержащих только положительные элементы."""
    return sum(1 for row in matrix if all(x > 0 for x in row))
