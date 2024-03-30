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


from functions import read_integers


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


file_handle = open("numbers.txt", "r", encoding="utf-8")
number_list = read_integers(file_handle)
print(number_list)
