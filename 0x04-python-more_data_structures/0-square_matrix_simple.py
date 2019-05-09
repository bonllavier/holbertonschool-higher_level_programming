#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_tmp = []
    for iter in range(len(matrix)):
        new = []
        for iter2 in range(len(matrix[0])):
            new.append(matrix[iter][iter2] ** 2)
        matrix_tmp.append(new)
    return matrix_tmp
