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


num_flyers = int(input("Number of flyers: "))
num_volunteers = int(input("Number of volunteers: "))

per_volunteer = num_flyers//num_volunteers
print("Flyers per volunteer: ", per_volunteer)

left_over = num_flyers % num_volunteers
print("Flyers left over: ", left_over)
