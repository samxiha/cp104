"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import line_numbering


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


read_file = open('wilde.txt', 'r')
write_file = open('wilde_numbered.txt', 'w')

line_numbering(read_file, write_file)
