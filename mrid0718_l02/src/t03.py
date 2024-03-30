"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports

# Constants


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


LARGE_COST = 75
SMALL_COST = 50
Large_dogs = int(input("Number of large dogs groomed: "))
Small_dogs = int(input("Number of small dogs groomed: "))

Total_earned = (Large_dogs * LARGE_COST) + (Small_dogs * SMALL_COST)
print("Total earned for the day: $", Total_earned)
