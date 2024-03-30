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


from functions import detect_prime


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
prime = detect_prime(number)
print(f'{prime}')
