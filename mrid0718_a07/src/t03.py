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


from functions import get_indexes

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
target_number = int(input("Enter target number: "))
index_list = get_indexes(numbers, target_number)
print(f'{index_list}')
