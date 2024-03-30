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


from functions import file_statistics


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


file_handle = open("addresses.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
print(f'{ucount}, {lcount}, {dcount}, {wcount}, {rcount}')
file_handle.close
