"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import count_of_digits


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


number = int(input("Enter a number: "))
digits = count_of_digits(number)
print(f'{digits}')
