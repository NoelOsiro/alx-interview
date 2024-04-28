#!/usr/bin/python3
""" A module that rotates 2d matrix """


def rotate_2d_matrix(matrix):
    """ A function that rotates matrix clock wise 90 degree"""
    n = len(matrix)
    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row in the transposed matrix
    for row in matrix:
        row.reverse()
