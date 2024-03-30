"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
import random
# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if value_type == "float":
                row.append(random.uniform(low, high))
            if value_type == "int":
                row.append(random.randint(low, high))
        matrix.append(row)

    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    print("    ", end="")
    for i in range(len(matrix[0])):
        print(f'{i:7}', end="")
    print()

    i = 0
    for row in matrix:
        print(f'{i:3}', end=" ")
        for value in row:
            if value_type == "float":
                print(f'{value:7.2f}', end="")
            elif value_type == "int":
                print(f'{value:7d}', end="")
        print()
        i += 1

    return


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0
    count = 0

    for row in matrix:
        for val in row:
            if val < smallest:
                smallest = val
            if val > largest:
                largest = val
            total += val
            count += 1

    average = total / count

    return smallest, largest, total, average


def count_frequency(matrix, char):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character char
    in matrix.
    Use: count = count_frequency(matrix, char)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        char - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of char in the matrix (int)
    -------------------------------------------------------
    """
    count = 0

    for row in matrix:
        for c in row:
            if c == char:
                count += 1

    return count


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    # Initialize the transposed matrix
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Transpose the matrix by swapping rows and columns
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
