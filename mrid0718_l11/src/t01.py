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


from functions import generate_matrix_num


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


value_type = input("Enter value type (float/int): ")
rows = int(input("Rows: "))
cols = int(input("Columns: "))
low = float(input("Low: "))
high = float(input("High: "))
matrix = generate_matrix_num(rows, cols, low, high, value_type)
for row in matrix:
    print(row)
