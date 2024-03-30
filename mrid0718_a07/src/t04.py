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


from functions import list_subtract
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


minuend = list_positives()
print(minuend)
subtrahend = list_positives()
print(subtrahend)
list_subtract(minuend, subtrahend)
print(f'minuend after: {minuend}')
