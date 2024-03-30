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

# Constants


from functions import matrix_stats


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


matrix = [[5, 0, -4, 1], [9, 3, -5, 7], [-6, 3, 6, 0]]
smallest, largest, total, average = matrix_stats(matrix)
print(f'({smallest}, {largest}, {total}, {average})')
