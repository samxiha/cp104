"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samiha Mridha
ID: 169060718
Email:   mrid0718@mylaurier.ca
__updated__ = "2023-09-28"
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


P = float(input("Principal: $"))
r = float(input("Interest(%): "))
t = int(input("Number of years: "))
n = int(input("Number of times interest compounded per year: "))

interest = r/100
A = P * (1 + (interest/n))**(n*t)

print(f'Balance: $ {A}')
