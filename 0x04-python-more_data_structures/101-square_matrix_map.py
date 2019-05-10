#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda rows: list(map(lambda col: col ** 2, rows)),
                    matrix))
