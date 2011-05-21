#!/usr/bin/env python

"""If an element in an MxN matrix is 0, it's row and column are set to 0."""


def adjust_matrix(matrix):
    """
    Given a matrix of size MxN, if an element is zero, set it's row and
    column to zeros.
    """
    zero_rows = {}
    zero_columns = {}
    # Get location of all the zeros.
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num is 0:
                zero_rows[i] = True
                zero_columns[j] = True
    # Adjust the matrix accordingly.
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            # Dictionary lookup is O(1).
            if i in zero_rows or j in zero_columns:
                matrix[i][j] = 0
    return matrix


def main():
    matrix = [[1],[2],[3]]
    print adjust_matrix(matrix)

    matrix = [[1, 2], [1, 0]]
    print adjust_matrix(matrix)

    matrix = [[1, 2, 3], [1, 2, 0], [1, 2, 3]]
    print adjust_matrix(matrix)

    matrix = [[1, 2, 3, 4], [1, 2, 3, 4],
              [1, 2, 0, 4], [1, 2, 3, 4]]
    print adjust_matrix(matrix)

if __name__ == '__main__':
    main()
