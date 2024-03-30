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


ANNUAL_TAX = 18.5
annual_tax_percent = ANNUAL_TAX/100

total_sales = float(input("Enter the total sales: $"))
tax = total_sales * annual_tax_percent

print("\nProjected Tax Report")
print(f'\nTotal sales: $ {total_sales:.2f}')
print(f'Annual tax:  % {ANNUAL_TAX}')
print(f'Tax:         $ {tax:.2f}')
