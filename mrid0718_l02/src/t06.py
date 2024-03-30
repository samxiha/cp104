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


principal = float(input("Mortgage principal ($): "))
years = int(input("Number of years: "))
interest = float(input("Yearly interest rate (%): "))

num_months = years * 12
monthly_interest = interest/1200

numerator = monthly_interest * ((1 + monthly_interest) ** num_months)
denominator = (1 + monthly_interest) ** num_months - 1

monthly_payments = principal * (numerator/denominator)
print("The monthly payments are: ", monthly_payments)
