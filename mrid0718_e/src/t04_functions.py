"""
-------------------------------------------------------
Exam Task 4 Function Definitions
-------------------------------------------------------
Author: Samiha Mridha
ID:     169060718
Email:  mrid0718@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def draw_x(height):
    """
    -------------------------------------------------------
    Prints a X shape height characters high.
    Use: draw_x(height)
    -------------------------------------------------------
    Parameters:
        height - maximum height in characters of X shape (int >= 3)
    Returns‌​‌​​​​‌​​‌‌‌​‌​‌​​‌​‌‌​‌‌‌​:
        None
    -------------------------------------------------------
    """
    for i in range(height-1):
        print(" " * (height - i) + "#")
        print(" " * i + "#")
