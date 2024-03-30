"""
-------------------------------------------------------
Exam Task 5 Function Definitions
-------------------------------------------------------
Author: Samiha Mridha
ID:     169060718
Email:  mrid0718@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def fill_matrix(fh_in, rows, cols):
    """
    -------------------------------------------------------
    Creates a rows by cols 2D list of integers filled with
    space-separated integers from f_in. If f_in does not have enough values,
    fill the remaining slots with 0s. If f_in has too many values,
    the excess values are ignored.
    Use: matrix = fill_matrix(fh_in, rows, cols)
    -------------------------------------------------------
    Parameters:
        fh_in - the integers file to process (file handle - already open for reading)
        rows - rows in matrix (int > 0)
        cols - columns in matrix (int > 0)
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌​​‌​‌‌​‌‌‌​:
        matrix - a 2D list of integers (2D list of int)
    -------------------------------------------------------
    """
    matrix = []

    for i in range(rows):
        line = fh_in.readline()
        values = [int(num) for num in line.split()]
        matrix.append(values[:cols])

    return matrix
