"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import pollution_ranking


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


air_quality_index = int(input("Enter AQI: "))
pollution = pollution_ranking(air_quality_index)
print(f'{pollution}')
