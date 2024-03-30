"""
-------------------------------------------------------
Exam Task 6 Function Definitions
-------------------------------------------------------
Author: Samiha Mridha
ID:     169060718
Email:  mrid0718@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def multiply_list(values):
    """
    -------------------------------------------------------
    Multiplies the value of each element of values by its index.
    Use: multiply_list(values)
    -------------------------------------------------------
    Parameters:
        values - list of elements to multiply (list of int)
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌​​‌​‌‌​‌‌‌​:
        None
    -------------------------------------------------------
    """
    for i in range(len(values)):
        values[i] *= i + 1

    return values
