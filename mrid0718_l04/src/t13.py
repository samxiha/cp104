"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import f_to_c


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


FARENHEIT_FREEZING = 32

fahrenheit = int(input("Temperature (F): "))

result = f_to_c(fahrenheit)
print(f"{result}")
