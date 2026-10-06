def read_matrix(rows, cols):
    """Чтение матрицы с клавиатуры."""
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Строка {i+1}: ").split()))
        matrix.append(row)
    return matrix


def transpose(matrix):
    """Транспонирование матрицы."""
    return [list(row) for row in zip(*matrix)]


def print_matrix(matrix):
    """Вывод матрицы на экран."""
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    rows = int(input("Количество строк: "))
    cols = int(input("Количество столбцов: "))
    m = read_matrix(rows, cols)
    print("Исходная матрица:")
    print_matrix(m)
    print("Транспонированная матрица:")
    print_matrix(transpose(m))


