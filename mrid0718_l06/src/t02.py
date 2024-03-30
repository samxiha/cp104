"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-10-24"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import sum_odd


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


num = int(input("Enter a number: "))
if num < 0:
    print("Number must be greater than 0")
else:
    total = sum_odd(num)
    print(f'{total}')
