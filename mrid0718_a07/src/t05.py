"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import verify_sorted
from functions import list_positives


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


numbers = list_positives()
print(numbers)
in_order, index = verify_sorted(numbers)
print(f'{in_order},{index}')
