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


from functions import factor_summation


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
if number >= 1:
    total = factor_summation(number)
    print(f"{total}")
else:
    print("Enter a number greater than or equal to 1")
