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


from functions import count_frequency


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


matrix = [['g', 'h', 'a', 'd'], ['o', 'g', 'n', 'd'], ['g', 'j', 't', 'c']]
char = 'g'
count = count_frequency(matrix, char)
print(f"({matrix},'{char}') -> {count}")
