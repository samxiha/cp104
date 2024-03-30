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


from functions import file_top


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


count = int(input("Count: "))
file_handle = open("students.txt", "r", encoding="utf-8")
file_top(file_handle, count)
file_handle.close()
