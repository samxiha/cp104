"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import calories_treadmill


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


per_min = float(input("Calories burned per minute: "))
minutes = int(input("Total minutes run: "))
calories_burned = calories_treadmill(per_min, minutes)
