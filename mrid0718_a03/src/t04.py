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


from functions import multiply_fractions


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


num1 = int(input("Numerator of first fraction: "))
den1 = int(input("Denominator of first fraction: "))
num2 = int(input("Numerator of second fraction: "))
den2 = int(input("Denominator of second fraction: "))

num, den, product = multiply_fractions(num1, den1, num2, den2)
print(f'multiply_fractions({num1},{den1},{num2},{den2}) -> ({num}, {den}, {product})')
