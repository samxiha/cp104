"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-11-16"
-------------------------------------------------------
"""
# Imports

# Constants


from functions import text_analyze


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


txt = input("Enter text: ")
uppr, lowr, dgts, whtspc = text_analyze(txt)
print(f'{uppr}, {lowr}, {dgts}, {whtspc}')
