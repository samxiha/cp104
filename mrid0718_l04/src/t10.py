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


from functions import population


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


size = int(input("What is the population size: "))
births = int(input("How many births: "))
deaths = int(input("How many deaths: "))
immigrants = int(input("How many immigrants: "))
years = int(input("How many years: "))

result = population(size, births, deaths, immigrants, years)
print(f'The future population size is: {result}')
