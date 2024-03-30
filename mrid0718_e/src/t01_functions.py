"""
-------------------------------------------------------
Exam Task 1 Function Definitions
-------------------------------------------------------
Author: Samiha Mridha
ID:     169060718
Email:  mrid0718@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def even_avg(values):
    """
    -------------------------------------------------------
    Returns the average (integer, rounded down) of all even numbers
    in values. If values has no even numbers, the average is 0.
    Use: ea = even_avg(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌​​‌​‌‌​‌‌‌​:
        ea - the average of the even numbers in values (int)
    -------------------------------------------------------
    """
    even_numbers = []
    for number in values:
        if number % 2 == 0:
            even_numbers.append(number)
    if even_numbers:
        ea = sum(even_numbers) // len(even_numbers)
    else:
        ea = 0

    return ea
