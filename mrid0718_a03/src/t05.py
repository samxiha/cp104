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


from functions import falling_distance


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


falling_time = int(input("Falling time: "))
if falling_time < 0:
    print("Invalid input. Falling time must be greater than or equal to 0.")
else:
    distance = falling_distance(falling_time)
    print(f'falling_distance({falling_time}) -> {distance}')
