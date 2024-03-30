"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import append_max_num


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


fh = open('numbers.txt', 'r+')
num = append_max_num(fh)
print(f"file 'numbers.txt' open for reading and writing.\n{num} is appended")
fh.close
