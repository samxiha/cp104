"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import customer_best


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


fh = open('customers.txt', 'r')
result = customer_best(fh)
print(f'Find customer with largest balance: {result}')
fh.close
