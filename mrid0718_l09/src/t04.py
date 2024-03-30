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


from functions import validate_code


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


product_code = input("Enter code: ")
category, digits, qualifiers = validate_code(product_code)
print(f'{category}, {digits}, {qualifiers}')
