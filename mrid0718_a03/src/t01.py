"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import footage_to_acres


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


square_feet = float(input("Enter area in square feet: "))
if square_feet < 0:
    print("Invalid input. Square feet must be greater than or equal to 0.")
else:
    acres = footage_to_acres(square_feet)
    print(f'footage_to_acres({square_feet}) -> {acres}')
