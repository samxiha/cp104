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


from functions import file_copy


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


fh_1 = open('words.txt', 'r')
fh_2 = open('new_words.txt', 'w')
print(f"Copying 'words.txt' to 'new_words.txt'")
file_copy(fh_1, fh_2)
