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


from functions import matrix_transpose


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


matrix = [[6, 4, 24, 77], [1, -9, 8, 6, 8]]
transposed = matrix_transpose(matrix)
print(f'{matrix} -> {transposed}')
