"""
-------------------------------------------------------
Midterm B Task 4 Testing
-------------------------------------------------------
Author: Samiha Mridha
ID:     169060718
Email:  mrid0718@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Imports
# your imports here
from t04_functions import get_it
# your code here
response = input("Y/N: ")
classification = get_it(response)
print(f'{classification}')
