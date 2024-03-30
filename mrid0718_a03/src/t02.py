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


from functions import lawn_mow_time


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


width = float(input("Enter width: "))
length = float(input("Enter length: "))
speed = float(input("Enter speed: "))

if width <= 0 or length <= 0 or speed <= 0:
    print("Invalid input. Width, length, and speed must be greater than 0.")
else:
    time = lawn_mow_time(width, length, speed)
    print(f'lawn_mow_time({width},{length},{speed}) -> {time}')
