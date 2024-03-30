"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-16"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import is_hydroxide


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


chemical = input("Chemical name: ")
hydroxide = is_hydroxide(chemical)
print(f'{hydroxide}')
