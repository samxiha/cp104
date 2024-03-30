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


flyers = int(input("Number of flyers: "))
num_people = int(input("Number of delivery people: "))

per_person = flyers//num_people
left_over = flyers % num_people

print(f"\nFlyers per delivery person: {per_person}")
print(f"Flyers left over: {left_over}")
