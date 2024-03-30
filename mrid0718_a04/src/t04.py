"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import colour_combine


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


rgb_colour1 = input("First primary colour: ")
rgb_colour2 = input("Second primary colour: ")
rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
print(f'{rgb_colour}')
